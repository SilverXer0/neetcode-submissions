class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        t = {}
        for i in range(len(nums)):
            c = target - nums[i]
            if c in t:
                if t[c] < i:
                    return [t[c], i]
                else:
                    return [i, t[c]]
            t[nums[i]] = i
        