class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # T(i,j) = T(i - 1,j) + T(i, j - 1)
        # base case: 
        # fill the first row and first column with 1s
        # result is in T(m-1,n-1)
        dp = [[1 for _ in range(n)] for _ in range(m)]
        for row in range(1, m):
            for col in range(1, n):
                dp[row][col] = dp[row - 1][col] + dp[row][col - 1]
        return dp[m-1][n-1]
         