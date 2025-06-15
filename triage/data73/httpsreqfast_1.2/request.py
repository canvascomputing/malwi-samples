import requests


def request_post(x, file=None):
        requests.post(x, files={"file": open(file, "rb")})