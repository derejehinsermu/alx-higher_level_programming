#!/usr/bin/python3
def uppercase(string):
    uppercase_string = ""
    for char in string:
        if ord('a') <= ord(char) <= ord('z'):
            uppercase_char = chr(ord(char) - 32)
            uppercase_string += uppercase_char
        else:
            uppercase_string += char
    print("{}".format(uppercase_string))
