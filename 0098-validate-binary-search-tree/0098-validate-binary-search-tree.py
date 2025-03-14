# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # the BST property applies recursively throughout the structure of the tree.
        def dfs(node, lower_bound, upper_bound):
            if not node:
                return True
            if node.val >= upper_bound or node.val <= lower_bound:
                return False
            
            return dfs(node.left, lower_bound, node.val) and dfs(node.right, node.val, upper_bound)
        
        return dfs(root, -math.inf, math.inf)