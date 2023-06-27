#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    index = 0
    try:
        while index < list_length:
            try:
                num1 = my_list_1[index]
                num2 = my_list_2[index]
                division = num1 / num2
                result.append(division)
            except TypeError:
                print("wrong type")
                result.append(0)
            except ZeroDivisionError:
                print("division by 0")
                result.append(0)
            except IndexError:
                print("out of range")
                result.append(0)
            finally:
                index += 1
    finally:
        return (result)
