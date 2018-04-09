#!/usr/bin/env python3.6


class Wine:
    def __init__(self, name, mark, country, date_of_bottling: int, info):
        self.name = name
        self.mark = mark
        self.country = country
        self.date_of_bottling = date_of_bottling
        self.info = info

    def get_info(self):
        """Prints all inputed info
        about the bottle.

        :returns: None
        """
        print('Name: {0}, '
              'Mark: {1}, '
              'Country of origin: {2}, '
              'Date of bottling: {3}, '
              'Additional information: {4}. '
            .format(
            self.name,
            self.mark,
            self.country,
            self.date_of_bottling,
            self.info))

    def wine_age(self, current_year: int):
        """ Calculates how old is wine in years.

        :param current_year: today's year.
        :type current_year: int.
        :returns: int.
        """
        if isinstance(current_year, int) and isinstance(self.date_of_bottling, int):
            return (current_year - self.date_of_bottling)
        else:
            return 'input year correctly, e.g. 1995'

    def set_name(self, name):
        """ Changes name of bottle.

        :param name: new name.
        :type name: str.
        :returns: None
        """
        self.name = name

    def set_mark(self, mark):
        """ Changes mark of the bottle.

        :param mark: new mark.
        :type mark: str.
        :returns: None
        """
        self.mark = mark

    def set_country(self, country):
        """ Changes country of the bottle.

        :param country: new country.
        :type country: str.
        :returns: None
        """
        self.country = country

    def set_date_of_bottling(self, date):
        """ Changes date of bottling.

        :param date: new date.
        :type date: int.
        :returns: None
        """
        if isinstance(date, int):
            self.date_of_bottling = date
        else:
            return 'input year correctly, e.g. 1995'

    def set_info(self, info):
        """ Changes additional information.

        :param info: new info.
        :type info: str.
        :returns: None
        """
        self.info = info

if __name__ == '__main__':
    bottle_1 = Wine(name='bottle526',
                    mark='Something',
                    country='french',
                    date_of_bottling=1990,
                    info='bad bottle')
    bottle_1.get_info()
    bottle_1.set_name('new bottle')
    bottle_1.get_info()
    print(bottle_1.wine_age(2018))