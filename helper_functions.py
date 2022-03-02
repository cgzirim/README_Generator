import json

def save_to_json_file(dict, filename):
    """Writes a dict to a text file, using JSON representation."""

    with open(filename, 'w') as f:
        json.dump(dict, f)

def load_from_json_file(filename):
    """Returns a dictionary from a JSON file"""

    with open(filename, 'r') as f:
        return json.load(f)