class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        arr = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            arr[i] = nums[nums[i]]
        return arr