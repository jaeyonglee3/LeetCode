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
        def inOrder(node) -> list:
            if not node:
                return []
            
            return inOrder(node.left) + [node.val] + inOrder(node.right)
        
        in_order = inOrder(root)
        return in_order[k - 1]
