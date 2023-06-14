#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniq_integers = set()

    for element in my_list:
        if element not in uniq_integers:
            uniq_integers.add(element)

    sum_unique = sum(uniq_integers)

    return sum_unique
