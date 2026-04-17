class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1

        m = list(d.items())
        sorted_m = sorted(m, key = lambda x: x[1], reverse=True)

        res = []
        for i in range(k):
            res.append(sorted_m[i][0])

        return res
