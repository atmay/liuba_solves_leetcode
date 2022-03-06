"""
Given an integer array nums sorted in non-decreasing order,
return an array of the squares of each number sorted in non-decreasing order.

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
"""


def sorted_squares(nums: list[int]) -> list[int]:
    nums.sort(key=lambda x: abs(x))
    nums_squares = list(map(lambda x: x ** 2, nums))
    return nums_squares


def sorted_squares_2(nums: list[int]) -> list[int]:
    nums.sort(key=lambda x: abs(x))
    return [el ** 2 for el in nums]


def sorted_squares_3(nums: list[int]) -> list[int]:
    """Most effective in terms of time complexity
    Inplace - O(1) memory"""
    res = [el ** 2 for el in nums]
    res.sort()
    return res
