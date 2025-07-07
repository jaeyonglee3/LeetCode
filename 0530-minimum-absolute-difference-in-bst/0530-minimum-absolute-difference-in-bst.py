# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prev = None
        self.min_diff = math.inf

        def inOrder(node):
            if not node:
                return
            
            # Traverse left
            inOrder(node.left)

            # Process current node
            if self.prev is not None:
                self.min_diff = min(self.min_diff, node.val - self.prev)
            self.prev = node.val

            # Traverse right
            inOrder(node.right)
        
        inOrder(root)
        return self.min_diff
