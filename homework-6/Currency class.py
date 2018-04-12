#!/usr/bin/env python3.6


from abc import ABCMeta, abstractmethod


class Currency(metaclass=ABCMeta):
    """Abstract class for currencies.

    Attributes:
        symbol: string unix symbol for currency.
        currency: string representation of currency name.
        value: int/float nominal value of currency.
        amount: int/float amount of currency you have.
    """
    symbol = 0
    currency = 0
    value = 0

    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        s = '{0} {1}'.format(self.amount, self.symbol)
        return s

    def __add__(self, other):
        if self.currency != other.currency:
            summing = self.amount + other.to(globals()[self.currency]).amount
            return globals()[self.currency](summing)
        if self.currency == other.currency:
            summing = self.amount + other.amount
            return globals()[self.currency](summing)

    def __radd__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            summing = other + self.amount
            return globals()[self.currency](summing)

    def __sub__(self, other):
        if self.currency != other.currency:
            substract = self.amount - other.to(globals()[self.currency]).amount
            return globals()[self.currency](substract)
        if self.currency == other.currency:
            substract = self.amount - other.amount
            return globals()[self.currency](substract)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            result = self.amount * other
            return globals()[self.currency](result)
        else:
            raise TypeError('use actual number')

    def __truediv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            result = self.amount / other
            return globals()[self.currency](result)
        else:
            raise TypeError('use actual number')

    def __eq__(self, other):
        return self.amount == other.amount

    def __le__(self, other):
        return self.amount <= other.amount

    def __ge__(self, other):
        return self.amount >= other.amount

    def __lt__(self, other):
        return self.amount < other.amount

    def __gt__(self, other):
        return self.amount > other.amount

    @abstractmethod
    def to(self):
        """Converts amount of one currency
        to the other.

        :returns: class object.
        """
        pass

    @classmethod
    def course(cls, other):
        """Compares value of currency to the
        other currency.

        :param other: another currency.
        :type other: class.
        :returns: float.
        """
        return cls.value / other.value

    @property
    # attribute _course will be based
    # on initial value of currency
    def _course(self):
        return globals()[self.currency].value

    @_course.setter
    # we can change the value of currency
    # to update it
    def _course(self, update):
        globals()[self.currency].value = update
        return globals()[self.currency].value


class Euro(Currency):
    """Euro class.
    """
    symbol = '€'
    currency = 'Euro'
    value = 70

    def to(self, other):
        """Converts amount of one currency
        to the other.

        :param other: another currency.
        :type other: class.
        :returns: class object.
        """
        return globals()[other.currency]((self.amount *
                                          (self.value / other.value)))


class Dollar(Currency):
    """Dollar class.
    """
    symbol = '$'
    currency = 'Dollar'
    value = 35

    def to(self, other):
        """Converts amount of one currency
        to the other.

        :param other: another currency.
        :type other: class.
        :returns: class object.
        """
        return globals()[other.currency]((self.amount *
                                          (self.value / other.value)))


class Ruble(Currency):
    """Ruble class.
    """
    symbol = '₽'
    currency = 'Ruble'
    value = 1

    def to(self, other):
        """Converts amount of one currency
        to the other.

        :param other: another currency.
        :type other: class.
        :returns: class object.
        """
        return globals()[other.currency]((self.amount *
                                          (self.value / other.value)))

if __name__ == '__main__':
    e = Euro(5)
    print(e)
    print(e * 2.5)
    print(e / 2)
    print(e.to(Dollar))
    print(sum([Euro(i) for i in range(5)]))
    print(e > Euro(6))
    print(e + Dollar(10))
    print(Dollar(10) + e)
    print(e.to(Dollar))
    print(e.course(Dollar))
    print(e.currency)
    print(e == Euro(5))
    print(e - Dollar(6) + Ruble(70))
    print(Euro.course(Dollar))
    e._course = 210
    print(Euro.course(Dollar))
    print(e.to(Dollar))
