#!/usr/bin/python3
class Rectangle:
    """
    The Rectangle class create a new object

    Args:
        width (int): integer value of the width
        height (int): integer value of the height

    Attributes:
        width (int): integer value of the width
        height (int): integer value of the height
        number_of_instances (int): integer number of the instances creates
        print_symbol (str): print with the symbol
    """

    number_of_instances = 0

    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def area(self):
        """
        Function area the rectangle

        Formule: width * height = area

        Returns:
            area

        """
        return self.width * self.height

    def perimeter(self):
        """
        Function petimeter the rectangle

        Formule: 2*(width + height)

        Returns:
            perimeter

        """
        w, h = self.width, self.height
        return 0 if (w or h) == 0 else 2*(w + h)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Function static bigger rectangle base on the area

        Args:
            rect_1 (Rectangle): first rectangle for compare
            rect_2 (Rectangle): second rectangle for compare

        Returns:
            the biggest rectangle
        """
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() == rect_1.area():
            return rect_1
        elif rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1

    @property
    def width(self):
        """Get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width"""
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set heigth"""
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def __str__(self):
        """Print the rectangle with the character #"""
        __list = ""
        w, h = self.width, self.height
        if (w or h) == 0:
            _list = ""
        else:
            for x in range(h):
                for y in range(w):
                    __list += str(self.print_symbol)
                if x != h - 1:
                    __list += '\n'

        return __list

    def __repr__(self):
        """Return: string representation of the rectangle"""
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        """del object print"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
