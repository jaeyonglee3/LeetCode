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

        for i, node in enumerate(q_path):
            if i > len(p_path) - 1 or p_path[i] != node:
                return p_path[i - 1]
        
        return p_path[len(q_path) - 1]

    
    def findPath(self, root, target):
        if root == target:
            return [root]
        
        if target.val > root.val:
            next_node = root.right
        else:
            next_node = root.left

        return [root] + self.findPath(next_node, target)
