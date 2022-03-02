"""
get a command as parameter
read through the readme file and get sections
store gotten sections in the dictionary
returns the start and end of a section of the given parameter.
"""
from helper_functions import save_to_json_file, load_from_json_file

def get_section(header, title, nxt_header):
    """ ... """
    dict = load_from_json_file(".rdm.txt")
    path = dict["path"]
    count = 0

    with open(path + "README.md", 'r') as f:
        f.seek(0)
        for line in iter(f.readline, ""):
            if header in line:
                break
        start = f.tell()

        f.seek(0)
        for line in f:
            if nxt_header in line:
                break
        end = f.tell()

    dict[title] = (start, end)
    return (start, end)


print(get_section("# ", "Project's title", "## Tasks"))
tuple = get_section("# ", "Project's title", "## Tasks")

with open("README.md", 'r') as f:
    f.seek(tuple[1])
    print(f.tell())
    for line in f:
        print(line)


