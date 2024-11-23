class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        

    def findMedian(self) -> float:
        self.arr.sort()
        mid = len(self.arr) // 2
        if len(self.arr) % 2 == 0: # even number of nums
            return (self.arr[mid - 1] + self.arr[mid]) / 2
        else: # odd number of nums
            return self.arr[mid]



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()