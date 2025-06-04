# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def findParentAndDepth(node, target, depth, parent) -> (int, int):
            # returns a tuple of ints, the first is depth, the second is the val of the parent
            if not node:
                return (None, None)
            if node.val == target:
                return (depth, parent)
            
            left_d, left_p = findParentAndDepth(node.left, target, depth + 1, node)
            if left_d:
                return (left_d, left_p)
            
            return findParentAndDepth(node.right, target, depth + 1, node)

        
        d1, p1 = findParentAndDepth(root, x, 0, None)
        d2, p2 = findParentAndDepth(root, y, 0, None)

        return d1 == d2 and p1 != p2