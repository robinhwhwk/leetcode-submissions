class Solution:
    def jump(self, nums: List[int]) -> int:
        # iterate through the array
        # for each i, num,
        #   for j in range(num):
        #       min_jumps[i + j] = min(min_jumps[i + j], min_jumps[i] + 1)
        min_jumps = [float('inf') for _ in range(len(nums))]
        min_jumps[0] = 0
        for i in range(len(nums)):
            num = nums[i]
            for j in range(1, num+1):
                if i + j >= len(nums):
                    break
                min_jumps[i + j] = min(min_jumps[i + j], min_jumps[i] + 1)
        return min_jumps[-1]
            
                