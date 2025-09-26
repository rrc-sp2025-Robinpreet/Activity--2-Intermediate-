"""This module defines the Rectangle class."""

__author__ = "Robinpreet Kaur"
__version__ = "1.0.0"

from shape import Shape

class Rectangle:
    """Represents a rectangle shape."""

    def __init__(self, color: str, length: int, width: int):
        super().__init__(color)

        if not isinstance(length, int):
            raise ValueError("Length must be numeric.")
        if not isinstance(width, int):
            raise ValueError("Width must be numeric.")

        self._length = length
        self._width = width

    def __str__(self):
        return (super().__str__() +
                f"\nThis rectangle has four sides with the lengths of "
                f"{self._length}, {self._width}, {self._length} and {self._width} centimeters.")

    def calculate_area(self):
        return self._length * self._width

    def calculate_perimeter(self):
        return 2 * (self._length + self._width)

