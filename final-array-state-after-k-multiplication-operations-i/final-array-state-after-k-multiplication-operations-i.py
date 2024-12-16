class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        locations = dict()
        heap = [(x, i) for i, x in enumerate(nums)]
        heapq.heapify(heap)
        
        for j in range(k):
            x, i = heap[0]
            heapq.heapreplace(heap, (x * multiplier, i))
        for x, i in heap:
            nums[i] = x
        return nums
