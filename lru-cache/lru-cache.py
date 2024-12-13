class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.hashmap = dict()
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.hashmap:
            # update this node to MRU
            node = self.hashmap[key]
            self.remove(node)
            self.add(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            node = self.hashmap[key]
            self.remove(node)
            node.val = value
            self.add(node)
        else:
            if self.size == self.capacity:
                # evict LRU
                lru_node = self.head.next
                self.remove(self.head.next)
                del self.hashmap[lru_node.key]
                self.size -= 1
            node = Node(key, value)
            self.hashmap[key] = node
            self.add(node)
            self.size += 1
        
    # Add a node to the linked list as the MRU.
    def add(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
    
    # Remove a node from the linked list.
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)