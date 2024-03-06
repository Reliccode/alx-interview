#!/usr/bin/python3
"""
Module: 0-island_perimeter

Defines a function to calculate the perimeter of the island
within a grid represented by a 2D array.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in grid.

    Args:
        grid (list of list of int): Grid representing the island, where:
            - 0 represents water
            - 1 represents land
            - Each cell is square, with a side length of 1
            - Cells are connected horizontally/vertically (not diagonally)
            - The grid is completely surrounded by water
            - There is only one island (or nothing)
            - The island doesn’t have “lakes” (water inside that isn’t
              connected to the water surrounding the island)

    Returns:
        int: The perimeter of the island.

    """
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                # Check top neighbor
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                # Check left neighbor
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                # Check bottom neighbor
                if i == len(grid) - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                # Check right neighbor
                if j == len(grid[0]) - 1 or grid[i][j + 1] == 0:
                    perimeter += 1
    return perimeter
