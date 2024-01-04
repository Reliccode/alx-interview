def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row.

    Args:- n (int): The number of rows to generate.

    Returns:list of lists of integers: Pascal's triangle.

    Raises: ValueError: If n is not a positive integer.
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    triangle = []
    for i in range(n):
        row = [1]
        if triangle:
            last_row = triangle[-1]
            # Generate next row by summing pairs of elements from prev row
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            row.append(1)
        triangle.append(row)

    return triangle


if __name__ == "__main__":
    try:
        # Example: Generate Pascal's triangle with 5 rows
        triangle = pascal_triangle(5)
        for row in triangle:
            print("[{}]".format(",".join(map(str, row))))
    except ValueError as e:
        print(f"Error: {e}")
