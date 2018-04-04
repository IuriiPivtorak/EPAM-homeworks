#!/usr/bin/env


def digits_count(val):
    """ Estimate number of digits for input value.

    :param val:  input value
    :type val: int
    :returns: int -- number of digits
    """
    if val == 0:
        return 0
    n_digits = 1
    while val // 10 > 0:
        n_digits += 1
        val /= 10
    return n_digits


def transformation(input_string):
    """ Convert converts the input string to a number
    that is the concatenation of a string byte
    ("abcd" -> 979899100)

    :param input_string:  input string
    :type input_string: str
    :returns: int -- concatenation of a string byte
    """
    string_list = list(input_string)
    if not string_list:
        return 0
    else:
        value = ord(string_list[::-1][0])
    return (value + transformation(string_list[0:-1]) *
            (10 ** digits_count(value)))

if __name__ == '__main__':
    print(transformation('abcder'))
