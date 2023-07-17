#!/usr/bin/python3
""" This is module for square class """


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class, inherits from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a Square instance.

        Args:
            size (int), x , y, id

        Raises:
            ValueError: If size is not positive.
            ValueError: If x or y is negative.
            TypeError: If size, x, or y is not an integer.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Getter for the size attribute.

        Returns:
            int: The size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute.

        Args:
            value (int): The size value to assign.

        Raises:
            ValueError: If the size value is not positive.
            TypeError: If the size value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("Size must be an integer.")
        if value <= 0:
            raise ValueError("Size must be > 0.")
        self.width = value
        self.height = value

    def __str__(self):
        """
        Returns:
            str: The formatted string representation of the square.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        """"
        update the attributes of the square

        Args:
            *args, **kwargs
        """
        if args:
            attributes = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                if 1>= len(attributes):
                    break
                setattr(self, attributes[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns:
            dict: The dictionary representation of the square.
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
