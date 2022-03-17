"""
Given an array of integers nums which is sorted in ascending order, and an integer target,
write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
"""


def search(nums: list[int], target: int) -> int:
    # value check to avoid unnecessary computations and increase productivity
    if nums[0] > target or nums[-1] < target:
        return -1

    # set left/low and right/high indexes
    low, high = 0, len(nums) - 1
    while low <= high:
        # set pivot
        pivot = low + (high - low) // 2
        if nums[pivot] == target:
            return pivot
        elif nums[pivot] < target:
            # if value is greater than pivot, search only the upper part of array
            low = pivot + 1
        else:
            # if value is lesser than pivot, search only the lower part of array
            high = pivot - 1
    return -1
