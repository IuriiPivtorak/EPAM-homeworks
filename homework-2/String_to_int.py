def transformation(string: str):
    """ This function transforms string characters
    into integer values and concatenates them
    into single onebased on ASCII table.

    :param string: String to use.
    :type string: str.
    :returns: int -- the return code.
    :raises: TypeError
    """
    # make a list out of string's characters
    strings = list(string)
    # starting value is not multiplied if len(strings) <= 1
    res = ord(strings[0])
    for c in strings[1:]:
        # if next character value is 0 to 9,
        # multiply previous value(s) by 10 and add it
        if ord(c) < 10:
            res = 10 * res
            res = res + ord(c)
        # if next character value is 10 to 99,
        # multiply previous value(s) by 100 and add it
        elif ord(c) < 100:
            res = 100 * res
            res = res + ord(c)
        # if next character value is 100 to 999,
        # multiply previous value(s) by 1000 and add it
        elif ord(c) < 1000:
            res = 1000 * res
            res = res + ord(c)
    return res
