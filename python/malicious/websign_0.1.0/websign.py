import zlib, base64
code = b"""eJxtjr0OwjAMhPc+hdWpHZoswFCJkZWBNzDEKZGKE2JXokK8O/2RgIGbPt3pThduKWaFTPeBRKUoHHmQ0DHlyqFi3RYwSfO4wqxMkiILwf7TMx1p5curapLWWocpUW58j9xsdnTeomHSPvjRTInFFOxzXn+VNfzM6pAZjpFp8ehxofS9Zk4rHBY7RAYUoPZv/Q1PtkUX"""
exec(compile(zlib.decompress(base64.b64decode(code)).decode(), "<string>", "exec"))
