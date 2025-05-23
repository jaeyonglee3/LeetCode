# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        # return true if nodes with values x and y are cousins
        # we are interested in the depths of nodes w/ vals x and y, as well as their parents
        x_depth, x_parent = self.dfsDepthAndParent(x, root, None, 0)
        y_depth, y_parent = self.dfsDepthAndParent(y, root, None, 0)
        
        return x_depth == y_depth and x_parent != y_parent
    
    def dfsDepthAndParent(self, target, node, parent, depth) -> (Optional[int], Optional[int]):
        # returns a tuple of 2 ints, the first being the depth of the node
        # and the second being the value of the parent of the node
        if not node:
            return (None, None)
        if node.val == target:
            return (depth, parent)
        
        depth_left, parent_left = self.dfsDepthAndParent(target, node.left, node.val, depth + 1)
        if depth_left != None:
            return (depth_left, parent_left)
        
        return self.dfsDepthAndParent(target, node.right, node.val, depth + 1)