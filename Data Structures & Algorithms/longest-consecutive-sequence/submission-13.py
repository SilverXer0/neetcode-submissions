class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        m = 0
        for num in num_set:
            if num + 1 in num_set:
                continue
            l = 0
            while num - l in num_set:
                l += 1
                m = max(m, l)
        return m
