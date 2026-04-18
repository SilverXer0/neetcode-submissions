class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_buy = prices[0]

        for price in prices:
            if price - min_buy > max_profit:
                max_profit = price - min_buy
            if price < min_buy:
                min_buy = price
        return max_profit

        