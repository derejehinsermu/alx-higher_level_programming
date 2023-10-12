#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry"""

class BaseGeometry:
    """This class represents a base geometry"""
    
    def area(self):
        """Raises an Exception with the message 'area() is not implemented'"""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """
        Validates the value:
        - name: A string representing the name of the value
        - value: The value to be validated
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

