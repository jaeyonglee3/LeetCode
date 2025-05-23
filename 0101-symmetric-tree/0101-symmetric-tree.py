# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # for any symmetric binary tree, if you invert the tree,
        # you should always end up with the same tree
        root_og = self.copyTree(root)
        root_invert = self.invertTree(root)

        return self.sameTree(root_og, root_invert)

    
    def invertTree(self, node) -> Optional[TreeNode]:
        if not node:
            return None
        
        node.left, node.right = self.invertTree(node.right), self.invertTree(node.left)
        return node
    
    def sameTree(self, p, q) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val == q.val:
            return self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right)
        
        return False
    
    def copyTree(self, node) -> Optional[TreeNode]:
        if not node:
            return None
        
        return TreeNode(node.val, self.copyTree(node.left), self.copyTree(node.right))