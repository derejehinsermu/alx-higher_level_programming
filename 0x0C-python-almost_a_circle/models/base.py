#!/usr/bin/python3
""" define base class"""


class Base:
    """
    Base class for managing the id attribute in subclasses.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a Base instance.

        Args:
            id (int, optional): The id value to assign. Defaults to None.

        Attributes:
            id (int): The unique identifier for the instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

