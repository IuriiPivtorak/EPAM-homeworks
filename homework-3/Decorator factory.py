#!/usr/bin/env


import functools


def dial(decorator):
    """ Function to turn on and
    off decorators.
    :param decorator: decorator to decorate.
    :type decorator: function.
    :returns: function to decorate.
    """
    def new_decorator(func):

        decorated = decorator(func)

        def new_decorated(*args):
            if decorator.enabled:
                return decorated(*args)
            else:
                return fn(*args)
        return new_decorated

    def on():
        decorator.enabled = True

    def off():
        decorator.enabled = False
    new_decorator.on = on
    new_decorator.off = off
    on()
    return new_decorator


@dial
def factory(lambda_func):
    """ Decorators factory.

    :param lambda_func: lambda function to apply.
    :type lambda_func: function.
    :returns: function to decorate.
    """
    def decorator(func):
        @functools.wraps(func)
        def decorated2(*args):
            function = func(args[0])
            print(function)
            Applying_lambda = lambda_func(function)
            print(Applying_lambda)
        return decorated2
    return decorator


@dial
def repeat(times):
    """ This function calls each element in tuple
    and sums them according to inputed number of times.

    :param times: times to repeat.
    :type times: integer
    :returns: function to decorate.
    """
    def decorator(func):
        @functools.wraps(func)
        def decorated2(*args):
            total = 0
            times = len(args[0])
            for i in range(times):
                total += func(args[0][i])
                print('total = ', total)
            return total / times
        return decorated2
    return decorator


@factory(lambda x: x**2)
@repeat(4)
def foo(*args):
    """ Just a function which returns
    first argument.

    :param args: data to input.
    :type args: list, tuple.
    :returns: first element after 'factory'
    and 'repeat' were applied.
    """
    return args[0]


if __name__ == '__main__':
    foo([1, 2, 3, 4])
    factory.off()
    foo([1, 2, 3])
