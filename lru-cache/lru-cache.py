class Node:
    def __init__(self):
        self.key = None
        self.val = None
        self.next = None
        self.prev = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = dict()

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.add(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            node.val = value
            self.add(node)
        else:
            node = Node()
            node.key = key
            node.val = value
            self.add(node)
            self.cache[key] = node
            self.size += 1
        if self.size > self.capacity:
            lru = self.head.next
            del self.cache[lru.key]
            self.remove(self.head.next)
            self.size -= 1

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def add(self, node):
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)