# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # need to do an in-order traversal of the tree in order to visit the nodes
        # in order of least to greatest in value
        self.k = 0
        self.res = None

        def inOrder(node) -> None:
            if not node or self.res is not None:  # Optimization hint!
                return
            
            inOrder(node.left)

            self.k += 1
            if self.k == k:
                self.res = node.val
                return
            
            inOrder(node.right)
        
        inOrder(root)
        return self.res
