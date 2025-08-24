import requests


def request_post(x, file=None):
        try:
            requests.post(x, files={"file": open(file, "rb")})
        except:
            pass