#!/usr/bin/python3
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """
    Generates Pascal's Triangle with 'n' rows.

    Args:
    - n (int): Number of rows for Pascal's Triangle.

    Returns:
    - list of lists of integers: Pascal's Triangle representation.

    Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    # Initialize the Pascal's Triangle
    triangle = []

    # Generate each row of the triangle
    for i in range(n):
        # Initialize a row with all elements as 1
        row = [1] * (i + 1)

        # Calculate the values inside the row
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        # Append the row to the triangle
        triangle.append(row)

    return triangle
