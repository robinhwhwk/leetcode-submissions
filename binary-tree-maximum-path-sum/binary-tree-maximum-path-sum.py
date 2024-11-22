# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # dp problem
        # dp[node][0]: max path sum not including this node
        # dp[node][1]: max path sum including this node
        # dp[node][1] = dp[node.left][1] + node.val + dp[node.right][1]
        # dp[node][0] = max(dp[node.left][1], dp[node.right][1], dp[node.left][0], dp[node.right][0])
        res = [0]

        def dfs(node):
            if not node:
                return 0
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            include = left + right + node.val
            res[0] = max(res[0], include)
            return node.val + left + right
        dfs(root)
        return res[0]
