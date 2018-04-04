#!/usr/bin/env


import functools


def decorator_with_args(decorator_to_enhance):
    """This function is decorator
    for decorators.
    """
    @functools.wraps(decorator_to_enhance)
    def decorator_maker(*args, **kwargs):
        def decorator_wrapper(func):
            return decorator_to_enhance(func, *args, **kwargs)
        return decorator_wrapper
    return decorator_maker


@decorator_with_args
def validate(func, low_bound, upper_bound):
    """ This function checks if values are in
    inputed values.

    :param func: function to decorate.
    :type func: function.
    :param low_bound: input lower bound here.
    :type low_bound: integer.
    :param upper_bound: input upper bound here.
    :type upper_bound: integer.
    :returns: wrapper function.
    """
    @functools.wraps(func)
    def wrapper(pixel_values: tuple):
        for element in pixel_values:
            if element < low_bound or element > upper_bound:
                print('Function is not callable!')
                break
        else:
            return func(collection)
    return wrapper


@validate(low_bound=0, upper_bound=256)
def set_pixel(pixel_values: tuple):
    """ This function print "Pixel created!"
    if pixel_values are between 0 and 256
    and "Function is not callable!" otherwise.

    :param pixel_values: values to input.
    :type pixel_values: tuple of length 3 with
    integer values.
    :returns: None.
    """
    print('Pixel created!')

if __name__ == '__main__':
    set_pixel((1, 2, 300))
