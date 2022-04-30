"""
You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians).
The soldiers are positioned in front of the civilians.
That is, all the 1's will appear to the left of all the 0's in each row.

A row i is weaker than a row j if one of the following is true:

The number of soldiers in row i is less than the number of soldiers in row j.
Both rows have the same number of soldiers and i < j.
Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.
"""


def k_weakest_rows(mat: list[list[int]], k: int) -> list[int]:
    weak = []
    c, r = len(mat), len(mat[0])
    for col in range(c):
        res = -1
        l, h = 0, r - 1
        while l <= h:
            mid = l + (h - l) // 2
            if mat[col][mid] == 0:
                h = mid - 1
            else:
                res = mid
                l = mid + 1
        weak.append((res, col))
    weak.sort(key=lambda x: x[0], reverse=False)
    return [x[1] for x in weak[:k]]
