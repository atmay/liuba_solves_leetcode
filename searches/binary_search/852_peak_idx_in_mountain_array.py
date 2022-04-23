"""
Let's call an array arr a mountain if the following properties hold:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... arr[i-1] < arr[i]
arr[i] > arr[i+1] > ... > arr[arr.length - 1]
Given an integer array arr that is guaranteed to be a mountain, return any i such that
arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

Input: arr = [0,1,0]
Output: 1

Input: arr = [0,2,1,0]
Output: 1

Input: arr = [0,10,5,2]
Output: 1
"""


def peak_index_in_mountain_array(arr: list[int]) -> int:
    """
    binary search approach
    """
    left, right = 0, len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid - 1] <= arr[mid] and arr[mid] >= arr[mid + 1]:
            return mid
        elif arr[mid] < arr[mid + 1]:
            left = mid
        else:
            right = mid


def peak_index_in_mountain_array_2(arr: list[int]) -> int:
    """two pointers approach"""
    p1, p2 = 0, len(arr) - 1
    while p1 < p2:
        if arr[p1] <= arr[p2]:
            p1 += 1
        else:
            p2 -= 1
    return p1
