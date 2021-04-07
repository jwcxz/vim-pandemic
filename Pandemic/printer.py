import sys

RED = "\033[1;31m";
YLW = "\033[1;33m";
CLR = "\033[0m";

class Printer:
    def __init__(self):
        pass;

    def message(self, msg):
        print(msg)

    def red_message(self, msg, level):
        print(f"{RED}{level}: {msg}{CLR}", file=sys.stderr)

    def error(self, msg):
        self.red_message(msg, "ERR")

    def warn(self, msg):
        self.red_message(msg, "WRN")
