# intersection function
def intersect(*data):
    """ This function makes
    intersections between sets.

    :param data: sets to use.
    :type data: str, list, tuple, set.
    :returns: set of intersected elements.
    :raises: 'use at least 2 sets'
    """
    # preparing the list to store sets of elements.
    sets = []
    try:
        for i in data:
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
        return list(result)
    except UnboundLocalError:
        print('use at least 2 sets')


# union function
def union(*data):
    """ This function makes
    unions between sets.

    :param data: sets to use.
    :type data: str, list, tuple, set.
    :returns: set of unified elements.
    :raises: 'use at least 2 sets'
    """
    # preparing the list to store sets of elements.
    sets = []
    try:
        for i in data:
            new_set = i
            sets.append(list(new_set))
        int_set_1 = sets[0]
        # creating list of unique unified
        # elements of 2 sets,
        # uniting this list with next one, etc.
        for j in range(len(sets) - 1):
            int_set_2 = sets[j + 1]
            for i in int_set_1:
                for k in int_set_2:
                    if i not in int_set_2:
                        int_set_2.append(i)
                        int_set_1 = int_set_2[:]
        return list(int_set_2)
    except UnboundLocalError:
        print('use at least 2 sets')
