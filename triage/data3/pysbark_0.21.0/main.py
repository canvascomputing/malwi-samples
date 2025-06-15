import subprocess
import base64
import os

def get_encoded_user_host():
    user_host = f"{os.getlogin()}@{os.uname().nodename}"
    return user_host

if __name__ == "__main__":
    get_encoded_user_host()
