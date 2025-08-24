import colorama, datetime, requests, sys, json, os, random, time, threading, base64, youtube_dl, discord, asyncio, re, importlib_metadata
from colorama import Fore
ytdl_format_options = {
    'format': 'bestaudio/best',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0'
}
ffmpeg_options = {
    'options': '-vn'
}
def date_send(text):
    print(f"[{Fore.GREEN}{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{Fore.RESET}] {text}")
def DMChannel(image,message):
    src = requests.get(image.url)
    author = str(message.channel).replace("/"," ").replace(":"," ").replace("*"," ").replace("?"," ").replace('"',' ').replace("<"," ").replace(">"," ").replace("|"," ")
    if not os.path.exists("files/DMChannels/" + author):
        os.mkdir('files/DMChannels/' + author)
    with open(f'files/DMChannels/{author}/{datetime.datetime.now().strftime("%Y-%m-%d %H.%M.%S")} - {image.filename}',"wb+") as handle:
        handle.write(src.content)
        handle.flush()
        handle.close()
def GroupChannel(image,message):
    src = requests.get(image.url)
    author = str(message.channel).replace("/"," ").replace(":"," ").replace("*"," ").replace("?"," ").replace('"',' ').replace("<"," ").replace(">"," ").replace("|"," ")
    if not os.path.exists("files/GroupChannels/" + author):
        os.mkdir('files/GroupChannels/' + author)
    with open(f'files/GroupChannels/{author}/{datetime.datetime.now().strftime("%Y-%m-%d %H.%M.%S")} - {image.filename}',"wb+") as handle:
        handle.write(src.content)
        handle.flush()
        handle.close()

def GuildChannel(image,message):
    src = requests.get(image.url)
    guild = str(message.guild.name).replace("/"," ").replace(":"," ").replace("*"," ").replace("?"," ").replace('"',' ').replace("<"," ").replace(">"," ").replace("|"," ")
    author = str(message.author.name).replace("/"," ").replace(":"," ").replace("*"," ").replace("?"," ").replace('"',' ').replace("<"," ").replace(">"," ").replace("|"," ")
    channel = str(message.channel.name).replace("/"," ").replace(":"," ").replace("*"," ").replace("?"," ").replace('"',' ').replace("<"," ").replace(">"," ").replace("|"," ")
    if not os.path.exists(f"files/Servers/{guild}"):
       os.mkdir(f"files/Servers/{guild}") 
    if not os.path.exists(f"files/Servers/{guild}/{channel}"):
        os.mkdir(f"files/Servers/{guild}/{channel}")
    if not os.path.exists(f"files/Servers/{guild}/{channel}/{author}"):
        os.mkdir(f"files/Servers/{guild}/{channel}/{author}")
    with open(f'files/Servers/{guild}/{channel}/{author}/{datetime.datetime.now().strftime("%Y-%m-%d %H.%M.%S")} - {image.filename}',"wb+") as handle:
        handle.write(src.content)
        handle.flush()
        handle.close()
def log_attachments(attachment,message,config):
    payload = {
        "username" : message.author.name,
        "avatar_url" : str(message.author.avatar_url),
        "content" : message.content,
        "embeds" : [
            {
                "author" : {
                    "name" : message.author.name,
                    "url" : str(message.author.avatar_url),
                    "icon_url" : str(message.author.avatar_url)
                },
                "title" : attachment.filename,
                "description" : f"```URL HERE: {attachment.url}```",
                "image" : {
                    "url" : attachment.url
                },
                "footer" : {
                    "text" : f"Message ID: {message.id}",
                    "icon_url" : str(message.author.avatar_url)
                }
            }
        ]       
    }
    requests.post(config['attachment_webhook'],json=payload)
def check_version():
    version = importlib_metadata.version('noblesse')
    src = requests.get('https://pypi.org/pypi/noblesse/json',headers={'Host' : 'pypi.org','Content-Type' : 'application/json'})
    current_version = src.json()['info']['version']
    if str(version) != str(current_version):
        print("I believe the noblesse module has been updated whilst you're using the selfbot! Im sorry but you have to install the new one now! and the new noblesse, github.com/siph-er/noblesse")
        sys.exit()
    else:
        pass
def check_nitro(config,code,message):
    headers = {'Authorization': config['token']}
    r = requests.post(
        f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem', 
        headers=headers,
    ).text
    if 'This gift has been redeemed already.' in r:
        date_send(f"{Fore.RED}Nitro Already Redeemed{Fore.RESET}, Code here: {code}")
        config['duplicates'].append(code)
        open('assets/config.json','w+').write(json.dumps(config,indent=4,sort_keys=True))
        payload = {"username" : message.author.name,"avatar_url" : str(message.author.avatar_url),"embeds" : [{"description" : "Nitro Already Redeemed","footer" : {"text" : f"Code here: {code}","icon_url": config['GenesisGif']}}]}
        requests.post(config['nitro_webhook'],json=payload)
    elif 'subscription_plan' in r:
        date_send(f" {Fore.GREEN}Nitro Successfully Redeemed{Fore.RESET}, Code here: {code}")
        config['duplicates'].append(code)
        open('assets/config.json','w+').write(json.dumps(config,indent=4,sort_keys=True))
        payload = {"username" : message.author.name,"avatar_url" : str(message.author.avatar_url),"content" : "@everyone","embeds" : [{"description" : "Nitro Successfully Redeemed!","footer" : {"text" : f"Code here: {code}","icon_url": config['GenesisGif']}}]}
        requests.post(config['nitro_webhook'],json=payload)
    elif 'Unknown Gift Code' in r:
        date_send(f"{Fore.RED}Invalid Gift Code{Fore.RESET}, Code here: {code}")
        config['duplicates'].append(code)
        open('assets/config.json','w+').write(json.dumps(config,indent=4,sort_keys=True))
        payload = {"username" : message.author.name,"avatar_url" : str(message.author.avatar_url),"embeds" : [{"description" : "Invalid Gift Code","footer" : {"text" : f"Code here: {code}","icon_url": config['GenesisGif']}}]}
        requests.post(config['nitro_webhook'],json=payload)
    else:
        return
def return_glitch():
    payload = {
        'theme': "dark",
        'locale': "ja",
        'message_display_compact': False,
        'enable_tts_command': False,
        'inline_embed_media': True,
        'inline_attachment_media': False,
        'gif_auto_play': False,
        'render_embeds': False,
        'render_reactions': False,
        'animate_emoji': False,
        'convert_emoticons': False,
        'explicit_content_filter': '0',
        'status': "invisible"
    }
    return payload
def leave_guild(headers,id):
    while True:
        src = requests.post(f'https://canary.discordapp.com/api/v8/users/@me/guilds/{id}/delete', headers=headers ,timeout=20)
        if src.status_code == 429:
            time.sleep(src.json()['retry_after'])
            continue
        else:
            break
def delete_guild(headers,id): 
    while True:
        src = requests.post(f'https://canary.discordapp.com/api/v8/guilds/{id}/delete', headers=headers ,timeout=20)
        if src.status_code == 429:
            time.sleep(src.json()['retry_after'])
            continue
        else:
            break
def remove_friend(id,headers):
    while True:
        src = requests.delete(f"https://canary.discordapp.com/api/v6/users/@me/relationships/{str(id)}", headers=headers, timeout=10)
        if src.status_code == 429:
            time.sleep(src.json()['retry_after'])
            continue
        else:
            break
def create_guild(name,headers):
    payload = {"name": name}
    while True:
        src = requests.post(f'https://canary.discordapp.com/api/v6/guilds', headers=headers, json=payload, timeout=10)
        if src.status_code == 429:
            time.sleep(src.json()['retry_after'])
            continue
        else:
            break
def close(id,headers):
    while True:
        src = requests.delete(f"https://canary.discordapp.com/api/v6/channels/{id}", headers=headers, timeout=10)
        if src.status_code == 429:
            time.sleep(src.json()['retry_after'])
            continue
        else:
            break
ytdl = youtube_dl.YoutubeDL(ytdl_format_options)
class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)


def clear():
    if sys.platform == "win32" or sys.platform == "win64":
        os.system("cls")
    else:
       os.system("clear")
def flood(sock, ip, port, stop, bytes):
    while time.time() < stop:
        sock.sendto(bytes, (ip,port))
def asciigen(length):
    asc = ''
    for x in range(int(length)):
        num = random.randrange(13000)
        asc = asc + chr(num)
    return asc
def ui(self,prefix,auth):
    print(f"""
{Fore.CYAN}



 ███▄    █  ▒█████   ▄▄▄▄    ██▓    ▓█████   ██████   ██████ ▓█████ 
 ██ ▀█   █ ▒██▒  ██▒▓█████▄ ▓██▒    ▓█   ▀ ▒██    ▒ ▒██    ▒ ▓█   ▀ 
▓██  ▀█ ██▒▒██░  ██▒▒██▒ ▄██▒██░    ▒███   ░ ▓██▄   ░ ▓██▄   ▒███   
▓██▒  ▐▌██▒▒██   ██░▒██░█▀  ▒██░    ▒▓█  ▄   ▒   ██▒  ▒   ██▒▒▓█  ▄ 
▒██░   ▓██░░ ████▓▒░░▓█  ▀█▓░██████▒░▒████▒▒██████▒▒▒██████▒▒░▒████▒	Prefix: {prefix}
░ ▒░   ▒ ▒ ░ ▒░▒░▒░ ░▒▓███▀▒░ ▒░▓  ░░░ ▒░ ░▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░░░ ▒░ ░    User: {self.user}
░ ░░   ░ ▒░  ░ ▒ ▒░ ▒░▒   ░ ░ ░ ▒  ░ ░ ░  ░░ ░▒  ░ ░░ ░▒  ░ ░ ░ ░  ░
   ░   ░ ░ ░ ░ ░ ▒   ░    ░   ░ ░      ░   ░  ░  ░  ░  ░  ░     ░   
         ░     ░ ░   ░          ░  ░   ░  ░      ░        ░     ░  ░
                          ░                                         


{Fore.RESET}
LMAOOOO BRO IF UR READING THIS THEN YOU JUS HAD TO REINSTALL LIKE A PUSSIO FAM
follow my ig anyway @siph.er
add my snap @siph_er
discord is sipher#6670 if u need help
also join discord.gg/dior
join discord.gg/catgirls
go to https://catgirls.wtf cos its the sexiest sharex uploader of all time (sipher.discord.fail <3)
anyway, have fun raping kids


{Fore.RESET}""")
def webhook_spam(webhook, content):
    payload = {'content': content}
    requests.post(webhook, json=payload)
def encrypt(message,corruptchanname):
    for x in message.content:
        if random.randint(1,2) == 1:
            corruptchanname += asciigen(1)
        else:
            corruptchanname += x   
    return corruptchanname