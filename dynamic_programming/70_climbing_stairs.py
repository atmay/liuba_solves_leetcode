"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
"""

from functools import lru_cache


@lru_cache(None)
def climb_stairs(self, n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2
    return self.climbStairs(n - 1) + self.climbStairs(n - 2)


# Bottom up, O(n) space
def climb_stairs2(n):
    if n == 1:
        return 1
    res = [0 for _ in range(n)]
    res[0], res[1] = 1, 2
    for i in range(2, n):
        res[i] = res[i - 1] + res[i - 2]
    return res[-1]


# Bottom up, constant space
def climb_stairs3(n):
    if n == 1:
        return 1
    a, b = 1, 2
    for _ in range(2, n):
        tmp = b
        b = a + b
        a = tmp
    return b
