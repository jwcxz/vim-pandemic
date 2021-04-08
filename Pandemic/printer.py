"""Handle printing for pandemic"""

import sys


def info(msg):
    print(msg)


def _red_message(msg, level):
    red = "\033[1;31m"
    no_colour = "\033[0m"
    print(f"{red}{level}: {msg}{no_colour}", file=sys.stderr)


def error(msg):
    _red_message(msg, "ERR")


def warn(msg):
    _red_message(msg, "WRN")
