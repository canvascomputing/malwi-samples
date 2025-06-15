class AuthManager:
    def __init__(self):
        self.headers = {'content-type': 'application/json'}
        self.cookies = {}
        self.token = None
