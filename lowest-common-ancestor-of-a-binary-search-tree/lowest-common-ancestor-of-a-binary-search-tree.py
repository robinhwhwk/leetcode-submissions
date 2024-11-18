# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # for each node, check if it has p and q as descendants
        if p.val > q.val:
            p, q = q, p
        def dfs(node, p, q):
            if not node:
                return None
            # in between p and q
            elif node.val == p.val or node.val == q.val:
                return node
            elif node.val > p.val and node.val < q.val:
                return node
            # bigger than both
            elif node.val > q.val:
                return dfs(node.left, p, q)
            # smaller than both
            elif node.val < p.val:
                return dfs(node.right, p, q)
        return dfs(root, p, q)