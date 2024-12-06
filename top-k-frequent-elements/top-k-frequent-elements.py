class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # brute force: heap and hashmap
        frequency_map = dict()
        for i in range(len(nums)):
            if nums[i] not in frequency_map:
                frequency_map[nums[i]] = 0
            frequency_map[nums[i]] += 1
        frequency_heap = [(-freq, val) for val, freq in frequency_map.items()]
        heapq.heapify(frequency_heap)
        res = []
        for j in range(k):
            res.append(heapq.heappop(frequency_heap)[1])
        return res