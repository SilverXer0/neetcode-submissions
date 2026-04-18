class Solution:
    def maxArea(self, heights: List[int]) -> int:
        length = len(heights) - 1
        res = 0

        left = 0
        right = len(heights) - 1

        while left < right:
            res = max(res, min(heights[left], heights[right]) * length)
            if heights[left] <= heights[right]:
                left += 1
                length -= 1
            else:
                right -= 1
                length -= 1

        return res