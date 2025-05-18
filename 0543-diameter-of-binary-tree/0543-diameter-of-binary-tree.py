# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        l, r = self.height(root.left), self.height(root.right)
        diameter = l + r

        sub = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
        return max(sub, diameter)
    
    def height(self, node) -> int:
        if not node:
            return 0
        
        return 1 + max(self.height(node.left), self.height(node.right))