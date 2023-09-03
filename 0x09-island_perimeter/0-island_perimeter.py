#!/usr/bin/python3
"""
0-island_perimeter.py
"""
def island_perimeter(grid):
    """Returns the perimeter of the island described in grid."""
    if not grid:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    perimeter = 0
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4  # Each land cell contributes 4 sides to the perimeter

                # Check adjacent cells (up, down, left, right)
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 1  # Subtract 1 if there's land above
                if i < rows - 1 and grid[i + 1][j] == 1:
                    perimeter -= 1  # Subtract 1 if there's land below
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 1  # Subtract 1 if there's land to the left
                if j < cols - 1 and grid[i][j + 1] == 1:
                    perimeter -= 1  # Subtract 1 if there's land to the right

    return perimeter

