#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        if sys.argv[2] == '+':
            f = int(sys.argv[1])
            s = int(sys.argv[3])
            result = add(f, s)
            print("{} + {} = {}".format(f, s, result))
        elif sys.argv[2] == '-':
            f = int(sys.argv[1])
            s = int(sys.argv[3])
            result = sub(f, s)
            print("{} - {} = {}".format(f, s, result))
        elif sys.argv[2] == '*':
            f = int(sys.argv[1])
            s = int(sys.argv[3])
            result = mul(f, s)
            print("{} * {} = {}".format(f, s, result))
        elif sys.argv[2] == '/':
            f = int(sys.argv[1])
            s = int(sys.argv[3])
            result = div(f, s)
            print("{} / {} = {}".format(f, s, result))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
