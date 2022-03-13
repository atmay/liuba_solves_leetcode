"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
find two numbers such that they add up to a specific target number. Let these two numbers
be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]

Input: numbers = [2,3,4], target = 6
Output: [1,3]
"""


def two_sum(numbers: list[int], target: int) -> list[int]:
    """Two pointers solution: go from both ends till pointers met"""
    left, right = 0, len(numbers) - 1
    while left < right:
        t = numbers[left] + numbers[right]
        if t == target:
            return [left + 1, right + 1]
        elif t < target:
            left += 1
        else:
            right -= 1


if __name__ == '__main__':
    print(two_sum([2, 3, 4], 6))
    print(two_sum([-1, 0], -1))
    print(two_sum(
        [3, 24, 50, 79, 88, 150, 345], 200))
