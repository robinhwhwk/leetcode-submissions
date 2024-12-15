"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_copy = dict()
        old_to_copy[None] = None
        curr = head
        while curr:
            old_to_copy[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            copy = old_to_copy[curr]
            next_node = old_to_copy[curr.next]
            random_node = old_to_copy[curr.random]
            copy.next = next_node
            copy.random = random_node
            curr = curr.next
        return old_to_copy[head]