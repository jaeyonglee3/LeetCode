# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):  # left and right boundaries for the values of nodes
            if not node:
                return True  # an empty bst is still a bst
            
            if node.val >= right or node.val <= left:
            # if not(node.val < right and node.val > left):  # another way of writing the if statement
                return False  # found a node that 'breaks' the bst (does not respect boundaries)
            
            return (valid(node.left, left, node.val) and valid(node.right, node.val, right))  # ensure right and left subtrees are valid
        
        return valid(root, -math.inf, math.inf)