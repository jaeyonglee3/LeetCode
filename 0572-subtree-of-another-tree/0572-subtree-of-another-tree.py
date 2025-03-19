# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(p, q) -> bool:
            if not p and not q:
                return True
            elif not p or not q:
                return False
            else:
                return p.val == q.val and sameTree(p.left, q.left) and sameTree(p.right, q.right)
        
        def dfs(node):
            if not node:
                return False
            if sameTree(node, subRoot):
                return True

            return dfs(node.left) or dfs(node.right)
        
        return dfs(root)

        # time: O(n * m). N is the number of nodes in the root tree. M is the number of nodes in the subRoot tree.
        # In the worst case, we may need to check every node in the root tree (which has N nodes) to see if it 
        # is the root of a subtree that matches subRoot. This is because we traverse all nodes of the root tree 
        # in the dfs function. For each node in root, we may need to check the entire subRoot tree (which has M nodes) 
        # to see if the trees are identical using the sameTree function.

        # space: O(H) (O(log N) for balanced trees, O(N) for skewed trees). Only recursion stack takes extra memory