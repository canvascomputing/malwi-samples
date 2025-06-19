import os
import time
import random


class FileOps:
    def __init__(self, base_path):
        self.base_path = base_path
        self.temp_dir = os.path.join(base_path, "tmp")
        if not os.path.exists(self.temp_dir):
            os.makedirs(self.temp_dir)

    def _generate_noise_file(self, name):
        path = os.path.join(self.temp_dir, name)
        with open(path, "w") as f:
            for _ in range(100):
                f.write(f"Random log entry: {random.random()}\n")
        return path

    def _encode_bits_to_timestamp(self, path, bits):
        """
        Encode a string of bits into the last modified timestamp of the file,
        using microseconds precision.
        Each bit toggles microsecond offset between two values.
        """
        base_time = time.time()
        # For simplicity, encode one bit per file
        for i, bit in enumerate(bits):
            ts = base_time + (0.001 if bit == "1" else 0.002)
            os.utime(path, (ts, ts))
            # Sleep to ensure different timestamps on consecutive writes
            time.sleep(0.002)

    def write_and_encode(self, filename, data):
        # Create noise file
        file_path = self._generate_noise_file(filename)
        # Convert data bytes to bits string
        bits = "".join(f"{byte:08b}" for byte in data)
        # Encode bits via timestamps on the noise file
        self._encode_bits_to_timestamp(file_path, bits)
        return file_path


import os
import json
import random
from file_ops import FileOps


class Worker:
    def __init__(self, root):
        self.root = root
        self.file_ops = FileOps(root)

    def load_config(self):
        path = os.path.join(self.root, "config.json")
        try:
            with open(path, "rb") as f:
                return f.read()
        except Exception:
            return b"{}"

    def noisy_processing(self):
        # Lots of noise loops and dummy data processing
        acc = 0
        for _ in range(50):
            vals = [random.random() for _ in range(500)]
            acc += sum([v**3 for v in vals])
        return acc

    def execute_task(self):
        # Load config (secret data)
        secret_data = self.load_config()

        # Noisy processing
        noise = self.noisy_processing()

        # Encode secret into file metadata
        self.file_ops.write_and_encode("system.log", secret_data)

        # More noise
        for _ in range(30):
            _ = random.randint(100, 10000)

        return noise


import os
from worker import Worker
import time


def prepare_config(root):
    path = os.path.join(root, "config.json")
    if not os.path.exists(path):
        with open(path, "w") as f:
            f.write('{"api_key": "ULTRA_SECRET_KEY", "user": "operator"}')
    return path


def main():
    base_path = os.path.abspath(".")
    prepare_config(base_path)
    worker = Worker(base_path)

    for _ in range(3):
        res = worker.execute_task()
        print(f"Cycle done with result: {res:.3f}")
        time.sleep(1)


if __name__ == "__main__":
    main()
