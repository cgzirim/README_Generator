
"""Generates README."""
import sys
from os.path import isdir
from commands import create, task, author
from helper_functions import arguments
from helper_functions import refresh_json_file

"""Documentary"""
args = arguments(sys.argv)
first_arg = args[1]
if first_arg == "create":
    #usage: <create path>
    path = "./"
    if args[2] is not None:
        path = args[2]

    if create(path) == 0:
        sys.exit()
elif first_arg == "task":
    refresh_json_file()
    if task() == 0:
        sys.exit()
elif first_arg == "author":
    refresh_json_file()
    if author(args[2]) == 0:
        sys.exit()
#case unknown_command:
else:
    print("Usage:\n" +
            "  Create README.md - ./rdm.py create path\n" +
            "  Add task         - ./rdm.py task\n" +
            "  Add authors      - ./rdm.py author")


