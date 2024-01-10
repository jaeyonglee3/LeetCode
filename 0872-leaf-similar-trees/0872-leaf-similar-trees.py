# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # Do an in-order traversal of both the trees (make nested function)
        # Return just a list of leaf nodes encountered during traversal
        # Check if the two lists are equal

        def dfs(root, leaf: List[int]):
            if not root:  # Empty tree base case
                return
            
            if not root.left and not root.right:
                leaf.append(root.val)
                return
            
            dfs(root.left, leaf)
            dfs(root.right, leaf) 

        leaf1, leaf2 = [], []
        dfs(root1, leaf1)
        dfs(root2, leaf2)

        return leaf1 == leaf2
