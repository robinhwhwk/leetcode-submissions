class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        left = 0
        right = k - 1
        count = collections.defaultdict(int) # keep nums count of the current window
        current_max = float('-inf')
        for i in range(left, right + 1):
            if nums[i] not in count:
                count[nums[i]] = 0
            count[nums[i]] += 1
            current_max = max(current_max, nums[i])

        res = [current_max]
        
        while right < len(nums) - 1:
            print(count[nums[left]])
            if nums[left] == current_max and count[nums[left]] == 1:
                current_max = max(nums[left + 1: right + 1])
            # move window
            count[nums[left]] -= 1
            left += 1
            right += 1
            count[nums[right]] += 1
            current_max = max(current_max, nums[right])
            res.append(current_max)
        return res
        
