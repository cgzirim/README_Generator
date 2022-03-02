"""
./rdm create
check if file exists: readme file already exists. do you want to generate a new one?(n/y)
--> insert project's title:
--> insert URL of this repository
--> projects description

"""

"""Defines funtions for each command"""
from os.path import isfile, isdir
import re
import json
from helper_functions import save_to_json_file, load_from_json_file


def create(path):
    """Creates a new README.md file.
    
    Args:
        path (str): Path to save the README.md file

    Returns: If the file wasn't created - 0
             Otherwise - 1.
    """
    if isfile(path + "README.md"):
        ans = input ("README.md file already exist in this directory. Do you want to generate a new one?(y/n): ")
        if ans == "n":
            return (0)

    if isdir(path) is False:
        print("{}: path doesn't exists".format(path))
        return (0)
    
    p_title = input ("Project's title: ")
    p_url = input ("Insert URL of this repository: ")
    p_description = input ("Project's description: ")

    with open(path + "README.md", 'w') as rdm_file:
        rdm_file.write("# " + p_title + "\n" + p_description)

    dictionary = {"path": path, "url": p_url}
    save_to_json_file(dictionary, ".rdm.txt")
    
    return (1)


def task(num_of_funcs):
    """Add tasks to the README file
    
    Args:
        path (str): Path to save the README.md file.
    Returns: If task was created successfully - 1
             Otherwise - 0
    """
    dict = load_from_json_file(".rdm.txt")
    path = dict["path"]
    p_url = dict["url"]
    
    if isfile(path + "README.md") is False:
        print("README.md file has to exist to add tasks.")
        return (0)

    tsk_title = input ("Task's title: ")
    tsk_description = input ("Task's descriptioin: ")

    if num_of_funcs is None:
        num_of_funcs = 0;

    with open(path + "README.md", 'a') as rdm_file:
        rdm_file.write("\n## Tasks \n" + "\t - #### " + tsk_title + "\n")
        rdm_file.write("\t   " + tsk_description)
        #you should probably print format here
        # and let function promt be num of function.
        for func in range(num_of_funcs):
            func_info = input ("<func name: func description>: ")
            func_name = "".join(re.findall("\A.*:", func_info))
            func_description = "".join(re.findall(":.*", func_info))
            func_url = p_url + "/" + func_name
            rdm_file.write("\n\t - " + func_url + func_description)

    return (1)

