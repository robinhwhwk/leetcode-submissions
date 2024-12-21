class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # two pointers, 1 at current number and 1 at index to fill
        # move current number every iteration
        # move fill index if current count is less than or equal to 2
        currentCount = 1
        currentNum = nums[0]
        i = 1
        fillIndex = 0
        while i < len(nums):
            if nums[i] == currentNum:
                currentCount += 1
                if currentCount <= 2:
                    fillIndex += 1
            else:
                currentCount = 1
                currentNum = nums[i]
                fillIndex += 1
            nums[fillIndex] = nums[i]
            i += 1
        return fillIndex + 1