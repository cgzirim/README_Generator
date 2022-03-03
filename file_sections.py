#!/usr/bin/python3
"""Defines a function that finds positions of a two strings in a file."""
from helper_functions import save_to_json_file, load_from_json_file

def get_section(start_char, stop_char):
    """Returns a tuple containing the position, and line,
    of a two strings in a the README.md file stream.
    
    Args:
        start_char (str): The first string.
        stop_char (str): The second string.
    """
    dict = load_from_json_file(".rdm.txt")
    path = dict["path"]
    flag = 0
    line_num = 0

    with open(path + "README.md", 'r') as f:
        f.seek(0)
        #start bytes
        for line in iter(f.readline, ""):
            line_num += 1
            if start_char in line:
                flag = 1
                break
        if flag == 0: return (None)
        start = f.tell()
        s_line = line_num - 1

        #end bytes
        f.seek(0) 
        flag = 0; line_num = 0
        for line in iter(f.readline, ""):
            line_num += 1
            if stop_char in line:
                flag = 1
                break
        if flag == 0: return (None)
        end = f.tell()
        e_line = line_num

    #start & end: positions of the string in the file.
    #s_line & e_line: strings' line in the file.
    return (start, end, s_line, e_line)