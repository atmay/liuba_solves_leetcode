# Given two strings s and t, determine if they are isomorphic.
#
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character while preserving the order of
# characters. No two characters may map to the same character, but a character may map to itself.

# Input: s = "egg", t = "add"
# Output: true

# Input: s = "foo", t = "bar"
# Output: false


def is_isomorphic(s: str, t: str) -> bool:
    pattern = dict()
    for i in range(len(s)):
        if s[i] in pattern:
            if pattern[s[i]] != t[i]:
                return False
        else:
            if t[i] in pattern.values():
                return False
            pattern[s[i]] = t[i]
    return True
