# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = [0]
        res = [0]
        def dfs(node):
            if not node:
                return
            left = dfs(node.left)
            count[0] += 1
            if count[0] == k:
                res[0] = node.val
            right = dfs(node.right)

        dfs(root)
        return res[0]