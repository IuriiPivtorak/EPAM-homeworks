"""
File comparison module.

"""

import os
import hashlib


def directory_check(directory):
    """
    Searches for files in directory and compares them.

    :param directory: directory path.
    :type directory: str.
    :returns: list of lists -- number of same files with their names.
    """
    list_of_files = {}
    try:
        files = os.listdir(directory)
    except FileNotFoundError:
        raise FileNotFoundError('No such directory!')
    for f in files:
        with open(os.path.join(directory, f), 'rb') as file:
            hasher = hashlib.md5()
            buf = file.read()
            hasher.update(buf)
            data = hasher.hexdigest()
            if data in list_of_files.keys():
                list_of_files[data].append(str(f))
            else:
                    list_of_files[data] = [f]
    result = []
    for i in list_of_files.values():
        x = len(i)
        result.append([x, [j for j in i]])
    for res in sorted(result, reverse=True):
        print('{} file(s): {}'.format(res[0], res[1]))
    return result