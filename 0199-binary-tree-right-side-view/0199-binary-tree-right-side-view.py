# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node, depth):
            if not node:
                return
            if len(res) == depth:
                res.append(node.val)
            
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0)
        return res

        # time: O(n) since we visit every node
        # space: O(h) for the recursion stack where h is height, so log n if tree balanced, and n if tree is skewed