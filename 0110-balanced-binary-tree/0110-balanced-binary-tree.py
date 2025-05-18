# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # for a tree to be balanced, EVERY node must have
        # a difference of at most 1 between the heights of their l and r subtrees.
        
        # Its false that any given node n is balanced if its l and r subtrees are also balanced.
        # to determine if the node n itself is balanced, we need the heights of the l and r subtrees

        def dfs(node) -> (bool, int):
            if not node:
                return (True, 0)
            
            l_is_balanced, l_height = dfs(node.left)
            r_is_balanced, r_height = dfs(node.right)
            
            curr_height = max(l_height, r_height) + 1
            curr_is_balanced = abs(l_height - r_height) <= 1 and r_is_balanced and l_is_balanced

            return (curr_is_balanced, curr_height)
        
        return dfs(root)[0]