#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0

    try:
        for element in my_list[:x]:
            print(element, end = "")
            count += 1
    except IndexError:
        print("Index dosen't exist")
    finally:
        print()
    return (count)

