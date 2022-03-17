"""
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected
4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],
[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],
[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
"""

"""
Solution explained:

I started with initiating a variable for result (max_area).
For every cell in the grid if cell == 1 I called a helper function where depth first search is used.

Base case for recursion is reaching boundaries and case where current cell equals 0. I avoided using additional 
memory for visited cells by setting visited cells to 0 after they've been explored.
"""


def max_area_of_island(grid: list[list[int]]) -> int:
    max_area = 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == 1:
                max_area = max(max_area, explore(grid, r, c))
    return max_area


def explore(grid, r, c):
    if (r < 0 or r >= len(grid)) or (c < 0 or c >= len(grid[r])):
        return 0
    if grid[r][c] == 0:
        return 0
    # mark as visited
    grid[r][c] = 0
    return 1 + explore(grid, r - 1, c) + explore(grid, r, c - 1) \
           + explore(grid, r + 1, c) + explore(grid, r, c + 1)
