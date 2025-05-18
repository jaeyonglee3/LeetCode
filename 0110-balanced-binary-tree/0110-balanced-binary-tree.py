# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # to be balanced requires that at EVERY node in the tree,
        # the difference in the heights of its left and right subtrees is at most 1

        def dfs(node) -> (bool, int):
            # returns true if balanced, and an int for its height
            if not node:
                return (True, 0)
            
            is_left, height_l = dfs(node.left)
            is_right, height_r = dfs(node.right)

            is_balanced = abs(height_l - height_r) <= 1 and is_left and is_right

            return (is_balanced, 1 + max(height_l, height_r))
        
        return dfs(root)[0]