# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def copyTree(root):
            if not root:
                return None
            
            new_root = TreeNode(root.val)
            new_root.left = copyTree(root.left)
            new_root.right = copyTree(root.right)
            
            return new_root
        
        def invertTree(root):
            if not root:
                return None
            
            root.left, root.right = invertTree(root.right), invertTree(root.left)
            return root
        
        def isSameTree(p, q):
            if not p and not q: return True
            if not p or not q: return False
            if p.val != q.val: return False

            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
        
        original_tree = copyTree(root)
        inverted_tree = invertTree(root)
        return isSameTree(original_tree, inverted_tree)