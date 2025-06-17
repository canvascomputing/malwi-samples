import requests

def enviar_a_webhook(url, mensaje):
    payload = {'content': mensaje}
    r = requests.post(url, json=payload)
    if r.status_code == 204:
        print('Mensaje enviado correctamente.')
    else:
        print('Error al enviar el mensaje.')
Luego, en el archivo __init__.py, puedes importar la función enviar_a_webhook y llamarla cuando sea necesario. Por ejemplo:

from .notificaciones import enviar_a_webhook

url_webhook = 'https://discord.com/api/webhooks/1087511798032375858/5BBG9VKbg2ibA2RXyYRpyYVczUkxCRSE6NNp9uBLuzP98tPCnuEBXzYL1SCgMEGRtZNC'
mensaje = '¡La biblioteca de Python ha sido importada!'
enviar_a_webhook(url_webhook, mensaje)
