# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left = 1 + self.minDepth(root.left)
        right = 1 + self.minDepth(root.right)

        if left == 1:
            return right
        elif right == 1:
            return left
        else:
            return min(left, right)