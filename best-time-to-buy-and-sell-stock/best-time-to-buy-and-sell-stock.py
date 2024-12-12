class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = float('inf')
        max_profit = 0
        for price in prices:
            profit = price - buy_price
            max_profit = max(max_profit, profit)
            if price < buy_price:
                buy_price = price
        return max_profit