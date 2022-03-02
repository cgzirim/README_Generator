""""""
import json


def arguments(args):
    """Collects command line arguments and prepare it for interpretion
    
    Args:
        args (list): Command line arguments passed to the program.

    Returns list of arguments.

    Documentation: Converts string to respective data type.
                   Use None where an expected command wasn't passed
    """
    
    list = []
    args_len = len(args)

    for arg in args:
        if arg.isnumeric():
            arg = int(arg)
        list.append(arg)

    try:
        if args[2] is True:
            pass
    except IndexError:
        list.append(None)
    
    return (list)

