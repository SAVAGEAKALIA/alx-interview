#!/usr/bin/python3
""" Island Parameter Question """


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in the grid.

    Args:
        grid (list of list of int):
        The grid representing the map (0 = water, 1 = land).

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Start with 4 for the current land cell
                perimeter += 4

                # Check for a neighboring land cell above
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 1

                # Check for a neighboring land cell below
                if i < rows - 1 and grid[i + 1][j] == 1:
                    perimeter -= 1

                # Check for a neighboring land cell to the left
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 1

                # Check for a neighboring land cell to the right
                if j < cols - 1 and grid[i][j + 1] == 1:
                    perimeter -= 1

    return perimeter
