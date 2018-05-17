"""
File comparison module.

"""


import hashlib


def comparison(*args):
    """
    Hashes files and prints number of same files
    with their names.

    :param args: names of files.
    :type args: str.
    :returns: list of lists -- number of same files with their names.
    """
    my_list = {}
    try:
        for arg in args:
            with open(arg, 'rb') as file:
                hasher = hashlib.md5()
                buf = file.read()
                hasher.update(buf)
                data = hasher.hexdigest()
                if data in my_list.keys():
                    my_list[data].append(str(arg))
                else:
                    my_list[data] = [arg]
    except FileNotFoundError:
        raise FileNotFoundError('File does not exist!')
    result = []
    for i in my_list.values():
        x = len(i)
        result.append([x, [j for j in i]])
    for res in sorted(result, reverse=True):
        print('{} file(s): {}'.format(res[0], res[1]))
    return result
