"""Handle shell operations for gitgutter"""

from subprocess import getstatusoutput
from typing import List


class BashError(ValueError):
    """The stderr from a failing bash command"""


def run(command_parts: List[str]):
    """Join those parts to a command, run that via bash"""
    command = " ".join(command_parts)
    status, output = getstatusoutput(command)
    if status:
        raise BashError(output)
    return output
