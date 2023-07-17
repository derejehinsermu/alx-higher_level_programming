#!/usr/bin/python3
""" define base class"""

import json


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

    
    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON string representation of a list of dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: The JSON string representation of the list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)


    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): A list of instances that inherit from Base.

        Raises:
            TypeError: If list_objs is not a list.
        """
        if not isinstance(list_objs, list):
            raise TypeError("list_objs must be a list.")

        filename = cls.__name__ + ".json"

        list_dict = []
        if list_objs is not None:
            list_dict = [obj.to_dictionary() for obj in list_objs]

        json_str = cls.to_json_string(list_dict)

        with open(filename, 'w') as file:
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """
        Return the list represented by the JSON string.

        Args:
            json_string (str): The JSON string representation.

        Returns:
            list: The list represented by the JSON string.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)


    @classmethod
    def create(cls, **dictionary):
        """
        Create and return an instance with all attributes already set.

        Args:
            **dictionary:

        Returns:
            object:
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()

        dummy.update(**dictionary)

        return dummy

    classmethod
    def load_from_file(cls):
        """
        Load instances from a file and return a list of instances.

        Returns:
            list: A list of instances loaded from the file.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as file:
                json_str = file.read()
                dict_list = cls.from_json_string(json_str)
                return [cls.create(**dictionary) for dictionary in dict_list]
        except FileNotFoundError:
            return []
