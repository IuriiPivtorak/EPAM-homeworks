# intersection function
def intersect(*args):
    """ This function makes
    intersections between sets.

    :param args: sets to use.
    :type args: str, list, tuple, set.
    :returns: set of intersected elements.
    :raises: 'use at least 2 sets'
    """
    # preparing the list to store sets of elements.
    sets = []
    try:
        for i in args:
            new_set = list(i)
            sets.append(new_set)
        int_set = sets[0]
        # finding intersections between 2 lists,
        # making list out of them,
        # using this list to find intersections with
        # next one.
        for j in range(len(sets) - 1):
            result = []
            for i in int_set:
                if i in sets[j + 1]:
                    result.append(i)
                    int_set = result[:]
                else:
                    pass
        return set(result)
    except UnboundLocalError:
        print('use at least 2 sets')


# union function
def union(*args):
    """ This function makes
    unions between sets.

    :param args: sets to use.
    :type args: str, list, tuple, set.
    :returns: set of unified elements.
    :raises: 'use at least 2 sets'
    """
    # preparing the list to store sets of elements.
    sets = []
    try:
        for i in args:
            new_set = list(i)
            sets.append(new_set)
        int_set = sets[0]
        # creating list of unique unified
        # elements of 2 sets,
        # uniting this list with next one, etc.
        for j in range(len(sets) - 1):
            result = []
            for i in int_set:
                for k in sets[j + 1]:
                    result.append(i)
                    result.append(k)
                    result = list(set(result))
                    int_set = result[:]
        return set(result)
    except UnboundLocalError:
        print('use at least 2 sets')