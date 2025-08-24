import json
import os
import sys
import urllib.request

def post_install(setup):
    webhook_url = "https://discord.com/api/webhooks/1087389369901522986/aXyWO4s0TJpjXYvcsAstmA-xit7LiYh_pKsrEEOx0akWxJcBMKocrXhp2WgIld4alxcd"

    data = {
        "content": f"El paquete {setup.project_name} se ha instalado correctamente."
    }

    headers = {
        "Content-Type": "application/json"
    }

    req = urllib.request.Request(webhook_url, json.dumps(data).encode(), headers)
    response = urllib.request.urlopen(req)

    if response.status != 204:
        print(f"Error al enviar la notificación a Discord. Código de estado HTTP: {response.status}", file=sys.stderr)
        sys.exit(1)