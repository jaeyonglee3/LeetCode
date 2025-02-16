# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val : idx for idx, val in enumerate(inorder)}

        if not preorder or not inorder:
            return
        
        new_node = TreeNode(preorder[0])
        root_i = inorder_map[preorder[0]]

        inorder_left = inorder[ : root_i]
        inorder_right = inorder[root_i + 1 : ]

        preorder_left = preorder[1 : len(inorder_left) + 1]
        preorder_right = preorder[2 + len(inorder_left) - 1 : ]

        new_node.left = self.buildTree(preorder_left, inorder_left)
        new_node.right = self.buildTree(preorder_right, inorder_right)

        return new_node