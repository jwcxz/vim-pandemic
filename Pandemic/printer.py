from __future__ import print_function

import sys

RED = "\033[1;31m";
YLW = "\033[1;33m";
CLR = "\033[0m";

class Printer:
    def __init__(self):
        pass;

    def message(self, msg):
        sys.stdout.write('%s\n', msg)

    def error(self, msg):
        sys.stderr.write('%sERR: %s%s\n' % (RED, msg, CLR))

    def warn(self, msg):
        sys.stderr.write('%sERR: %s%s\n' % (YLW, msg, CLR))
