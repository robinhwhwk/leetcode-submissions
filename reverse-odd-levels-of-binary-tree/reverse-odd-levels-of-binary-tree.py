# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = [root]
        level = -1
        while queue:
            level += 1
            print(level)
            size = len(queue)
            children = [None for _ in range(size * 2)]
            for i in range((size+1) // 2):
                left = queue[i]
                right = queue[-1 - i]
                if level % 2: 
                    left.val, right.val = right.val, left.val
                    print(left.val, right.val)
                if not left.left:
                    continue
                children[2 * i] = left.left
                children[2 * i + 1] = left.right
                children[-1 -2*i] = right.right
                children[-1 -2*i - 1] = right.left
            if not children[0]:
                return root
            queue = children
            
        return root
