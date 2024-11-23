from heapq import *

class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        if len(self.small) == len(self.large): # add to large
            heappush(self.large, -heappushpop(self.small, -num))
        else: # large has 1 more element, so add to small
            heappush(self.small, -heappushpop(self.large, num))

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            # 2 medians
            return (-self.small[0] + self.large[0]) / 2
        else:
            return self.large[0]




# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()