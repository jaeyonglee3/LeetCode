# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0

        def dfs(node, greatest) -> None:
            if not node:
                return
            
            next_greatest = greatest
            
            if node.val >= greatest:
                self.res += 1
                next_greatest = node.val
            
            dfs(node.left, next_greatest)
            dfs(node.right, next_greatest)
        
        dfs(root, root.val)
        return self.res