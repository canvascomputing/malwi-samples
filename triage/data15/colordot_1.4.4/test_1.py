#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''test foreground and background colors'''

import time
from colored import fg, bg, attr


def main():

    for color in range(0, 256):
        print('%s This text is colored %s' % (fg(color), attr('reset')))
        print('%s This background is colored %s' % (bg(color), attr('reset')))
        time.sleep(0.1)


if __name__ == '__main__':
    main()
