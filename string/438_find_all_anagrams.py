# Given two strings s and p, return an array of all the start indices of p's anagrams in s.
# You may return the answer in any order.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.


def find_anagrams(self, s: str, p: str) -> list[int]:
    if len(p) == 0 or len(p) > len(s):
        return []

    p_cnt, s_cnt = {}, {}

    for i in range(len(p)):
        p_cnt[p[i]] = 1 + p_cnt.get(p[i], 0)
        s_cnt[s[i]] = 1 + s_cnt.get(s[i], 0)

    res = [0] if p_cnt == s_cnt else []

    l = 0
    for r in range(len(p), len(s)):
        s_cnt[s[r]] = 1 + s_cnt.get(s[r], 0)
        s_cnt[s[l]] -= 1

        if s_cnt[s[l]] == 0:
            s_cnt.pop(s[l])
        l += 1

        if s_cnt == p_cnt:
            res.append(l)
