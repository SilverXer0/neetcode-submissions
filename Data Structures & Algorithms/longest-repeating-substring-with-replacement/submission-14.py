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
            # we dont' care about the value of most becoming stale
            # after this runs once because the only way to get a substring
            # better than our best res is to get a most greater than the 
            # current one anyway, and most will be updated w a greater 
            # value at the start of the for loop if it eventually exists
            if (right - left + 1) - most > k:
                freq[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)

        return res