#!/usr/bin/python3
"""
class Rectangle based on base class
"""


from models.base import Base


class Rectangle(Base):
    """
    Rectangle class, inherits from Base.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a Rectangle instance.

        Args:
            width,height,x,y,id
        """
        super().__init__(id)
        self.__width = None
        self.__height = None
        self.__x = None
        self.__y = None
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter for the width attribute.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width attribute.

        Args:
            value (int): The width value to assign.

        Raises:
            ValueError: if the width is not posive
            TypeError: If the width value is not an integer
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be positive")
        self.__width = value

    @property
    def height(self):
        """
        Getter for the height attribute.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height attribute.

        Args:
            value (int): The height value to assign.

        Raises:
            ValueError:if the height value is not positive
            TypeError: if the height value is not an integer
        """
        if not isinstance(value, int):
            raise TypeError("Heigh must be an integer")
        if value <= 0:
            raise ValueError("Height must be positive")
        self.__height = value

    @property
    def x(self):
        """
        Getter for the x attribute.

        Returns:
            int: The x-coordinate of the rectangle's position.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for the x attribute.

        Args:
            value (int): The x-coordinate value to assign.

        Raises:
            valueError: if the x-coordninate value is negative.
            TypeError: If the y-coordinate value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer.")
        if value < 0:
            raise ValueError("x must be >=0")
        self.__x = value

    @property
    def y(self):
        """
        Getter for the y attribute.

        Returns:
            int: The y-coordinate of the rectangle's position.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for the y attribute.

        Args:
            value (int): The y-coordinate value to assign.

        Raises:
            ValueError: If the y-coordinate value is negative
            TypeError: if the y-coordinate value is not an integer
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer.")
        if value < 0:
            raise ValueError("y must be >= 0.")
        self.__y = value
    
    def area(self):
        """
        Calculate the area of recatngle 
        
        Returns:
            int: the area of the recangle
        """
        return self.width * self.height
    
    def display(self):
        """
        print the rectangle instance using the character '#',
        taking into account x and y offsets.
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def __str__(self):
        """
        return:
            str: the formated string represntation of the rectangle
        """
        return (f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}")

    def update(self, *args, **kwargs):
        """
        update the attributes of the rectangle

        Args:
            *args: id,width, height, x, y.
            **kwargs:
        """
        if args:
            attributes = ["id", "width", "height", "x", "y"]

            for i, arg in enumerate(args):
                if i >= len(attributes):
                    break
                setattr(self, attributes[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
