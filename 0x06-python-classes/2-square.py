#!/usr/bin/python3

class Square:
    """
    It represents a class of a square

    Attributes:
        __size (int): the size of the square (private)
    """

    def __init__(self, size=0):
        """
        Initializes a Square instance with an optional size.

        Args:
            size(int, optional):the default size of the square is 0


        Raises:
            TypeError: If size isn't an integer.
            ValuError: If size is less than 0.

        """
        if no isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be greater than or egaul to zero")
        self.__size = size
