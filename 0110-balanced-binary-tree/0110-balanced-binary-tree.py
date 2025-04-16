# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # balanced requires left and right subtrees to be balanced
        # and the difference in height for L and R subtrees is at most 1

        def dfs(node) -> (bool, int):
            # returns a bool for whether its balanced, and an int for its height
            if not node:
                return (True, 0)
            
            left_result = dfs(node.left)
            right_result = dfs(node.right)
            is_balanced = left_result[0] and right_result[0] and abs(right_result[1] - left_result[1]) <= 1

            return (is_balanced, 1 + max(left_result[1], right_result[1]))
        
        return dfs(root)[0]
