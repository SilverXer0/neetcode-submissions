class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        num_set = set(nums)

        for num in nums:
            length = 1
            if num - 1 in num_set:
                continue
            while num + length in num_set:
                length += 1
            res = max(res, length)

        return res