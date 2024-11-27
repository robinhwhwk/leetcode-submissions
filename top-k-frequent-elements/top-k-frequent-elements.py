class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # get frequency of each num
        # sort them into buckets of frequency
        # iterate buckets from the end, stop when we reach k items
        frequency_map = dict()
        for num in nums:
            if num not in frequency_map:
                frequency_map[num] = 0
            frequency_map[num] += 1
        buckets = [[] for _ in range(len(nums) + 1)] # len(nums) + 1 b/c if we have an array of length 5 we want to have frequencies from 0 to 5
        for key in frequency_map:
            frequency = frequency_map[key]
            buckets[frequency].append(key)
        res = [0 for _ in range(k)]
        index = 0
        for frequency in range(len(nums), -1, -1):
            # process each bucket at frequency
            for key in buckets[frequency]:
                res[index] = key
                index += 1
                if index == k:
                    return res
        return res