class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l = 0
        for i in range(len(prices)):
            if prices[i] < prices[l]:
                l = i
            else:
                res = max(res, prices[i] - prices[l])

        return res
