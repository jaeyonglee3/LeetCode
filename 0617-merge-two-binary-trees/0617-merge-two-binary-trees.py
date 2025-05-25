# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node1, node2) -> Optional[TreeNode]:
            if not node1 and not node2:
                return None
            
            node1_val = 0 if node1 == None else node1.val
            node2_val = 0 if node2 == None else node2.val

            if not node1:
                return TreeNode(node1_val + node2_val, dfs(None, node2.left), dfs(None, node2.right))
            elif not node2:
                return TreeNode(node1_val + node2_val, dfs(node1.left, None), dfs(node1.right, None))
            else:
                return TreeNode(node1_val + node2_val, dfs(node1.left, node2.left), dfs(node1.right, node2.right))
        
        return dfs(root1, root2)
