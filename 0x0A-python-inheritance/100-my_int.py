#!/usr/bin/python3
"""this module defines a class MyInt that inherits from int"""

class MyInt(int):
    def __eq__(self, other):
        """Invert the == operator."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Invert the != operator."""
        return super().__eq__(other)

