class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        front = 0
        back = len(nums) - 1
        i = 0
        while i <= back:
            if nums[i] == 0:
                nums[front], nums[i] = nums[i], nums[front]
                front += 1
                if nums[i] == 0:
                    i += 1
            elif nums[i] == 2:
                nums[back], nums[i] = nums[i], nums[back]
                back -= 1
                if nums[i] == 2:
                    i += 1
            else:
                i += 1
        

        