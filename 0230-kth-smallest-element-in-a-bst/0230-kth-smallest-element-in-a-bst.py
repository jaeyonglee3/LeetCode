# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # in order traversal naturally visits nodes
        # in order from least to greatest
        def inOrder(root):
            if not root:
                return []
            
            return inOrder(root.left) + [root] + inOrder(root.right)
        
        nodes = inOrder(root)
        return nodes[k - 1].val
