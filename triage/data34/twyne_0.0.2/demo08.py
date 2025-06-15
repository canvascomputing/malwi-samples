from __future__ import print_function
import fixpath
from twyne import expresstext, Fore


def main():
    """automatically reset stdout"""
    with express_text():
        print(Fore.GREEN + 'text is green')
        print(Fore.RESET + 'text is back to normal')

    print('text is back to stdout')

if __name__ == '__main__':
    main()
