# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        # at any node, the diameter can be computed by summing the depths of its left
        # and right subtrees.

        # returns the maximum depth of any given node, while also updating the 
        # global result variable at each recursive call, i.e. at each node we visit
        def maxDepth(node):
            if not node:
                return 0
            
            left = maxDepth(node.left)
            right = maxDepth(node.right)

            # update the global res variable
            self.res = max(self.res, left + right)

            return 1 + max(left, right)
        
        maxDepth(root)
        return self.res