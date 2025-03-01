# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, greatest):
            if not node:
                return 0
            
            if node.val >= greatest:
                return 1 + dfs(node.left, node.val) + dfs(node.right, node.val)
            else:
                return 0 + dfs(node.left, greatest) + dfs(node.right, greatest)
        
        return 1 + dfs(root.left, root.val) + dfs(root.right, root.val)
