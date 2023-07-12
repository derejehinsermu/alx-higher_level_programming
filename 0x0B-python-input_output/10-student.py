#!/usr/bin/python3
""" Define class Student """


class Student:
    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with the provided first name, last name, and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the Student instance.

        Args:
            attrs (list): Optional list of attribute names to filter the dictionary representation.
                If provided, only the attribute names contained in this list will be retrieved.
                If not provided or set to None, all attributes will be retrieved.

        Returns:
            dict: The dictionary representation of the Student instance.
        """
        if attrs is None or not isinstance(attrs, list):
            attrs = self.__dict__.keys()

        json_dict = {}
        for attr in attrs:
            if attr in self.__dict__:
                json_dict[attr] = self.__dict__[attr]

        return (json_dict)
