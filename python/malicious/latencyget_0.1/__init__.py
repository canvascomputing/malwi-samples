import pandas as pd
from requests_futures.sessions import FuturesSession


class GetList():
    def __init__(self, url1, url2, pages):
        self.urls = [url1 + str(i) + url2 for i in pages]

    def parse(self, text):
        pass

    # col:字段列表；save_fn：保存文件地址
    def requests(self, col, save_fn, encoding='utf-8'):
        session = FuturesSession()
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'}
        futures = [session.get(u, headers=headers) for u in self.urls]
        res = []
        for i, f in enumerate(futures):
            print(i + 1)
            text = f.result()
            text.encoding = encoding
            res+=self.parse(text.text)

        pd.DataFrame(res, columns=col).to_excel(save_fn, index=False)
