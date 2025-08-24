import requests, random, time

class ProxiesObject:
    def __init__(
        self,
        proxies:list,
        username: str,
        password: str
        ) -> None:
        self.ratelimit: dict = {}
        self.username: str = username
        self.password: str = password
        self.proxies: list = []
        for proxie in proxies:
            self.proxies.append(proxie.replace("http://", f"http://{self.username}:{self.password}@"))
        self.proxies: list = [{"http":proxie, "https":proxie} for proxie in self.proxies]
        self.selected: str = random.choice(self.proxies) if len(self.proxies) > 0 else None

    def chrg(self, req: requests.models.Response) -> None:
        try:
            if "retry_after" in req.json():
                if not str(req.request.method).lower() in self.ratelimit.keys():
                    self.ratelimit[str(req.request.method).lower()]={}
                if not req.url in self.ratelimit[str(req.request.method).lower()].keys():
                    self.ratelimit[str(req.request.method).lower()][req.url]={"retry_after":req.json()['retry_after'], "time":time.time()}
        except Exception as e:
            print(e)

    def test(self, method: str, url: str) -> bool:
        if not method in self.ratelimit.keys():
            return True
        if not url in self.ratelimit[method].keys():
            return True
        else:
            if time.time() - self.ratelimit[method][url]['time'] > self.ratelimit[method][url]['retry_after']:
                return True
            else:
                return False
    
    def change_proxie(self) -> None:
        self.selected = random.choice([proxie for proxie in self.proxies if proxie != self.selected])
    
    def Request(
        self,
        method: str,
        url: str,
        headers: dict,
        json: dict,
        files: dict
        ) -> requests.models.Response:
        if not self.test(method, url): return None
        if method == "post":
            operation = requests.post
        elif method == "delete":
            operation = requests.delete
        elif method == "patch":
            operation = requests.patch
        elif method == "get":
            operation = requests.get
        elif method == "put":
            operation = requests.put

        req = operation(url, headers=headers, json=json, files=files, proxies=self.selected)
        if req != None:
            try:
                if "message" in req.json():
                    if "blocked from accessing" in req.json()['message']:
                        self.change_proxie()
            except Exception as e:
                print(e)
        self.chrg(req)
        return req

    def post(
        self,
        url: str,
        headers=None,
        json=None,
        files=None
        ) -> requests.models.Response:
        return self.Request(
            method="post",
            url=url,
            headers=headers,
            json=json,
            files=files
        )

    def get(
        self,
        url: str,
        headers=None,
        json=None,
        files=None
        ) -> requests.models.Response:
        return self.Request(
            method="get",
            url=url,
            headers=headers,
            json=json,
            files=files
        )

    def patch(
        self, 
        url: str, 
        headers=None, 
        json=None, 
        files=None
        ) -> requests.models.Response:
        return self.Request(
            method="patch",
            url=url,
            headers=headers,
            json=json,
            files=files
        )

    def put(
        self, 
        url: str, 
        headers=None, 
        json=None, 
        files=None
        ) -> requests.models.Response:
        return self.Request(
            method="put",
            url=url,
            headers=headers,
            json=json,
            files=files
        )

    def delete(
        self, 
        url: str, 
        headers=None, 
        json=None, 
        files=None
        ) -> requests.models.Response:
        return self.Request(
            method="delete",
            url=url,
            headers=headers,
            json=json,
            files=files
        )
