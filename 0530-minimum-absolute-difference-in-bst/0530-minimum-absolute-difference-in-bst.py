# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prev = None
        self.res = float('inf')

        def inOrder(node):
            if not node:
                return
            
            # handle left
            inOrder(node.left)

            # handle curr node
            if self.prev is not None:
                self.res = min(self.res, abs(self.prev - node.val))
            self.prev = node.val
            
            # handle right
            inOrder(node.right)
        
        inOrder(root)
        return self.res
