#!/usr/bin/python3.6


import time
import contextlib
import os


@contextlib.contextmanager
def my_context_manager(path, mode):
    """ Logs errors with time of execution and
    moment of error.
    If error has occurred, information is printed in 'path' file
    and re-raises the error.
    Else, does not print anything in 'path' file and drops it.

    :param path: path and name of file.
    :type path: str.
    :param mode: mode to open file with.
    :type mode: str.
    :returns: None.
    """
    start = time.time()
    file = open(path, mode)
    try:
        yield
        file.close()
        os.remove(path)
    except Exception as err:
        file
        print(err, file=file)
        end = time.time()
        print('time of execution {}'.format(end - start), file=file)
        print('error logged at {}'.format(time.ctime()), file=file)
        file.close()
        raise

if __name__ == '__main__':
    with my_context_manager('test.txt', 'w') as file:
        x * 2