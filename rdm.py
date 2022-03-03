
"""Generates README."""
import sys
from os.path import isdir
from commands import create, task, author
from get_args import arguments

"""Documentary"""
args = arguments(sys.argv)

match args[1]:
    case "create":
        #usage: <create path>
        path = "./"
        if args[2] is not None:
            path = args[2]

        if create(path) == 0:
            sys.exit()
    case "task":
        if task() == 0:
            sys.exit()
    case "author":
        if author(args[2]) == 0:
            sys.exit()
    case unknown_command:
        print("Help message")


