# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # we need to check that every node satisfies the BST condition
        # each node has an upper and lower bound
        
        # the root node has a lower bound of -inf, upper bound of inf
        # root's immediate left child node has an upper bound of root.val, lower bound of -inf
        # and these bounds continue as you go along any tree

        # verify that every node satisfies its upper and lower bound constraints
        def verify_dfs(node, lower, upper) -> bool:
            if not node:
                return True
            
            if node.val <= lower or node.val >= upper:
                return False
            
            return verify_dfs(node.left, lower, node.val) and verify_dfs(node.right, node.val, upper)
        
        return verify_dfs(root, -math.inf, math.inf)