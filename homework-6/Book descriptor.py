#!/usr/bin/env python3.6


class Price(object):
    """Descriptor that does not allow
    values not between 0 and 100.
    """

    def __init__(self, initial=None):
        self.val = initial

    def __get__(self, obj, objtype):
        return self.val

    def __set__(self, obj, val):
        if val < 0 or val > 100:
            raise ValueError('Price must be between 0 and 100')
        self.val = val


class Book:
    price = Price()

    def __init__(self, author, name, price):
        self.author = author
        self.name = name
        self.price = price


if __name__ == '__main__':
    b = Book('William', 'The Sound...', 12)
    print(b.price)
    b.price = -12
