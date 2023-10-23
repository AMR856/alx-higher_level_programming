#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as Anything:
        sys.stderr.write("Exception: {}\n".format(Anything))
        return None
