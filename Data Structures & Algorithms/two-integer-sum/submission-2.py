class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in d:
                if i < d[complement]:
                    return [i, d[complement]]
                return [d[complement], i]
            d[nums[i]] = i