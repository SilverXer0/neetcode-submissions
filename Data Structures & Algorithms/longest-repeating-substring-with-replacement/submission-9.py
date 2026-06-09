class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        t = {}
        l = 0
        res = 0
        maxf = 0
        for r in range(len(s)):
            t[s[r]] = 1 + t.get(s[r], 0)
            maxf = max(maxf, t[s[r]])
            while (r - l + 1) - maxf > k:
                t[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res