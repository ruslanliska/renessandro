import json


def read_json_file(json_file_path: str):
    """
    Read a JSON file and parse its content into a Python dictionary.

    Args:
        json_file_path (str): The path to the JSON file to be read.

    Returns:
        dict: A Python dictionary containing the parsed JSON data.

    Example Usage:
        json_data = read_json_file('data.json')
    """
    # Open and read the JSON file
    with open(json_file_path, 'r') as json_file:
        # Parse the JSON content into a Python dictionary
        picture_data = json.load(json_file)
    return picture_data


picture = read_json_file('picture.json')
