
"""Generates README."""
from asyncio.windows_events import NULL
import sys
from os.path import isdir
from commands import create, task
from get_args import arguments

"""Documentary"""
args = arguments(sys.argv)

match args[1]:
    case "create":
        #usage: <create path>
        path = "./"
        if args[2] is not None:
            path = args[2]

        res = create(path)
        if res == 0:
            sys.exit()
    case "task":
        res = task(args[2])
        if res == 0:
            sys.exit()
    #case "author":
     #   ;
    case unknown_command:
        print("Help message")


