class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # (priority, value) -> (num, index)

        heap = []
        res = []
        for i, a in enumerate(nums):
            heapq.heappush_max(heap, (a, i))
            if i < k - 1:
                continue
            while heap[0][1] < i - k + 1:
                heapq.heappop_max(heap)
            res.append(heap[0][0])

        return res
