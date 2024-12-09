"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        nodes = dict() # node.val : node
        queue = [node]
        visited = set()
        while queue:
            size = len(queue)
            for i in range(size):
                curr = queue.pop(0)
                if curr.val in visited:
                    continue
                visited.add(curr.val)
                if curr.val not in nodes:
                    node_copy = Node(curr.val)
                    nodes[curr.val] = node_copy
                for nbr in curr.neighbors:
                    if nbr.val in nodes:
                        nodes[curr.val].neighbors.append(nodes[nbr.val])
                    else:
                        nbr_copy = Node(nbr.val)
                        nodes[curr.val].neighbors.append(nbr_copy)
                        nodes[nbr.val] = nbr_copy
                    if nbr.val not in visited:
                        print("adding", nbr.val, "to queue")
                        queue.append(nbr)
        return nodes[node.val]
        
                    

