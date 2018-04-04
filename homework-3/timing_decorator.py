#!/usr/bin/env


import functools
import time


def timing(func):
    """ This function calculates time
    requires to execute function "func".

    :param func: function to input
    :type func: function
    :returns: time required
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print('time: {}'.format(end-start))
        return result
    return wrapper


@timing
def foo(number):
    """ This is function just to test timing decorator.
    It returns square of inputed number.

    :param number: value to input.
    :type number: integer.
    :returns: squared number.
    """
    return number ** 2

if __name__=='__main__':
    print(foo(2))