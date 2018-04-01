import math


def transformation(string):
    """ This function transforms string characters
    into integer values and concatenates them
    into single onebased on ASCII table.

    :param string: String to use.
    :type string: str.
    :returns: int -- the return code.
    :raises: TypeError
    """
    # decoding letters as int values
    # and storing them in a list.
    numbers = []
    for c in string:
        number = ord(c)
        numbers.append(number)
        x = numbers[0]
    # using concatenation formula to
    # unite 2 values into 1 repeatedly.
    for i in range(len(numbers) - 1):
        x = x * 10 ** (math.floor(
            math.log10(numbers[i + 1])) + 1)\
            + numbers[i + 1]
    return x
