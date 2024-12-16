class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        locations = dict()
        result = nums.copy()
        for i in range(len(nums)):
            if nums[i] not in locations:
                locations[nums[i]] = []
            locations[nums[i]].append(i)
        heapq.heapify(nums)
        
        for j in range(k):
            min_element = heapq.heappop(nums)
            min_location = heapq.heappop(locations[min_element])
            new_element = multiplier * min_element
            if new_element not in locations:
                locations[new_element] = []
            heapq.heappush(locations[new_element], min_location)
            heapq.heappush(nums, new_element)
            result[min_location] = new_element
        return result
