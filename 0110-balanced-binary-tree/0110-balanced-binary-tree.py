# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # optimal "bottom up" approach. start from the leaf nodes

        # returns bool for whether node is balanced, and int height
        def dfs(node) -> (bool, int):
            if not node:
                return (True, 0)
            
            left, right = dfs(node.left), dfs(node.right)
            # if we find even a single unbalanced subtree, the entire tree is unbalanced
            is_balanced = abs(left[1] - right[1]) <= 1 and left[0] and right[0]

            return (is_balanced, 1 + max(left[1], right[1]))
        
        return dfs(root)[0]

        # time: O(n) since each node is visited once
        # space: O(n) worst case with a skewed tree, O(logn) best case with a balanced tree (recursive stack)
