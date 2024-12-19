# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        levels = collections.defaultdict(list)
        queue = deque([(root, 0)])
        minLevel = 0
        maxLevel = 0
        while queue:
            curr, level = queue.popleft()
            minLevel = min(minLevel, level)
            maxLevel = max(maxLevel, level)
            levels[level].append(curr.val)
            if curr.left:
                queue.append((curr.left, level - 1))
            if curr.right:
                queue.append((curr.right, level + 1))
        result = []
        for i in range(minLevel, maxLevel + 1):
            result.append(levels[i])
        return result
