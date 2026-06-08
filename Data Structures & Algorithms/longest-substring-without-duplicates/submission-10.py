class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        t = {}
        l = 0
        res = 0
        for r in range(len(s)):
            if s[r] in t:
                l = max(l, t[s[r]] + 1)
            t[s[r]] = r
            res = max(res, r - l + 1)
        return res
