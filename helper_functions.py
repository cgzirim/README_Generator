"""This file contains all the helper functions used in commands.py

list of funtions in alphabetical order:
    - arguments(): line 9
    - 
"""
import json


def save_to_json_file(dict, filename):
    """Writes a dict to a text file, using JSON representation."""

    with open(filename, 'w') as f:
        json.dump(dict, f)

def load_from_json_file(filename):
    """Returns a dictionary from a JSON file"""

    with open(filename, 'r') as f:
        return json.load(f)

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



def get_line(start_char):
    """Returns a tuple containing the cursor position, and line,
    of strings in the README.md file stream.
    
    Args:
        start_char (str): The first string.

    if start_char isn't found, it returns -1
    """
    dict = load_from_json_file("rdm_gen.json")
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
        if flag == 0:
            print("get_line func: '{}' not found".format(start_char))
            return -1
        seek = f.tell()
        line_idx = line_num - 1

    #start & end: positions of the string in the file.
    #s_line & e_line: strings' line in the file.
    return (seek, line_idx)




def insert_content(content='', line=None):
    """Insert string in a given position of a file.
    
    Args:
        line (int): line to insert string.
        content (str): string to insert into the specified position.
    """
    if content == '' or line == None:
        return
    
    dict = load_from_json_file("rdm_gen.json")
    path = dict["path"]

    content + "\n"
    with open(path + "README.md", "r+", encoding="utf-8") as f:
        contents = f.readlines()
    with open(path + "README.md", "w", encoding="utf-8") as f:  
        contents.insert(line, content)
        contents = "".join(contents)
        f.write(contents)

def delete_content(line1, line2):
    """Deletes lines the README file.
    
    Args:
        line1 (int): Line to begin deletion.
        line2 (int): Line to end deletion.
    """
    dict = load_from_json_file("rdm_gen.json")
    path = dict["path"]
    
    with open(path + "README.md", "r") as f:
        contents = f.readlines()
    with open(path + "README.md", "w") as f:
        difference = [line for line in contents \
            if line not in contents[line1:line2 + 1]]
        contents = "".join(difference)
        f.write(contents)



def get_section(section_begin, section_end):
    """Returns a tuple of line index of pecified strings in the README file.
    A section could be literally any segment in the README file. For example
    the lines the contents of the Project's descriprion occupies.
    
    Args:
        section_begin (str): The name of the section to get it's line index.
        section_end (str): The name of the next section where which the current section's boundary ends.

    """
    if get_line(section_begin) == -1 or get_line(section_end) == -1:
        return
    begin_idx = get_line(section_begin)[1]
    end_idx = get_line(section_end)[1]

    return (begin_idx, end_idx)

def count_tasks():
    """
    Counts the number of tasks in the README file.
    Adds the sum into the JSON file.

    Returns: If the function is successful - the sum
             Otherwise - -1
    """
    dict = load_from_json_file("rdm_gen.json")
    path = dict["path"]

    if dict['task_exist'] == 0:
        return (-1)
    with open(path + "README.md", 'r') as f:
        f_lines = f.readlines()

    i = 1
    count = 0
        
    for line in f_lines:
        if "[comment]: <> (task_{}_begin)".format(i) in line:
            count += 1
            i += 1

    dict['tasks_num'] = count
    save_to_json_file(dict, "rdm_gen.json")
    
    return count


def refresh_json_file():
    """
    Adds or updates 'begin' and 'end' lines of all sections to the json file.
    """
    dict = load_from_json_file("rdm_gen.json")
    path = dict["path"]

    with open(path + "README.md", "r") as f:
        line_idx = 0
        for line in f.readlines():
            if "[comment]: <> (Section_0_begin)" in line:
                begin = line_idx
                dict['section0'] = (begin, None)
            if "[comment]: <> (Section_0_end)" in line:
                end = line_idx
                dict['section0'] = (begin, end)
            
            if "[comment]: <> (Section_1_begin)" in line:
                begin = line_idx
                dict['section1'] = (begin, None)
            if "[comment]: <> (Section_1_end)" in line:
                end = line_idx
                dict['section1'] = (begin, end)
            line_idx += 1

    save_to_json_file(dict, 'rdm_gen.json')


def sort_tasks():
    """Sorts the tasks in ascending order.
    
    Returns: if the sort didn't happen - 0. Otherwise - 1
    """
    # Flow:
    #1. Go through each task section and get its content.
    #2. Get the first number in the gotten content and make it
    #   key and the content the value of a dictionary
    #3. Sort the keys in an ascending order.
    #4. Delete contents in all sections and insert content from the dictionary
    #   in ascending order.
    #
    # If the content in a section doesn't have a number append it to
    # 'tasks without nums' section.
    count_tasks()
    dict = load_from_json_file("rdm_gen.json")
    path = dict["path"]
    tasks_sections = []

    if dict['task_exist'] == 0:
        return 0

    for i in range(1, dict['tasks_num'] + 1):
        t_begin = "[comment]: <> (task_{}_begin)".format(i)
        t_end = "[comment]: <> (task_{}_end)".format(i)
        tasks_sections.append(get_section(t_begin, t_end))

    
    dictionary = {}
    with open(path + "README.md", 'r') as f:
        lines = f.readlines()
        key_false = 0
        for t_begin, t_end in tasks_sections:
            content = []
            for i in range(t_begin + 1, t_end):
                # Get the key from the first line in a task.
                line = lines[i]
                for j in range(len(line) - 1):
                    if line[j].isnumeric() and line[j+1] == ".":
                        key = int(line[j])
                content += lines[i]
                value = "".join(content)

            # If a key wasn't generated for a task, it means that
            # task wasn't numbered: generate a with a negative number
            # as its key.
            try:
                # Do not use an existing key for a new content:
                if key in dictionary.keys():
                    key_false -= 1
                    dictionary[key_false] = value
                else:
                    dictionary[key] = value
            except UnboundLocalError:
                key_false -= 1
                dictionary[key_false] = value

    #Sort tasks
    key_list = [k for k in dictionary.keys()]
    if key_list == sorted(key_list):
        return 0
    
    key_list.sort()

    # Delete all tasks in the Task section
    for i in range(1, len(key_list) + 1):
        t_begin = "[comment]: <> (task_{}_begin)".format(i)
        t_end = "[comment]: <> (task_{}_end)".format(i)

        begin, end = get_section(t_begin, t_end)
        delete_content(begin + 1, end - 1)

    i = 1
    # Append sorted tasks that are numbered in the Task section
    for key in key_list:
        t_begin = "[comment]: <> (task_{}_begin)".format(i)
        t_end = "[comment]: <> (task_{}_end)".format(i)

        if key >= 0:
            begin, end = get_section(t_begin, t_end)
            insert_content(dictionary[key], end)
            i += 1
    
    # Append unnumbered task below numbered tasks
    for key in key_list:
        t_begin = "[comment]: <> (task_{}_begin)".format(i)
        t_end = "[comment]: <> (task_{}_end)".format(i)

        if key < 0:
            begin, end = get_section(t_begin, t_end)
            insert_content(dictionary[key], end)
            i += 1

    refresh_json_file()
    return 1


def update_task(task_title):
    """Updates a task if it exists.
    
    Args:
        task_title (str): Title of the task.

    Documentation: Appends the update to the end of the task.
    """
    count_tasks()
    refresh_json_file()
    dict = load_from_json_file("rdm_gen.json")
    path = dict["path"]

    if dict['task_exist'] == 0:
        return 0

    flag = 0
    for i in range(1, dict['tasks_num'] + 1):
        t_begin = "[comment]: <> (task_{}_begin)".format(i)
        t_end = "[comment]: <> (task_{}_end)".format(i)
        t_section = get_section(t_begin, t_end)

        with open(path + 'README.md', 'r') as f:
            lines = f.readlines()
        for line in lines[t_section[0]:t_section[1]]:
            if task_title in line:
                flag = 1
                break
        if flag == 1:
            break

    if flag == 0:
        return 0

    update = input("insert update: ")
    update = "\t- " + update + "\n"

    insert_content(update, t_section[1] - 1)

    return 1
            
