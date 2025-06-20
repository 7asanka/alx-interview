#!/usr/bin/python3
"""Island Perimeter"""


def island_perimeter(grid):
    """Calculates the perimeter of the island in the grid"""
    if not grid or not grid[0]:
        return 0

    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4

                # Check if there's land above
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2

                # Check if there's land to the left
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter
