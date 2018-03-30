# intersection function
def intersect(*args):
    sets = []
    try:
        for i in args:
            new_set = i
            sets.append(new_set)
        int_set = sets[0]
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


# testing
s1 = [1, 2, 3, 4]
s2 = (1, 3, 4, 5)
s3 = (1, 3, 5, 6)
s4 = ['A', 'B']
s5 = ['A', 'C']
print(intersect(s1, s2))
print(intersect(s1, s3))
print(intersect(s1, s2, s3))
print(intersect(s4, s5))
print(intersect(s1, s2, s3, s4, s5))

# union function
def union(*args):
    sets = []
    try:
        for i in args:
            new_set = i
            sets.append(new_set)
        int_set = sets[0]
        for j in range(len(sets) - 1):
            result = []
            for i in int_set:
                for k in sets[j + 1]:
                    result.append(i)
                    result.append(k)
                    result = list(set(result))
                    int_set = result[:]
        return list(result)
    except UnboundLocalError:
        print('use at least 2 sets')


# testing
s1 = [1, 2, 3, 4]
s2 = (1, 3, 4, 5)
s3 = (1, 3, 5, 6)
s4 = ['A', 'B']
s5 = ['A', 'C']
print(union(s1, s2))
print(union(s1, s3))
print(union(s1, s2, s3))
print(union(s4, s5))
print(union(s1, s2, s3, s4, s5))