# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, lower_bound, upper_bound):  # left and right boundaries for the values of nodes
            # Two Base cases:
            # 1. Empty tree
            # 2. We have a BST property violation

            if not node: # empty tree is still valid BST
                return True
            
            if node.val >= upper_bound or node.val <= lower_bound:
                return False
            
            # check if left subtree is valid, lower bound doesnt change, upper bound is parent
            # check if right subtree is valid, upper bound doesnt change, lower bound is parent
            return valid(node.left, lower_bound, node.val) and valid(node.right, node.val, upper_bound)
        
        return valid(root, -math.inf, math.inf)