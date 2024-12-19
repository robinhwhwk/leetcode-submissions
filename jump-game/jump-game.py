class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        steps = nums[0]
        for i in range(1, len(nums)):
            if steps > 0:
                steps -= 1
                steps = max(steps, nums[i])
                if i + steps >= len(nums) - 1:
                    return True
        return False

