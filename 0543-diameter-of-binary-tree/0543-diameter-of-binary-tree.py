# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Diameter may or may not pass through the root!
        # Use member variable to make it accessible within nested dfs function
        self.res = 0

        # Returns the max height between L and R subtrees
        def maxDepth(curr):
            if not curr: return 0

            left = maxDepth(curr.left)
            right = maxDepth(curr.right)
            # result updates every recursive call, thereby considering diameters
            # that pass through every node, not just the root
            # i.e. since the recursion visits every node, 
            # we check all possible paths that could form the tree's diameter.
            self.res = max(self.res, left + right)

            # Add 1 for the current node we are at
            return 1 + max(left, right)
        
        maxDepth(root)
        return self.res