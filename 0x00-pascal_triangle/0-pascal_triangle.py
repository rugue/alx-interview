#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """
    a function that returns a list
    of integers representing the
    pascal triangle of n:
       . Returns an empty list if n <= 0
       . assume n will be always an integer
    """
    pascal_tri = []

    if n <= 0:
        return []

    for i in range(n):
        if (i == 0):
            pascal_tri.append([1])
        else:
            cur_row = []
            for j in range(i + 1):
                if (j == 0 or j == i):
                    cur_row.append(1)
                else:
                    cur_row.append(pascal_tri[i - 1][j - 1] +
                                   pascal_tri[i - 1][j])

            pascal_tri.append(cur_row)

    return (pascal_tri)def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]  # Start with the first row

    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]  # First element is always 1

        for j in range(1, i):
            new_row.append(prev_row[j-1] + prev_row[j])

        new_row.append(1)  # Last element is always 1
        triangle.append(new_row)

    return triangle
