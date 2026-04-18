class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tracker = {}
        res = 0
        left = 0

        for right in range(len(s)):
            if s[right] in tracker:
                left = max(left, tracker[s[right]] + 1)
            tracker[s[right]] = right
            res = max(res, right - left + 1)

        return res


