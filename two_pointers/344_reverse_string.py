"""
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
"""


def reverse_string(s: list[str]) -> None:
    """
    I used two pointers approach and swapped values until left pointer met right pointer
    """
    l, r = 0, len(s) - 1

    while l <= r:
        temp = s[l]
        s[l] = s[r]
        s[r] = temp
        l, r = l + 1, r - 1
