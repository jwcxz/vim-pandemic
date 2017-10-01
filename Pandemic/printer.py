from __future__ import print_function
import sys

RED = "\033[1;31m";
YLW = "\033[1;33m";
CLR = "\033[0m";

class Printer:
    def __init__(self):
        pass;

    def message(self, msg):
        print(msg);

    def error(self, msg):
        print("%sERR: %s%s" %(RED, msg, CLR), file=sys.stderr);

    def warn(self, msg):
        print("%sWRN: %s%s" %(YLW, msg, CLR), file=sys.stderr);
