"""This module defines the Triangle class."""

__author__ = "Robinpreet Kaur"
__version__ = "1.0.0"

import math
from shape import Shape

class Triangle:
    """Represents a triangle shape."""

    def __init__(self, color: str, side_1: int, side_2: int, side_3: int):
        super().__init__(color)

        if not isinstance(side_1, int):
            raise ValueError("Side 1 must be numeric.")
        if not isinstance(side_2, int):
            raise ValueError("Side 2 must be numeric.")
        if not isinstance(side_3, int):
            raise ValueError("Side 3 must be numeric.")

        # Triangle Inequality Theorem
        if (side_1 + side_2 <= side_3 or
            side_1 + side_3 <= side_2 or
            side_2 + side_3 <= side_1):
            raise ValueError("The sides do not satisfy the Triangle Inequality Theorem.")

        self._side_1 = side_1
        self._side_2 = side_2
        self._side_3 = side_3

    def __str__(self):
        return (super().__str__() +
                f"\nThis triangle has three sides with the lengths of "
                f"{self._side_1}, {self._side_2} and {self._side_3} centimeters.")

    def calculate_area(self):
        s = (self._side_1 + self._side_2 + self._side_3) / 2  # semi-perimeter
        return math.sqrt(s * (s - self._side_1) * (s - self._side_2) * (s - self._side_3))

    def calculate_perimeter(self):
        return self._side_1 + self._side_2 + self._side_3
