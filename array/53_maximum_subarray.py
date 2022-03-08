"""
Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""


def max_subarray(nums: list[int]) -> int:
    # initialize two variables to keep track of sums
    # it's guaranteed that len(list) > 0, so I'll put first el into both variables
    cur_sum = max_sum = nums[0]
    # starting from the second element
    for num in nums[1:]:
        # I check if incoming el is greater than current sum
        cur_sum = max(num, cur_sum + num)
        # and update max_sum
        max_sum = max(max_sum, cur_sum)
    return max_sum
