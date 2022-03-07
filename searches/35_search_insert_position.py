"""
Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Input: nums = [1,3,5,6], target = 5
Output: 2
"""


def search_insert(nums: list[int], target: int) -> int:
    """using binary search"""
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return l


def search_insert_2(nums: list[int], target: int) -> int:
    """alternative solution - more effective, time O(n), space O(1)"""
    l = len(nums)
    for i in range(l):
        if nums[i] >= target:
            return i
    return l
