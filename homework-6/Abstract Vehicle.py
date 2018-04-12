#!/usr/bin/env python3.6


from abc import ABCMeta, abstractmethod


class Vehicle(metaclass=ABCMeta):
    """Vehicle for sale.

    Attributes:
        base sale price: integer starting price.
        wheels: integer number of wheels.
        miles: integer number of miles driven.
        maker: string of firm that made vehicle.
        model: string of model of vehicle.
        year: integer of year of creation.
    """

    base_sale_price = 0
    wheels = 0

    def __init__(self, miles, maker, model, year):
        self.miles = miles
        self.maker = maker
        self.model = model
        self.year = year

    def sale_price(self):
        """Returns the price of purchase.
        If already sold, return 0.

        :returns: int.
        """
        return self.base_sale_price - (0.1 * self.miles)

    @abstractmethod
    def vehicle_type(self):
        """Returns string name of the type.

        :returns: str.
        """
        pass

    @abstractmethod
    def is_motorcycle(self):
        """Returns True or False if
        it's motorcycle or not.

        :returns: bool.
        """
        pass


class Car(Vehicle):
    """A car for sale.

    """

    base_sale_price = 8000
    wheels = 4

    def vehicle_type(self):
        """Returns string name of the type.

        :returns: str.
        """
        return 'car'

    def is_motorcycle(self):
        """Returns True or False if
        it's motorcycle or not.

        :returns: bool.
        """
        if self.wheels == 2:
            return True
        else:
            return False


class Motorcycle(Vehicle):
    """A motorcycle for sale.

    """
    base_sale_price = 2000
    wheels = 2

    def vehicle_type(self):
        """Returns string name of the type.

        :returns: str.
        """
        return 'motorcycle'

    def is_motorcycle(self):
        """Returns True or False if
        it's motorcycle or not.

        :returns: bool.
        """
        if self.wheels == 2:
            return True
        else:
            return False


class Truck(Vehicle):
    """A truck for sale.

    """

    base_sale_price = 5000
    wheels = 4

    def vehicle_type(self):
        """Returns string name of the type.

        :returns: str.
        """
        return 'truck'

    def is_motorcycle(self):
        """Returns True or False if
        it's motorcycle or not.

        :returns: bool.
        """
        if self.wheels == 2:
            return True
        else:
            return False


class Bus(Vehicle):
    """A bus for sale.

    """

    base_sale_price = 25000
    wheels = 4

    def vehicle_type(self):
        """"Returns string name of the type.

        :returns: str.
        """
        return 'bus'

    def is_motorcycle(self):
        """Returns True or False if
        it's motorcycle or not.

        :returns: bool.
        """
        if self.wheels == 2:
            return True
        else:
            return False

if __name__ == '__main__':
    veh = Bus(100000, 'Audi', 'X500', 1994)
    print(veh.sale_price())
    print(veh.vehicle_type())
    print(veh.is_motorcycle())
