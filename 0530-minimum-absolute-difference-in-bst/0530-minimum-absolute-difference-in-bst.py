# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # run an in-order traversal - since its a BST, 
        # it returns the nodes in sorted order

        def inOrderDfs(node) -> list[int]:
            if not node:
                return []
            
            return inOrderDfs(node.left) + [node.val] + inOrderDfs(node.right)
        
        in_order = inOrderDfs(root)
        res = math.inf

        for i in range(len(in_order) - 1):
            res = min(res, abs(in_order[i] - in_order[i + 1]))
        
        return res

