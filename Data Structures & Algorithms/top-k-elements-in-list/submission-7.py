import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            d[num] = 1 + d.get(num, 0)
        
        heap = [] # (priority, value)
        for value, priority in d.items():
            heapq.heappush(heap, (priority, value))
            if len(heap) > k:
                heapq.heappop(heap)
       
        res = []
        for priority, value in heap:
            res.append(value)

        return res
