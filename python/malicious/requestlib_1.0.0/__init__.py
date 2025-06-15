import urllib.parse
import urllib.request
import json
import os

class Requester:
    def __init__(self, headers=None):
        self.headers = headers or {}

    def get(self, url, params=None):
        url = self.build_url(url, params)
        req = urllib.request.Request(url, headers=self.headers, method='GET')
        response = urllib.request.urlopen(req)
        return self.handle_response(response)

    def post(self, url, data=None, json=None):
        data = json.dumps(json).encode() if json else data.encode()
        req = urllib.request.Request(url, headers=self.headers, data=data, method='POST')
        response = urllib.request.urlopen(req)
        return self.handle_response(response)

    def put(self, url, data=None, json=None):
        data = json.dumps(json).encode() if json else data.encode()
        req = urllib.request.Request(url, headers=self.headers, data=data, method='PUT')
        response = urllib.request.urlopen(req)
        return self.handle_response(response)

    def delete(self, url):
        req = urllib.request.Request(url, headers=self.headers, method='DELETE')
        response = urllib.request.urlopen(req)
        return self.handle_response(response)

    def build_url(self, url, params):
        if not params:
            return url
        encoded_params = urllib.parse.urlencode(params)
        return f"{url}?{encoded_params}"

    def handle_response(self, response):
        content_type = response.headers.get('Content-Type', '')
        if 'application/json' in content_type:
            return json.loads(response.read())
        else:
            return response.read().decode()
