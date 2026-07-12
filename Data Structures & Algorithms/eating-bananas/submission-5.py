class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = float('inf')
        left = 1
        right = max(piles)

        while left <= right:
            time = 0
            mid = (left + right) // 2
            for pile in piles:
                time += math.ceil(pile / mid)
            if time <= h:
                k = min(k, mid)
                right = mid - 1
            else:
                left = mid + 1
        
        return k
