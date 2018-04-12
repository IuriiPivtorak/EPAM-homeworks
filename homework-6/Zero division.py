#!/usr/bin/env python3.6


if __name__ == '__main__':
    try:
        times = int(input('input number of pairs: '))
        pairs = []
        for i in range(times):
            pair = input().split()
            pairs.append(pair)
        for pair in pairs:
            print(float(pair[0]) / float(pair[1]))
    except ZeroDivisionError:
        # if 2nd number is 0
        print('Please, do not divide by zero')
    except ValueError:
        # if number is not float/int, if 'times' not int
        print('Please, input an actual number')
    except IndexError:
        # if not 2 numbers were inputed
        print('Please, input 2 numbers')
