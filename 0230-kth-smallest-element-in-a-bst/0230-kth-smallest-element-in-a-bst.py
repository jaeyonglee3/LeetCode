# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.result = None
        self.inorder(root)
        return self.result
    
    def inorder(self, node):
        if not node or self.result is not None:  # Optimization hint!
            return

        self.inorder(node.left)

        self.k -= 1
        if self.k == 0:
            self.result = node.val
            return  # Stop traversing once found

        self.inorder(node.right)