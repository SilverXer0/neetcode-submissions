class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0
        c = {}
        for num in nums:
            if num not in c:
                c[num] = 1
            else:
                c[num] += 1

        res = 1
        for num in nums:
            temp = 1
            while num + 1 in c:
                temp += 1
                num += 1
            res = max(res, temp)
        
        return res
