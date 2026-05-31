import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # (priority, value) 
        heap = []
        d = {}
        for num in nums:
            d[num] = 1 + d.get(num, 0)
        
        for value, priority in d.items():
            heapq.heappush(heap, (priority, value))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for value, key in heap:
            res.append(key)

        return res
