"""
Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated,
and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
"""


def my_sqrt(x: int) -> int:
    """
    Binary search approach.
    The trick is to check whether x is between power 2 of current pivot and power 2 of pivot+1
    """
    l, r = 0, x
    while l <= r:
        mid = (r + l) // 2
        if mid ** 2 <= x < (mid + 1) ** 2:
            return mid
        elif x < mid * mid:
            r = mid - 1
        else:
            l = mid + 1