class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            d[num] = 1 + d.get(num, 0)

        temp = []
        for key, v in d.items():
            temp.append((key, v))
        temp = sorted(temp, key = lambda x: x[1], reverse = True)

        res = []
        for i in range(k):
            res.append(temp[i][0])

        return res