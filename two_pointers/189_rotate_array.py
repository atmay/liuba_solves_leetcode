"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
"""


def rotate(nums: list[int], k: int) -> list[int]:
    nums1 = nums[k + 1:]
    nums2 = nums[:k + 1]
    nums = nums1 + nums2
    return nums


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6, 7]
    rotate(a, 3)
    # expected: [5, 6, 7, 1, 2, 3, 4]
