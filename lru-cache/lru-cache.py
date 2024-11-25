class ListNode:
    def __init__(self, key=None, val=None, next=None):
        self.key = key
        self.val = val
        self.next = next
class LRUCache:

    def __init__(self, capacity: int):
        self.head = ListNode() # head.next is the LRU
        self.tail = ListNode() # tail.prev is the MRU
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = dict() # key : ListNode()
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key in self.cache:
            # update this as the MRU, 1 before the tail
            target = self.cache[key]
            target.prev.next = target.next
            target.next.prev = target.prev
            self.tail.prev.next = target
            target.prev = self.tail.prev
            target.next = self.tail
            self.tail.prev = target
            return target.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache: # already there, no need to evict
            node = self.cache[key]
            node.val = value
            node.prev.next = node.next
            node.prev.next.prev = node.prev
            self.tail.prev.next = node
            node.prev = self.tail.prev
            node.next = self.tail
            self.tail.prev = node
        else: 
            if self.size == self.capacity:
                # at capacity, evict LRU and insert at MRU
                target = self.head.next
                self.head.next = self.head.next.next
                if target.next:
                    self.head.next.prev = self.head
                del self.cache[target.key]
                self.size -= 1
            node = ListNode(key, value)
            self.tail.prev.next = node
            node.prev = self.tail.prev
            self.tail.prev = node
            node.next = self.tail
            self.cache[key] = node
            self.size += 1








# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)