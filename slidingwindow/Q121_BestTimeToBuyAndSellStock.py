from typing import List


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        # will len(prices) < 2?
        min_price = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            profit = prices[i] - min_price
            max_profit = max(max_profit, profit)
            min_price = min(min_price, prices[i])
        return max_profit

    def maxProfit_right_to_left(self, prices: List[int]) -> int:
        # will len(prices) < 2?
        max_price = prices[len(prices) - 1]
        max_profit = 0
        for i in range(len(prices) - 2, -1, -1):
            profit =  max_price - prices[i]
            max_profit = max(max_profit, profit)
            max_price = max(max_price, prices[i])
        return max_profit
