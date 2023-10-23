#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except Exception as Anything:
        sys.stderr.write("Exception: {}\n".format(Anything))
        return False
    return True
