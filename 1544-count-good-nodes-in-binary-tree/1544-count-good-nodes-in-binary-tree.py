# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_val) -> int:
            if not node:
                return 0
            
            if node.val < max_val:
                # Run DFS on left, right subtrees.
                # max_value stays the same.
                return 0 + dfs(node.left, max_val) + dfs(node.right, max_val)
            else:
                # Run DFS on left, right subtrees. 
                # New max_value is the value of the curr node.
                return 1 + dfs(node.left, node.val) + dfs(node.right, node.val)
        
        return 1 + dfs(root.left, root.val) + dfs(root.right, root.val)

            
