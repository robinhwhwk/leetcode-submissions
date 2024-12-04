class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # for each price, calculate the current profit.
        # if current profit > 0:
        #   add profit to total profit
        #   set buy price to current price
        # else:
        #   set buy price to current price
        buy_price = prices[0]
        total_profit = 0
        for i in range(1, len(prices)):
            current_price = prices[i]
            if current_price > buy_price:
                total_profit += current_price - buy_price
            buy_price = current_price
        return total_profit