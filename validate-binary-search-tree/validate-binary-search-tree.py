# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        max_left = root.val
        min_right = root.val
        def dfs(node, left, right):
            if not node:
                return True
            if node.val <= left or node.val >= right:
                return False
            left = dfs(node.left, left, node.val)
            right = dfs(node.right, node.val, right)
            return left and right
        return dfs(root, float('-inf'), float('inf'))
            