"""
Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise,
return the number of negative numbers in grid.

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.

Input: grid = [[3,2],[1,0]]
Output: 0
"""


# binary search solution: binary_search helper function + main func which iterates over the matrix
def binary_search(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
        mid = start + ((end - start) // 2)
        if arr[mid] < 0:
            end = mid
        else:
            start = mid + 1
    return end if arr[end] < 0 else end + 1


def count_negatives_binary(grid: list[list[int]]) -> int:
    m = len(grid)
    n = len(grid[0])
    negatives = 0
    for i in range(m):
        negatives += n - binary_search(grid[i])
    return negatives


# solution with anonymous built-in functions
def count_negatives(grid: list[list[int]]) -> int:
    cnt = 0
    for g in grid:
        cnt += len(list(filter(lambda x: x < 0, g)))
    return cnt
