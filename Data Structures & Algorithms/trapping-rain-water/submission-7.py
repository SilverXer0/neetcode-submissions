class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        leftmax = height[0]
        rightmax= height[-1]
        left = 0
        right = len(height) - 1

        while left < right:
            if height[left] < height[right]:
                left += 1
                leftmax = max(height[left], leftmax)
                res += leftmax - height[left]
            else:
                right -= 1
                rightmax = max(height[right], rightmax)
                res += rightmax - height[right]

        return res