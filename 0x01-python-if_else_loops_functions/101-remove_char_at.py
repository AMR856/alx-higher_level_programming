#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= 0 and n <= len(str) - 1:
        newString = str[:n] + str[n + 1:]
        return newString
    return (str)
