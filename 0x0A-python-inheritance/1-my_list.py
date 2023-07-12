#!/usr/bin/python3
"""class MyList that inherits from list:"""


class MyList(list):
    def print_sorted(self):
        """
        Prints the list in ascending order (sorted).

        Returns:
            None
        """
        sorted_list = sorted(self)
        print(sorted_list)
