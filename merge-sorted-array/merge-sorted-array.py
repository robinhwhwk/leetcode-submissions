class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # move indices 0 ~ m-1 to n ~ m + n - 1
        for i in range(m-1, -1, -1):
            nums1[i + n] = nums1[i]
        # compare indices n ~ m + n - 1 in nums1 to indices 0 ~ n - 1 in nums2
        j, k = n, 0
        index = 0
        while j < m + n and k < n:
            num1 = nums1[j]
            num2 = nums2[k]
            if num1 < num2:
                nums1[index] = num1
                j += 1
            else:
                nums1[index] = num2
                k += 1
            index += 1
        while j < m + n:
            num1 = nums1[j]
            nums1[index] = num1
            index += 1
            j += 1
        while k < n:
            num2 = nums2[k]
            nums1[index] = num2
            index += 1
            k += 1