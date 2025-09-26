"""This module defines the Shape class."""

__author__ = "Robinpreet Kaur"
__version__ = "1.0.0"


from abc import ABC, abstractmethod

"""Abstract base class representing a geometric shape."""

def __init__(self, color: str):
        """
        Initialize a Shape with a color.
        :param color: The color of the shape. Must not be blank.
        """
        if not color or color.strip() == "":
            raise ValueError("Color cannot be blank.")
        self._color = color.strip()


def __str__(self):
        """Return the description of the shape color."""
        return f"The shape color is {self._color}."


@abstractmethod
def calculate_area(self):
        """Abstract method to calculate area."""
        pass

    
@abstractmethod
def calculate_perimeter(self):
    """Abstract method to calculate perimeter."""
    pass