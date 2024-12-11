class Solution:
    def rob(self, nums: List[int]) -> int:
        # house robber 1, but exclude first and last indices then compare
        if len(nums) < 4:
            return max(nums)
        # without first index
        dp = [0 for _ in range(len(nums)-1)]
        dp[0] = nums[1]
        dp[1] = max(nums[1], nums[2])
        for i in range(2, len(nums)-1):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i+1])
        without_first = dp[-1]
        # without last index
        dp = [0 for _ in range(len(nums)-1)]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for j in range(2, len(nums)-1):
            dp[j] = max(dp[j-1], dp[j-2] + nums[j])
        without_last = dp[-1]
        return max(without_first, without_last)