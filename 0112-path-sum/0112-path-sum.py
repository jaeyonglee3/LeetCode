# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False

        def dfs(node, curr_sum) -> bool:
            if not node:
                return False
            if not node.left and not node.right:
                # we are at a leaf node
                return curr_sum + node.val == targetSum
            
            curr_sum += node.val
            if dfs(node.left, curr_sum):
                return True
            
            return dfs(node.right, curr_sum)
            
        return dfs(root, 0)
