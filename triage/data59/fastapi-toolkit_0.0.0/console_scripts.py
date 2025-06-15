import argparse
import os

from cookiecutter.main import cookiecutter


def startproject(args):  # noqa
    dirname = os.path.dirname(os.path.abspath(__file__))
    cookiecutter(os.path.join(dirname, 'project_template'))


def main():
    parser = argparse.ArgumentParser(
        prog='fastapi-toolkit',
    )
    subparsers = parser.add_subparsers()
    parser_startproject = subparsers.add_parser(
        'startproject',
        help='Create new project'
    )
    parser_startproject.set_defaults(func=startproject)

    args = parser.parse_args()
    args.func(args)
