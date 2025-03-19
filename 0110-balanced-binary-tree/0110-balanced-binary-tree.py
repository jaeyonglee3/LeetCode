# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: 
            return True

        def getHeight(node) -> int:
            if not node:
                return 0
            
            return 1 + max(getHeight(node.left), getHeight(node.right))
        
        return abs(getHeight(root.left) - getHeight(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)