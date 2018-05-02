from decimal import Decimal


def triangle_area():
    """
    Calculates area of triangle based on Heron's formula.

    :returns: Decimal -- result of calculation.
    """
    stacks = []
    try:
        for _ in range(3):
            stack = [float(x) for x in input('input 2 values separated by space and press <Enter>: ').split()]
            stacks.append(stack)
    except ValueError:
        raise ValueError('Please, use integer or float values only!')

    if (stacks[0][0] == stacks[1][0] and stacks[0][1] == stacks[1][1]) \
        or (stacks[1][0] == stacks[2][0] and stacks[1][1] == stacks[2][1]) \
        or (stacks[0][0] == stacks[2][0] and stacks[0][1] == stacks[2][1]) \
        or (stacks[0][0] == stacks[1][0] == stacks[2][0] and
        stacks[0][1] == stacks[1][1] == stacks[2][1]):
        raise ValueError('Points cannot be the same!')
    else:
        i = 0
        for _ in range(3):
            for stack in stacks:
                stack[0] = Decimal(stack[0])
                stack[1] = Decimal(stack[1])
                i += 1

        x = stacks[0]
        y = stacks[1]
        z = stacks[2]

        if len(x) == 2 and len(y) == 2 and len(z) == 2:
            a = ((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2) ** Decimal(0.5)
            b = ((x[0] - z[0]) ** 2 + (x[1] - z[1]) ** 2) ** Decimal(0.5)
            c = ((z[0] - y[0]) ** 2 + (z[1] - y[1]) ** 2) ** Decimal(0.5)

            if max(a, b, c) < sum([a, b, c]) - max(a, b, c):
                p = (a + b + c) / 2
                s = (p * (p - a) * (p - b) * (p - c)) ** Decimal(0.5)
                return round(s, 3)

            else:
                raise ValueError('All points cannot lie on the same line!')

        else:
            raise IndexError('Please, input exactly 2 coordinates for each point!')
