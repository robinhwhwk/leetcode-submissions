class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 3 options
        # multiply the current number 
        # take the current number
        # take the negative number
        minSoFar = nums[0]
        maxSoFar = nums[0]
        maxTotal = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            maxSoFar, minSoFar = max(maxSoFar * num, num, minSoFar * num), min(minSoFar * num, num, maxSoFar * num)
            maxTotal = max(maxTotal, maxSoFar)
        return maxTotal
