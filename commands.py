"""Defines funtions for each command of the README gen."""

from os.path import isfile, isdir
from helper_functions import save_to_json_file, load_from_json_file
from helper_functions import insert_content, sort_tasks, count_tasks


def create(path):
    """Creates a new README.md file.
    
    Args:
        path (str): Path to create the README.md file

    Returns: On success - 1. Otherwise - 0.
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
    section0_begin = "[comment]: <> (Section_0_begin)\n"
    section0_end = "\n[comment]: <> (Section_0_end)"

    content = section0_begin + "# " + p_title + "\n" + p_description
    content += section0_end

    with open(path + "README.md", 'w') as rdm_file:
        rdm_file.write(content)

    dictionary = {"path": path, "url": p_url}
    save_to_json_file(dictionary, "rdm_gen.json")
    
    return (1)


def task():
    """Add tasks to the README file below the first section.
    
    Args:
        path (str): Path to save the README.md file.
    Returns: If task was created successfully - 1
             Otherwise - 0
    """
    dict = load_from_json_file("rdm_gen.json")
    path = dict["path"]
    p_url = dict["url"]
    
    if isfile(path + "README.md") is False:
        print("README.md file has to exist to add tasks.")
        return (0)

    with open(path + "README.md", 'r+') as rdm_file:
        if "[comment]: <> (Section_1_begin)" in rdm_file.read():
            dict["task_exist"] = 1
        else:
            dict["task_exist"] = 0

    save_to_json_file(dict, "rdm_gen.json")

    # When task() is called for the first time input the task header and
    # make it's boundries
    if dict['task_exist'] == 0:
        task_header = "## Tasks \n"
        section1_begin = "\n[comment]: <> (Section_1_begin)\n"
        section1_end = "\n[comment]: <> (Section_1_end)"
        dict['tasks_num'] = 1
    else:
        task_header = ""
        section1_begin = ""
        section1_end = ""
        dict['tasks_num'] = count_tasks() + 1

    #Task title
    tsk_title = input ("Task's title: ")
    
    #File(s) created to complete task
    file_info = input ("<file name: file description>: ")
    file_name = "".join(file_info[:file_info.index(':')])
    file_description = "".join(file_info[file_info.index(':'):])
    file_url = p_url + "/" + file_name

    if tsk_title == "" or file_info == "":
        return (0)

    content =  section1_begin
    content += task_header
    content += "[comment]: <> (task_{}_begin)\n".format(dict['tasks_num'])
    content += "\t - #### " + tsk_title + "\n"
    content += "\t - " + file_url + file_description + "\n"
    content += "[comment]: <> (task_{}_end)\n\n".format(dict['tasks_num'])
    content += section1_end

    if dict['task_exist'] == 0:
        # Add the task section under section 0
        insert_content(content, dict['section0'][1] + 1)
    else:
        # Add tasks within the task section
        insert_content(content, dict['section1'][1])

    save_to_json_file(dict, "rdm_gen.json") 
    sort_tasks()      

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

    dict = load_from_json_file("rdm_gen.json")
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
             