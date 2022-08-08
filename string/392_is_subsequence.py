# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
#
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none)
# of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is
# a subsequence of "abcde" while "aec" is not).

# Input: s = "abc", t = "ahbgdc"
# Output: true

# Input: s = "axc", t = "ahbgdc"
# Output: false


def is_subsequence(s: str, t: str) -> bool:
    """
    I used s as a queue but instead of removing an element I just added up to the virtual pivot
    """
    pivot = 0
    for i in t:
        if pivot == len(s):
            break
        if i == s[pivot]:
            pivot += 1
    return pivot == len(s)
