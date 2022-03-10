"""
Given a string s, reverse the order of characters in each word within a sentence
while still preserving whitespace and initial word order.

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
"""


def reverse_words(s: str) -> str:
    """Since strings in Python are immutable, I decided to use lists and slicing"""
    s = s.split()
    for i in range(len(s)):
        s[i] = s[i][::-1]
    return " ".join(s)


def reverse_words_2(s: str) -> str:
    """Let's modify previous solution using list comprehension"""
    words = [w[::-1] for w in s.split()]
    return " ".join(words)
