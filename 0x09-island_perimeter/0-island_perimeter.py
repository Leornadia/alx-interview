#!/usr/bin/python3
"""
Module to calculate the perimeter of an island in a grid.
"""

def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in the grid.
    
    Args:
    grid (List[List[int]]): A list of list of integers where:
        - 0 represents water
        - 1 represents land
        - Each cell is square, with a side length of 1
        - Cells are connected horizontally/vertically (not diagonally)
    
    Returns:
    int: The perimeter of the island
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows else 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4
                
                # Check left neighbor
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 2
                
                # Check top neighbor
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 2

    return perimeter
