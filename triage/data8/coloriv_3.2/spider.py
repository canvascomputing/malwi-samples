"""Basic spider tools."""

import requests

DEFAULT_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
}

class Spider(requests.Session):

    def __init__(self, headers=DEFAULT_HEADERS, cache=None):

        super.__init__()
        self.headers = headers
        self.cache = cache

    def request(self, method, url, *args, **kwargs):
        if self.cache:

            




def __test():
    requests.request


if __name__ == '__main__':
    __test()

