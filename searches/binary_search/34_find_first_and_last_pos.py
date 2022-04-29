"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position
of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Input: nums = [], target = 0
Output: [-1,-1]
"""


def search_range_binary(nums: list[int], target: int) -> list[int]:
    """
    binary search approach, one pass
    """
    start, end = 0, len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        if nums[start] == nums[end] == target:
            return [start, end]
        if nums[mid] < target:
            start = mid + 1
        elif nums[mid] > target:
            end = mid - 1
        else:
            if nums[start] != target:
                start += 1
            if nums[end] != target:
                end -= 1
    return [-1, -1]


def search_range(nums: list[int], target: int) -> list[int]:
    """
    straight forward solution: find index of the first occurrence and iterate from this index while end==target
    """
    if target not in nums:
        return [-1, -1]
    start = cur = nums.index(target)
    while nums[cur] == target:
        if cur + 1 < len(nums) and nums[cur + 1] == target:
            cur += 1
        else:
            break
    return [start, cur]
