import requests
import time
import random
import json
from string import ascii_letters, digits

class ChatGPT():
    def __init__(self):
        self.user_id = self.get_user_id()
        self.s = requests.Session()
        self.s.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US;q=0.6,en;q=0.5,zh-TW;q=0.4,zh;q=0.3'
        })
        self.json_data = {
            'user_id': self.user_id
        }

    def create_chat(self):
        return self.s.post('https://chat.chatgptdemo.net/new_chat', json=self.json_data).json()['id_']

    def delete_chat(self, chat_id):
        return self.s.post('https://chat.chatgptdemo.net/delete_chat', json={'chat_id': chat_id}).json()

    def get_chats(self):
        return self.s.post('https://chat.chatgptdemo.net/get_user_chat', json=self.json_data).json()

    def get_chat(self, chat_id):
        return self.s.post('https://chat.chatgptdemo.net/get_chat', json={'chat_id': chat_id}).json()

    def send_message(self, chat_id, message):
        data_text = self.s.post('https://chat.chatgptdemo.net/chat_api_stream', json={'question': message, 'chat_id': chat_id, 'timestamp': self.get_timestamp()}).text        
        datas = [json.loads(x.strip().split('data: ')[1])['choices'][0]['delta']['content'] for x in data_text.split('\n') if 'data' in x and not '"finish_reason":"stop"' in x]
        return (''.join(datas)).strip()

    def get_user_id(self):
        return ''.join(random.choices(ascii_letters + digits, k=17))

    def get_timestamp(self):
        return round(time.time())