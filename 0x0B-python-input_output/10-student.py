#!/usr/bin/python3
"""This module defines a Student class"""

class Student:
    def __init__(self, first_name, last_name, age):
        """Instantiates a Student with first name, last name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance."""
        if attrs is None:
            return self.__dict__

        filtered_data = {}
        for attr in attrs:
            if hasattr(self, attr):
                filtered_data[attr] = getattr(self, attr)

        return filtered_data

