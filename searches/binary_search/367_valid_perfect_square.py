"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.

Input: num = 16
Output: true

Input: num = 14
Output: false
"""


def is_perfect_square(num: int) -> bool:
    """
    binary search approach
    """
    p1, p2 = 1, num
    while p1 <= p2:
        mid = p1 + (p2 - p1) // 2
        if mid ** 2 == num:
            return True
        elif mid ** 2 > num:
            p2 = mid - 1
        else:
            p1 = mid + 1
    return p1 ** 2 == num
