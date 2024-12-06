class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # brute force: heap and hashmap
        # bucket sort: O(n)
        buckets = [[] for _ in range(len(nums) + 1)] # freq from 0 to len(nums)
        frequency_map = dict()
        for i in range(len(nums)):
            if nums[i] not in frequency_map:
                frequency_map[nums[i]] = 0
            frequency_map[nums[i]] += 1
        for freq, value in frequency_map.items():
            buckets[freq].append(value)
        res = []
        for i in range(len(nums), -1, -1): # scan frequency buckets from backwards
            current_bucket = buckets[i]
            j = 0
            while k > 0 and j < len(buckets[i]):
                res.append(buckets[i][j])
                j += 1
                k -= 1
            if k == 0:
                break
        return res

