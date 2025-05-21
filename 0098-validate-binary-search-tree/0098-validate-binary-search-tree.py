# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, upper_bound, lower_bound) -> bool:
            if not node:
                return True
            
            # node must be greater than its lower bound, lesser than its upper bound.
            if node.val > lower_bound and node.val < upper_bound:
                return dfs(node.left, node.val, lower_bound) and dfs(node.right, upper_bound, node.val)
            
            return False
        
        return dfs(root, math.inf, -math.inf)