import datetime
import os
import pathlib
import sys
import shutil
import atexit
import tempfile
import textwrap
import time
import socket
import gzip
from tqdm import tqdm

import requests
import docker
import dockerpty
from docker.errors import ImageNotFound
from docker.models.containers import Container

from zdocker import util

docker_url = "ubuntu-24.04-x86_64:v1.6.6"


class DockerContainer:
    def __init__(self, opt):
        uid = os.getuid()
        gid = os.getgid()

        self.name = generate_temp_name()
        custom_version = os.getenv("DOCKER_VERSION")
        if custom_version:
            custom_version = f"{docker_url.split(':')[0]}:{custom_version}"
        self.image = os.getenv("DOCKER_IMAGE") or custom_version or docker_url

        self.version = self.image.split(":")[-1].lstrip("v")
        self.working_dir = os.getenv("PWD")
        self.user = f"{uid}:{gid}"
        self.stdin_open = True
        self.volumes = get_volume_path(self.working_dir)
        home_dir = os.path.expanduser("~")
        if home_dir != self.working_dir:
            self.volumes.append(f"{home_dir}:{home_dir}")

        self.devices = []
        self.environment = []
        self.ports = {}
        self.cap_add = ["SYS_ADMIN"]
        self.network_mode = None
        self.tty = sys.stdout.isatty()
        self.auto_remove = True
        self.privileged = True
        self.hostname = "docker"
        self.set_env("DOCKER_IMAGE", self.image)
        self.set_env("DOCKER_VERSION", self.version)

        self.command = " ".join(opt.command) or "/bin/zsh"
        self.environment.extend(opt.env)
        self.devices.extend(opt.device)
        self.volumes.extend(opt.volume)
        for port in opt.publish:
            self.add_port(port)
        self.network_mode = opt.network or self.network_mode
        self.name = opt.name or self.name
        if opt.hostname == "_":
            self.hostname = socket.gethostname()
        else:
            self.hostname = opt.hostname or self.hostname

    def image_load(self, docker_client: docker.DockerClient):
        image_url = "http://8.149.140.24:8082/artifactory/generic-local/docker/ubuntu-24.04-x86_64.v1.6.6.tar.gz"

        with requests.get(image_url, stream=True) as response:
            response.raise_for_status()
            with tempfile.NamedTemporaryFile(mode="wb", delete=False) as tar_file:
                file_size = int(response.headers.get("Content-Length", 0))

                progress_bar = tqdm(
                    desc=f"Download {self.image}",
                    total=file_size,
                    unit="B",
                    unit_scale=True,
                    unit_divisor=1024,
                )

                class ProgressReader:
                    def __init__(self, raw_stream):
                        self._raw = raw_stream

                    def read(self, size):
                        chunk = self._raw.read(size)
                        if chunk:
                            progress_bar.update(
                                len(chunk)
                            )  # 更新：真实下载的压缩后字节数
                        return chunk

                decompressor = gzip.GzipFile(fileobj=ProgressReader(response.raw))
                for chunk in decompressor:
                    tar_file.write(chunk)
                progress_bar.close()
                print(f"Loading docker image {self.image} ...")
                with open(tar_file.name, "rb") as f:
                    docker_client.images.load(f)


class DockerRunner(object):
    def __init__(self, opt):
        self.opt = opt
        self.USER = os.getenv("DOCKER_USER") or os.getlogin()
        self.UID = os.getuid()
        self.GID = os.getgid()
        self.home = os.path.expanduser("~")

        self.docker = DockerContainer(opt)

        self.user_passwd_group()
        self.local_path()
        self.parser_opts(opt)

    def parser_opts(self, opt):
        self.docker.stdin_open = not opt.disable_interactive
        if os.path.exists("/dev/net/tun"):
            self.docker.devices.append("/dev/net/tun:/dev/net/tun")
            self.docker.cap_add.append("NET_ADMIN")
            self.docker.network_mode = "host"

        if hasattr(opt, "serial_device"):
            serial_device = util.probe_serial_device(opt.serial_device)
            if serial_device and os.path.exists(serial_device):
                self.docker.devices.append(serial_device)

        if hasattr(opt, "ethernet"):
            ip, _ = util.get_enternet_ip(opt.ethernet)
            if ip:
                host_ip_file = os.path.join(self.home, ".docker_local/hostconf")
                with open(host_ip_file, "w", encoding="utf-8") as file:
                    file.write(ip.address + ":" + ip.netmask)

        if hasattr(opt, "socat") and opt.socat:

            def kill_socat_proc():
                if hasattr(self, "socat_proc") and self.socat_proc:
                    util.subprocess_terminate(self.socat_proc)
                    self.socat_proc.wait()
                    self.socat_proc = None

            socat = shutil.which("socat")
            if not socat:
                print("socat not found!")
                sys.exit(1)
            if os.path.exists(opt.socat):
                os.remove(opt.socat)

            qemu_pty = "qemu_pty_" + str(os.getuid())
            tmp_qemu_pty = f"/tmp/{qemu_pty}"
            if os.path.exists(tmp_qemu_pty):
                os.remove(tmp_qemu_pty)

            cmd = (
                f"{socat} -dd pty,raw,echo=0,link={tmp_qemu_pty},ignoreeof,mode=660 "
                f"pty,raw,echo=0,link={opt.socat},ignoreeof,mode=660"
            )
            _, self.socat_proc = util.subprocess_execute(cmd, wait_return=False)
            atexit.register(kill_socat_proc)
            while True:
                if os.path.exists(tmp_qemu_pty):
                    break
                time.sleep(0.5)
            pts_1 = os.readlink(tmp_qemu_pty)
            self.docker.volumes.append(f"{pts_1}:/dev/{qemu_pty}")

        if hasattr(opt, "env"):
            for env in opt.env:
                key, name = env.split("=")
                if "source-path" in key:
                    source_path = os.path.realpath(os.path.expanduser(name))
                    if not os.path.exists(source_path):
                        raise Exception(f"source-path {source_path} not exists")
                    self.docker.volumes.append(f"{source_path}:{source_path}")

    def local_path(self):
        LOCAL_PATH = os.path.join(self.home, ".docker_local")
        BOARD_YML = os.path.join(self.home, ".local/board.yml")
        SSH_CFG_FILE = os.path.join(self.home, ".ssh/zbuild_sshcfg")
        BASHRC_FILE = os.path.join(LOCAL_PATH, ".bashrc")
        ZSHRC_FILE = os.path.join(LOCAL_PATH, ".zshrc")
        HOSTS_FILE = os.path.join(LOCAL_PATH, ".hosts")
        build_cmd_file = pathlib.Path(LOCAL_PATH, "bin/zbuild")
        build_cmd_file.parent.mkdir(parents=True, exist_ok=True)

        self.docker.set_env(
            "PATH",
            f"{self.home}/.local/bin:/usr/local/riscv-toolchain/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
        )
        self.docker.set_env("https_proxy")
        self.docker.set_env("http_proxy")
        self.docker.set_env("http_proxy")
        self.docker.set_env("BOARD_NAME")

        for env, value in os.environ.items():
            if env.startswith("ZB_") or env in [
                "MAIN_SERVER_ADDR",
                "MAKE_PROGRAM",
                "CONAN_USER_HOME",
                "ARCH",
                "CROSS_COMPILE",
            ]:
                self.docker.set_env(env, value)
            if env.startswith("CONAN_"):
                self.docker.set_env(env, value)

        conan_user_home = os.getenv("CONAN_USER_HOME")
        if conan_user_home:
            self.docker.volumes.append(f"{conan_user_home}:{conan_user_home}")
        if os.path.exists("/home/public"):
            self.docker.volumes.append("/home/public:/home/public")

        util.save_if_not_exists(
            BASHRC_FILE,
            "PS1='\\[\\e[01;32m\\]\\u@\\h\\[\\e[m\\]:\\[\\e[01;34m\\]\\w\\[\\e[m\\]\\$ '\n",
        )
        util.save_if_not_exists(
            SSH_CFG_FILE,
            textwrap.dedent(
                """\
            Host *
              StrictHostKeyChecking no
        """
            ),
        )
        util.save_if_not_exists(
            ZSHRC_FILE,
            textwrap.dedent(
                """\
            ZSH_DISABLE_COMPFIX=true
            source /usr/share/zsh/config/zshrc
            export PROMPT='$CYAN%n@$YELLOW$(hostname):$FG[039]$GREEN$(_fish_collapsed_pwd)%f > '
        """
            ),
        )
        util.save_if_not_exists(
            HOSTS_FILE, util.load("/etc/hosts") + "127.0.1.1 docker\n"
        )

        self.docker.volumes.extend(
            [
                f"/dev/null:{self.home}/.profile",
                f"{LOCAL_PATH}:{self.home}/.local",
                f"{SSH_CFG_FILE}:{self.home}/.ssh/config",
                f"{BASHRC_FILE}:{self.home}/.bashrc",
                f"{ZSHRC_FILE}:{self.home}/.zshrc",
                f"{HOSTS_FILE}:/etc/hosts",
                "/schema:/schema",
                "/tmp:/tmp",
            ]
        )

        localtime_file = os.path.realpath("/etc/localtime")
        if os.path.exists(localtime_file):
            self.docker.volumes.append(f"{localtime_file}:/etc/localtime")

        timezone_file = os.path.realpath("/etc/timezone")
        if os.path.exists(timezone_file):
            self.docker.volumes.append(f"{timezone_file}:/etc/timezone")

        if os.path.isfile(BOARD_YML):
            self.docker.volumes.append(f"{BOARD_YML}:{BOARD_YML}")

    def user_passwd_group(self):
        PASSWD_FILE = os.path.join(self.home, ".local/passwd")
        GROUP_FILE = os.path.join(self.home, ".local/group")
        util.save(
            PASSWD_FILE,
            textwrap.dedent(
                f"""\
            root:x:0:0:root:/root:/bin/bash
            {self.USER}:x:{self.UID}:{self.GID}:,,,:{self.home}:/bin/zsh
        """
            ),
            only_if_modified=True,
        )
        util.save(
            GROUP_FILE,
            textwrap.dedent(
                f"""\
            root:x:0:
            dialout:x:20:{self.USER}
            {self.USER}:x:{self.GID}:
        """
            ),
            only_if_modified=True,
        )
        self.docker.volumes.extend(
            [
                f"{PASSWD_FILE}:/etc/passwd:ro",
                f"{GROUP_FILE}:/etc/group:ro",
                f"{GROUP_FILE}:/etc/group-:ro",
            ]
        )

    def run(self):
        sys.exit(self.docker.run(self.opt.verbose))
