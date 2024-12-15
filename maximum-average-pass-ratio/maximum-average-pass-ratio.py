class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # compute the added value for each class
        max_heap = [(-((p+1)/(t+1) - p/t), [p+1,t+1]) for p, t in classes]
        heapq.heapify(max_heap)
        for i in range(extraStudents):
            p, t = heapq.heappop(max_heap)[1]
            added_value = -((p+1)/(t+1) - p/t)
            heapq.heappush(max_heap, (added_value, [p + 1, t + 1]))
        total = 0
        for added_value, (p, t) in max_heap:
            total += (p-1)/(t-1)
        return total / len(classes)


