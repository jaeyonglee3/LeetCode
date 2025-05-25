# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Use member variable to make it accessible within nested dfs function
        # self.res is accessible and modifiable from inside maxDepth() because it belongs to the class instance, not the function scope.
        self.res = 0

        # Returns the max height between L and R subtrees
        def maxDepth(curr):
            if not curr: return 0

            left = maxDepth(curr.left)
            right = maxDepth(curr.right)
            self.res = max(self.res, left + right)

            # Add 1 for the current node we are at
            return 1 + max(left, right)
        
        maxDepth(root)
        return self.res