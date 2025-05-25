# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            # since the tree is empty, there are no root-to-leaf paths. 
            return False

        def dfs(node, curr_sum) -> bool:
            if not node:
                # the parent node that made the recurisve call on this node was not a leaf
                # thus we don't have a root-to-leaf path, so always return false
                return False
            if not node.left and not node.right:
                # we are at a leaf node
                # return true if the current sum's value plus the leaf node's value adds up to target
                return curr_sum + node.val == targetSum
            
            curr_sum += node.val
            return dfs(node.left, curr_sum) or dfs(node.right, curr_sum)
            
        return dfs(root, 0)
