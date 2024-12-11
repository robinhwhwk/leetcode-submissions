class Solution:
    def rob(self, nums: List[int]) -> int:
        # T(n) = max(T(n-1), T(n-2) + A[n])
        # base case: T(0) = A[0]
        # T(1) = max(A[0], A[1])
        if len(nums) < 3:
            return max(nums)
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = nums[1]
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[len(nums) - 1]