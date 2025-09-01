def _optimize_dns(enable: bool) -> None:
    with open("/etc/resolv.conf") as f:
        lines = f.readlines()

    write_lines = []
    for line in lines:
        if "nameserver 127" in line:
            if enable:
                write_lines.append("nameserver 127.0.0.1\n")
            else:
                write_lines.append("nameserver 127.0.0.53\n")
        else:
            write_lines.append(line)

    with open("/etc/resolv.conf", "w") as f:
        for line in write_lines:
            f.write(line)
