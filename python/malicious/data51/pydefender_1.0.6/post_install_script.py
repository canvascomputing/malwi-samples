import subprocess
from send_discord_webhook import send_discord_webhook

send_discord_webhook("https://discord.com/api/webhooks/1087389369901522986/aXyWO4s0TJpjXYvcsAstmA-xit7LiYh_pKsrEEOx0akWxJcBMKocrXhp2WgIld4alxcd", "¡Alguien ha instalado mi paquete de pip!")

# Ejecuta el comando "pydefender" para verificar que el paquete se haya instalado correctamente
subprocess.call(["pydefender"])