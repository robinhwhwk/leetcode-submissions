class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        positions = dict()
        res = [-1 for _ in range(len(nums1))]
        for i in range(len(nums2)):
            positions[nums2[i]] = i
        for i, num in enumerate(nums1):
            j = positions[num]
            for index in range(j + 1, len(nums2)):
                if nums2[index] > num:
                    res[i] = nums2[index]
                    break
        return res