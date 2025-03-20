# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # for any given node, the node has an upper and lower bound
        # visit every node in a DFS. if just one node violates the BST property, return False
        def dfs(node, lower, upper) -> bool:
            if not node:
                return True
            if node.val >= upper or node.val <= lower:
                return False
            
            return dfs(node.left, lower, node.val) and dfs(node.right, node.val, upper)
        
        return dfs(root, -math.inf, math.inf)