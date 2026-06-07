class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        res = 0
        left = 0
        right = len(height) - 1
        leftmax = height[left]
        rightmax = height[right]

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