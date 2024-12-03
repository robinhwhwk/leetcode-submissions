class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        counts = dict()
        for num in nums:
            if num not in counts:
                counts[num] = 0
            counts[num] += 1
        total = sum(nums)
        outliers = []
        for num in nums:
            sum_without = total - num
            if sum_without % 2 == 1:
                continue
            target = sum_without // 2
            if num != target and target in counts:
                outliers.append(num)
            elif num == target and target in counts and counts[target] > 1:
                outliers.append(num)

        return max(outliers)