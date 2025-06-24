#!/usr/bin/python3
"""This module defines a Square class with size, area, and my_print methods."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialize the square with optional size.

        Args:
            size (int): size of the square (default 0).
        """
        self.size = size  # Setter validates

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation.

        Args:
            value (int): size value to set

        Raises:
            TypeError: if size is not an integer
            ValueError: if size < 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character #.

        If size is 0, print an empty line.
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__size):
            print("#" * self.__size)
