class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # heap
        count = dict()
        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1
        priority_queue = [(-prio, label) for label, prio in count.items()]
        heapq.heapify(priority_queue)
        res = []
        for i in range(k):
            top = heapq.heappop(priority_queue)
            res.append(top[1])
        return res