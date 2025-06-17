"""
__author__ = "Pneb" or "Bernward Sanchez"
"""



import sockets

class pyrequester:
    def __init__(self, url, port, method="GET", headers="", data=""):
        self.url = url
        self.port = port
        self.method = method
        self.headers = headers
        self.data = data

    def get_req(self):
        try:
            s = socket.socket()
            s.connect((self.url, self.port))
            s.send(self.method.encode('utf-8'))
            s.send(self.headers.encode('utf-8'))
            s.send(self.data.encode('utf-8'))
            get_reply = s.recv(1024)
            s.close()
        except:
            get_reply = b'Error'
        return get_reply.decode('utf-8')

    def post_req(self):
        try:
            s = socket.socket()
            s.connect((self.url, self.port))
            s.send(self.method.encode('utf-8'))
            s.send(self.headers.encode('utf-8'))
            s.send(self.data.encode('utf-8'))
            post_reply = s.recv(1024)
            s.close()
        except:
            post_reply = b'Error'
        return post_reply.decode('utf-8')

    def put_req(self):
        try:
            s = socket.socket()
            s.connect((self.url, self.port))
            s.send(self.method.encode('utf-8'))
            s.send(self.headers.encode('utf-8'))
            s.send(self.data.encode('utf-8'))
            put_reply = s.recv(1024)
            s.close()
        except:
            put_reply = b'Error'
        return put_reply.decode('utf-8')