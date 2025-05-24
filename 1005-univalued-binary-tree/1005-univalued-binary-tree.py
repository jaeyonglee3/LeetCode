# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(node) -> bool:
            # runs a dfs that visits every node,
            # return true if every node has the same value as the val param
            if not node:
                return True
            if node.val != root.val:
                return False
            
            # still efficient, as python will check left side first
            # so dfs(node.right) runs only if dfs(node.left) returns True
            return dfs(node.left) and dfs(node.right)
        
        return dfs(root)