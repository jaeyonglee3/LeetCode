# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):  # left and right boundaries for the values of nodes
            # Two Base cases:
            # 1. Empty tree
            # 2. We have a BST property violation

            if not node: # empty tree is still valid BST
                return True
            
            if right <= node.val or left >= node.val:
                return False
            
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)
        
        return valid(root, -math.inf, math.inf)