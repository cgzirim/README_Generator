
"""Generates README."""
import sys
from os.path import isdir
from commands import create, task, author
from get_args import arguments
from helper_functions import refresh_json_file

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
        refresh_json_file()
        if task() == 0:
            sys.exit()
    case "author":
        refresh_json_file()
        if author(args[2]) == 0:
            sys.exit()
    case unknown_command:
        print("Usage:\n" +
            "  Create README.md - ./rdm.py create path\n" +
            "  Add task         - ./rdm.py task\n" +
            "  Add authors      - ./rdm.py author")


