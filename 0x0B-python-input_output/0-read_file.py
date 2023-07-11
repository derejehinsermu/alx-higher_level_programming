#!/usr/bin/python3
""" Define the function clalled read_file """


def read_file(filename=""):
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            print(line, end="")
