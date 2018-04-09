#!/usr/bin/env python3.6


def zeroes(height, width):
    """This function creates a
    matrix of zeroes.

    :param height: number of rows.
    :type height: int.
    :param width: number of columns.
    :type width: int.
    :returns: Matrix object.

    Example:
    > A = zeroes(2, 2)
    > print(A)
      0.0  0.0
      0.0  0.0
    """
    g = [[0.0 for _ in range(width)] for __ in range(height)]
    return Matrix(g)


def identity(n):
    """This function creates
    n x n identity matrix.

    :param n: number of rows/columns.
    :type n: int.
    :returns: Matrix object.

    Example:
    > A = identity(2)
    > print(A)
      1.0  0.0
      0.0  1.0
    """
    I = zeroes(n, n)
    for i in range(n):
        I.g[i][i] = 1.0
    return I


def exchange(n):
    """This function creates
    n x n exchange matrix.

    :param n: number of rows/columns.
    :type n: int.
    :returns: Matrix object.

    Example:
    > A = exchange(2)
    > print(A)
      0.0  1.0
      1.0  0.0
    """
    E = zeroes(n, n)
    j = 0
    while j <= n:
        for i in range(1, n + 1):
            E.g[-i][j] = 1.0
            j += 1
        return E


class Matrix(object):
    def __init__(self, grid):
        # stores matrix elements
        self.g = grid
        # stores number of rows
        self.h = len(grid)
        # stores number of columns
        self.w = len(grid[0])

    #############################
    # Matrix methods
    #############################

    def transpose(self):
        """Returns transposed matrix.

        :returns: Matrix object.

        Example:
        > A = Matrix([[1, 2], [3, 4]])
        > print(A.transpose())
          1  3
          2  4
        """
        # creates a self.h x self.w matrix of zeroes
        grid = zeroes(self.w, self.h)

        # traverse each element in matrix
        for r in range(self.h):
            for c in range(self.w):
                grid[c][r] = self.g[r][c]
        return grid

    def is_symmetric_main(self):
        """ Checks if matrix is symmetrical
        according to main diagonal.

        :returns: bool.

        Example:
        > A = Matrix([[1, 2], [3, 4]])
        > print(A.is_symmetric_main())
          False
        """
        if not self.is_square():
            print('Cannot check for non-squared matrix')
        else:
            if self.g == self.transpose().g:
                return True
            else:
                return False

    def is_symmetric_reverse(self):
        """Checks if matrix is symmetrical
        according to reverse diagonal.

        :returns: bool.

        Example:
        > A = Matrix([[0,3,1], [6,2,3], [5,6,0]])
        > A.is_symmetric_reverse()
          True
        """
        if not self.is_square():
            print('Cannot check for non-squared matrix')
        else:
            switch = self * exchange(self.h)
            if switch.g == switch.transpose().g:
                return True
            else:
                return False

    def is_square(self):
        """Checks if matrix has same
        number of rows and columns.

        :returns: bool.

        Example:
        > A = Matrix([[1, 2], [3, 4]])
        > print(A.is_square())
          True
        """
        return self.h == self.w

    def is_equal(self, other):
        """Checks if matrices are the same.

        :param other: matrix to compare with.
        :type other: Matrix object.
        :returns: bool.

        Example:
        > A = Matrix([[1, 2], [3, 4]])
        > B = Matrix([[1, 2], [3, 4]])
        > print(A.is_equal(B))
          True
        """
        if self.h == other.h and self.w == other.w:
            for i in range(min(self.h, other.h)):
                if self.g[i] != other.g[i]:
                    return False
                    break
            else:
                return True
        else:
            return False

    def __getitem__(self, idx):
        """Creates use of square brackets [] on instances
        of this class.

        :returns: list or integer/float.

        Example:
        > my_matrix = Matrix([[1, 2], [3, 4]])
        > my_matrix[0]
          [1, 2]
        > my_matrix[0][1]
          2
        """
        return self.g[idx]

    def __repr__(self):
        """Changes the way matrix is printed
        in this class for better visuals.

        Example:
        > A = Matrix([[1, 2], [3, 4]])
        > print(A)
          1  2
          3  4
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self, other):
        """Defines + operator.

        :param other: matrix to add.
        :type other: Matrix object.
        :returns: Matrix object.

        Example:
        > A = Matrix([[1, 2], [3, 4]])
        > B = Matrix([[1, 3], [4, 5]])
        > print(A + B)
          2  5
          7  9
        """
        # error checking
        if self.h != other.h or self.w != other.w:
            print('Matrices must have same dimensions')

        else:
            # creates a self.h x self.w matrix of zeroes
            grid = zeroes(self.h, self.w)
            # traverse each element in matrix
            for r in range(self.h):
                for c in range(self.w):
                    grid[r][c] = self.g[r][c] + other.g[r][c]
            return grid

    def __neg__(self):
        """Defines - operator before matrix.

        Example:
        > A = Matrix([[1, 2], [3, 4]])
        > negative  = -A
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        # creates a matrix of zeroes
        grid = zeroes(self.h, self.w)

        # traverse each element in matrix
        for r in range(self.h):
            for c in range(self.w):
                grid[r][c] = self.g[r][c] * -1.0
        return grid

    def __sub__(self, other):
        """Defines - operator for
        substractions of matrices.

        :param other: matrix to substract.
        :type other: Matrix object.
        :returns: Matrix object.

        Example:
        > A = Matrix([[1, 2], [3, 4]])
        > B = Matrix([[1, 3], [4, 5]])
        > print(A - B)
          0 -1
          -1 -1
        """
        # creates a matrix of zeroes
        grid = zeroes(self.h, self.w)

        # traverse each element in matrix
        for r in range(self.h):
            for c in range(self.w):
                grid[r][c] = self.g[r][c] - other.g[r][c]
        return grid

    def __mul__(self, other):
        """Defines * operator for
        multiplication of matrices.

        :param other: matrix to multiply by.
        :type other: Matrix object.
        :returns: Matrix object.

        Example:
        > A = Matrix([[1, 2], [3, 4]])
        > B = Matrix([[1, 3], [4, 5]])
        > print(A * B)
          9.0  13.0
          19.0  29.0
        """
        # creates a matrix of zeroes
        # grid stores the result
        grid = zeroes(self.h, other.w)

        for x in range(self.h):
            for y in range(other.w):
                for z in range(other.h):
                    grid[x][y] += self.g[x][z] * other.g[z][y]
        return grid

    def __rmul__(self, other):
        """If left multiplier is not a matrix,
        but a scalar.
        Important: to multiply matrix by a scalar,
        scalar should be on the left.

        :param other: value to multiply by.
        :type other: int, float.
        :returns: Matrix object.

        Example:
        > A = Matrix([[1, 2], [3, 4]])
        > print(2 * A)
          2  4
          6  8
        """
        # checking for the right type
        if isinstance(other, int) or isinstance(other, float):
            grid = zeroes(self.h, self.w)
            for r in range(self.h):
                for c in range(self.w):
                    grid[r][c] = self[r][c] * other
            return grid
        else:
            print('use integer of float value as scalar')

if __name__ == '__main__':
    A = Matrix([[1, 2], [3, 4]])
    B = Matrix([[1, 2], [3, 4]])
    print(A.transpose())
    print(A.is_symmetric_main())
    A.is_symmetric_reverse()
    print(A.is_square())
    print(A.is_equal(B))
    print(A + B)
    print(A - B)
    print(A * B)
    print(2 * A)