class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # sort so we can skip duplicates
        i = 0
        res = []
        while i < len(nums):
            print(i)
            target = -1 * nums[i]
            # do 2sum where nums[j] + nums[k] = target
            complements = dict()
            j = i + 1
            while j < len(nums):
                complement = target - nums[j]

                if complement in complements:
                    res.append([nums[i], nums[j], complement])
                    while j < len(nums) - 1 and nums[j] == nums[j + 1]:
                        j += 1
                complements[nums[j]] = j

                j += 1
            while i < len(nums)-1 and nums[i] == nums[i + 1]:
                i += 1
            i += 1
        return res