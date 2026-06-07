class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        
        l = 0
        dupes = set()
        dupes.add(s[l])
        length = 1

        for r in range(1, len(s)):
            while s[r] in dupes:
                dupes.remove(s[l])
                l += 1
            dupes.add(s[r])
            length = max(length, r - l + 1)

        return length