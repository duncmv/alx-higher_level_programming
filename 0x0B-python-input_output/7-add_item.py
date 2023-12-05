#!/usr/bin/python3
""""this module loads an object and adds args to it
then saves it as a JSOn file
"""


from sys import argv
import json
import os.path


save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
if os.path.isfile(filename):
    lis = load(filename)
else:
    lis = []
lis = lis + argv[1:]
save(lis, filename)
