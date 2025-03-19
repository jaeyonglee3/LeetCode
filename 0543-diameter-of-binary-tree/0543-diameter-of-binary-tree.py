# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Using self.res allows us to maintain a global state that 
        # is accessible throughout all recursive calls.
        self.res = 0

        # returns the maximum depth of any given node, while also updating the 
        # global result variable at each recursive call, i.e. at each node we visit
        def maxDepth(node) -> int:
            if not node:
                return 0
            
            left = maxDepth(node.left)  # in ex 1, left = 2 for maxDepth(root)
            right = maxDepth(node.right)  # in ex 1, right = 1 for maxDepth(root)

            # step 1: update result! - left + right is the diameter for the node we're currently at
            self.res = max(self.res, left + right)

            # step 2: return the max depth, +1 to include the current node itself
            return 1 + max(left, right)
        
        maxDepth(root)
        return self.res
