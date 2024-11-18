# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(tree1, tree2):
            if not tree1 and not tree2:
                return True
            elif not tree1 or not tree2:
                return False
            elif tree1.val != tree2.val:
                return False
            left = sameTree(tree1.left, tree2.left)
            right = sameTree(tree1.right, tree2.right)
            return left and right
        def dfs(node, subRoot):
            if sameTree(node, subRoot):
                return True
            if not node:
                return False
            left = dfs(node.left, subRoot)
            right = dfs(node.right, subRoot)
            return left or right
        return dfs(root, subRoot)