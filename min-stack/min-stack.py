class MinStack:

    def __init__(self):
        self.min = float('inf')
        self.stack = []
        self.map = dict()
        self.index = 0

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min = min(self.min, val)
        self.map[self.index] = self.min
        self.index += 1

    def pop(self) -> None:
        self.stack.pop()
        self.index -= 1
        del self.map[self.index] 
        if self.index == 0:
            self.min = float('inf')
        else:
            self.min = self.map[self.index - 1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()