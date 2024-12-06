class Solution:
    def myPow(self, x: float, n: int) -> float:
        def dfs(num, exponent):
            if exponent == 0:
                return 1
            if exponent == 1:
                return num
            if exponent % 2 == 0:
                left = dfs(num, exponent // 2)
                return left * left
            else:
                return dfs(num, exponent // 2 + 1) * dfs(num, exponent // 2)

        res = dfs(x, abs(n))
        if n < 0:
            res = 1 / res
        return res
        

