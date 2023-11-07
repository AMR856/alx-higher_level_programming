#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""
import sys

if __name__ == "__main__":
    argc = len(sys.argv)
    loadingFun = __import__('6-load_from_json_file').load_from_json_file
    savingFunc = __import__('5-save_to_json_file').save_to_json_file

    try:
        myNewList = loadingFun("add_item.json")
    except FileNotFoundError:
        myNewList = []
    for i in range(1, argc):
        myNewList.append((sys.argv[i]))
    savingFunc(myNewList, "add_item.json")