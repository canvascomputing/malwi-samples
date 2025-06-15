
def ec(s: str):
    import base64
    return base64.b64encode(s.encode('utf-8'))
