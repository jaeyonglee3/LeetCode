# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, val) -> bool:
            # runs a dfs that visits every node,
            # return true if every node has the same value as the val param
            if not node:
                return True
            if node.val != val:
                return False
            
            left_res = dfs(node.left, val)
            if not left_res:
                return False
            
            return dfs(node.right, val)
        
        return dfs(root, root.val)
            
