import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        res = []

        for i, a in enumerate(nums):
            heapq.heappush_max(heap, (a, i))
            if i >= k - 1:
                while i - heap[0][1] >= k:
                    heapq.heappop_max(heap)
                res.append(heap[0][0])
            
        return res