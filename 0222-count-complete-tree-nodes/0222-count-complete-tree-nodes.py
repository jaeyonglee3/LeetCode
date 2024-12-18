# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        l_height = self.findHeight(root.left)
        r_height = self.findHeight(root.right)
        
        if l_height == r_height:
            # It is guaranteed that left subtree is a perfect BT
            # Perfect BT has 2^(height) - 1 nodes
            return int(math.pow(2, l_height)) + self.countNodes(root.right)
        else:
            # It is guaranteed that right subtree is a perfect BT
            # Perfect BT has 2^(height) - 1 nodes
            return int(math.pow(2, r_height)) + self.countNodes(root.left)
        
    
    def findHeight(self, root) -> int:
        height = 0
        while root:
            height += 1
            root = root.left  # Only traverse the left subtree
        return height