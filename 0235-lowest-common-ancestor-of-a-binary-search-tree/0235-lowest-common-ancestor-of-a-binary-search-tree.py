# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > root.val and q.val > root.val:
            # then, LCA must be on the right subtree of root
            return self.lowestCommonAncestor(root.right, p, q)
        elif p.val < root.val and q.val < root.val:
            # then, LCA must be on the left subtree of root
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            # we've found the LCA to be root as one of p or q is greater,
            # and one is lesser, than the root value.
            return root