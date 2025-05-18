# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        
        def dfs(node, depth):
            if not node: return

            # Each list in res corresponds to a level in the tree.
            # if len(res) == depth is true, we're at a new depth, so add a new list.
            # if the len(res) exceeds depth, the list corresponding to that depth already exists.
            if len(res) == depth:
                res.append([])
            
            res[depth].append(node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)
        return res
