# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def getMinSwaps(original):
            swaps = 0
            target = original.copy()
            target.sort()
            pos = dict()
            for i in range(len(original)):
                pos[original[i]] = i
            for index in range(len(original)):
                if original[index] != target[index]:
                    swaps += 1
                    target_pos = pos[target[index]]
                    pos[original[index]] = target_pos
                    original[target_pos] = original[index]
            return swaps
            

        queue = collections.deque([root])
        swaps = 0
        while queue:
            size = len(queue)
            level_values = []

            for i in range(size):
                node = queue.popleft()
                level_values.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            swaps += getMinSwaps(level_values)
            
        return swaps
                
