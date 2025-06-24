#!/usr/bin/python3
"""This module defines a class Square with getter and setter for size."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialize the square.

        Args:
            size (int): size of the square (default is 0).
        """
        self.size = size  # Setter will validate

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation.

        Args:
            value (int): new size of the square.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the current square area."""
        return self.__size ** 2
