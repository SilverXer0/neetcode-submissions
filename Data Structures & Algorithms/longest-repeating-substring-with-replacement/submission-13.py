class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # length of window - most frequent char <= k
        freq = {}
        most = 0
        left = 0
        res = 0
        for right in range(len(s)):
            freq[s[right]] = 1 + freq.get(s[right], 0)
            most = max(most, freq[s[right]])
            if (right - left + 1) - most > k:
                freq[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)

        return res