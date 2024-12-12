class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.hashmap = dict()

    def insert(self, val: int) -> bool:
        if val in self.hashmap:
            return False
        index = len(self.arr)
        self.hashmap[val] = index
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hashmap:
            return False
        index = self.hashmap[val]
        del self.hashmap[val]
        if index != len(self.arr) - 1:
            self.arr[index] = self.arr[-1]
            self.hashmap[self.arr[-1]] = index
        self.arr.pop(-1)
        return True

    def getRandom(self) -> int:
        start, stop = 0, len(self.arr) - 1
        index = random.randint(start, stop)
        return self.arr[index]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()