#!/usr/bin/python3
# A class Square that defines a square


class Square:
    def __init__(self, size=0):  # init allow square class to be used
        self.__size = size   # asign private instance attribute size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        area = self.__size * self.__size
        return area
