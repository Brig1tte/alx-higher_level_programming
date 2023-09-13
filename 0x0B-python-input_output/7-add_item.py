#!/usr/bin/python3
"""
    function to write a script that adds all arguments to a Python list,
    and then save them to a file:

    You must use your function save_to_json_file (5-save_to_json_file.py)
    You must use your function load_from_json_file (6-load_from_json_file.py)
    The list must be saved as a JSON representation
    in a file named add_item.json
    If the file doesn’t exist, it should be created
    You don’t need to manage file permissions / exceptions.
"""


from sys import argv
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"

if not exists(filename) or not isfile(filename):
    json_list = []
else:
    json_list = load_from_json_file(filename)

for arg in argv[1:]:
    json_list.append(arg)

save_to_json_file(json_list, filename)
