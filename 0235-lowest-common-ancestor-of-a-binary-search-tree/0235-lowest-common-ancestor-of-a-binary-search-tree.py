# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # key insight: the LCA is always the node that has p as part of one of its subtrees,
        # and q as part of its other subtree.
        # the LCA could also be either p or q themselves if no such node as described above exists

        # assumptions + clarifications
        # - all node values ARE in fact unique
        # - p and q will be different nodes
        # - p and q will exist in the BST

        # intuition
        # - we can run a DFS that follows one path down the tree. 
        # Since we have a BST, we can easily check if the current
        # node satisfies the key insight condition.

        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root
        
        # time: O(h) where h is the height of the tree.
        # Unlike a general tree traversal (which takes O(N) because it visits every node), 
        # this algorithm only follows one path down the tree. Since the BST property allows us 
        # to decide at each step whether to go left or right, we prune half the tree at each recursive call.
        
        # space: O(h) where h is the height of the tree, usually logn (balanced) or n worst case (skewed)