class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tracker = {}
        res = 0
        l = 0

        for r in range(len(s)):
            if s[r] in tracker:
                l = max(l, tracker[s[r]] + 1)
            tracker[s[r]] = r
            res = max(res, r - l + 1)

        return res