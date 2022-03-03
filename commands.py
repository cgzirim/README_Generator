"""
./rdm create
check if file exists: readme file already exists. do you want to generate a new one?(n/y)
--> insert project's title:
--> insert URL of this repository
--> projects description

"""

"""Defines funtions for each command"""
import imp
from os.path import isfile, isdir
import re
import json
from helper_functions import save_to_json_file, load_from_json_file
from file_sections import get_section


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


def task():
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

    with open(path + "README.md", 'r+') as rdm_file:
        #When task() is called for the first time
        if '## Tasks' not in rdm_file.read():
            #Get the project's description section and add 'task' below it.
            p_d_section = get_section("# ", "\n")
            rdm_file.seek(p_d_section[1])
            tsk_title = input ("Task's title: ")
            rdm_file.write("\n## Tasks \n" + "\t - #### " + tsk_title + "\n")

        #you should probably print format here
        # and let function promt be num of function.
        p_d_section = get_section("# ", "## Tasks")
        rdm_file.seek(p_d_section[1])

        file_info = input ("<file name: file description>: ")
        file_name = "".join(re.findall("\A.*:", file_info))
        file_description = "".join(re.findall(":.*", file_info))
        file_url = p_url + "/" + file_name
        rdm_file.write("\n\n\t - " + file_url + file_description + "\n")

        
    return (1)

def author(num_of_authors):
    """Adds names of authors to the README file.
    
    Args:
        num_of_authors (int): The number of authors in the project.

    Returns 1 on success. Otherwise - 0.
    """
    try:
        int(num_of_authors)
    except TypeError:
        print("Usage message.")
        return 0
    if num_of_authors == 0:
        print("Usage message")
        return 0

    dict = load_from_json_file(".rdm.txt")
    path = dict["path"]

    if isfile(path + "README.md") is False:
        print("README.md file has to exist to add authors.")
        return (0)
    
    with open(path + "README.md", 'a') as f:
        for author in range(num_of_authors):
            author_full_name = input("Insert author's full name: ")
            author_github = input("Insert GitHub username: ")
            f.write("\n## Authors")
            f.write("\n\t - {} <{}>".format(author_full_name, author_github))
             