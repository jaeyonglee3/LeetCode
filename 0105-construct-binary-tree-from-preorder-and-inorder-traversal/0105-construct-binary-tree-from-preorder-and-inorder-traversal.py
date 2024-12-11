# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        
        root_val = preorder[0]

        left_inorder = inorder[0 : inorder.index(root_val)]
        right_inorder = inorder[inorder.index(root_val) + 1 : ]
        
        left_preorder = preorder[1 : len(left_inorder) + 1]
        right_preorder = preorder[len(left_inorder) + 1: ]

        return TreeNode(val=root_val, left=self.buildTree(left_preorder, left_inorder), right=self.buildTree(right_preorder, right_inorder))

