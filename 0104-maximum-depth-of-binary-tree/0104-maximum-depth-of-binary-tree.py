# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # BFS Solution
        res = 0
        q = collections.deque([(root, 1)])

        while q:
            curr, d = q.popleft()

            if curr:
                res = max(res, d)
                q.append((curr.left, d + 1))
                q.append((curr.right, d + 1))
        
        return res