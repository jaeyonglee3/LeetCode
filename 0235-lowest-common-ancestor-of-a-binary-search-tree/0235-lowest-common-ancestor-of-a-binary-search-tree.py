# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_path = self.findPath(root, p)
        q_path = self.findPath(root, q)

        i = 0
        while True:
            if i > len(p_path) - 1 or i > len(q_path) - 1 or p_path[i] != q_path[i]:
                return p_path[i - 1]
            else:
                i += 1
    
    def findPath(self, root, target):
        # return an array of nodes representing the path
        # from root to target node
        if root == target:
            return [root]
        
        if target.val > root.val:
            return [root] + self.findPath(root.right, target)
        else:
            return [root] + self.findPath(root.left, target)