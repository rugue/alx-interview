def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]  # First row of Pascal's triangle

    for i in range(1, n):
        prev_row = triangle[-1]  # Get the last row
        new_row = [1]  # Every row starts with 1
        # Generate the middle values of the row
        for j in range(1, i):
            new_row.append(prev_row[j-1] + prev_row[j])
        new_row.append(1)  # Every row ends with 1
        triangle.append(new_row)

    return triangle