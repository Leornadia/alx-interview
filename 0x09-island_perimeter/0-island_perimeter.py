#!/usr/bin/python3
"""
Calculates the perimeter of an island represented by a 2D grid.

Args:
    grid (list of list of int): A 2D grid where 1 represents land and 0 represents water.

Returns:
    int: The perimeter of the island.
"""
def island_perimeter(grid):
    """Calculates the perimeter of an island in a grid."""

    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  # Found land
                # Check top
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                # Check bottom
                if i == rows - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                # Check left
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                # Check right
                if j == cols - 1 or grid[i][j + 1] == 0:
                    perimeter += 1

    return perimeter
