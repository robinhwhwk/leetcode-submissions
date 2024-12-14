class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # check from 0 to amount of coins
        # for each amount, check all the dp[amount - coin]
        # take the minimum + 1
        dp = [float('inf') for _ in range(amount + 1)]
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1