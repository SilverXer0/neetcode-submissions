class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        num_set = set(nums)
        for num in nums:
            if num - 1 in num_set:
                continue
            length = 1
            while num + length in num_set:
                length += 1
            res = max(res, length)

        return res