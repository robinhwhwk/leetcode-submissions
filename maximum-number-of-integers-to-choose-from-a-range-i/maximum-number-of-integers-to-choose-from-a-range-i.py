class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        res = 0
        total_sum = 0
        for i in range(1, n + 1):
            if i in banned:
                continue
            if total_sum + i > maxSum:
                break
            total_sum += i
            res += 1
        return res
