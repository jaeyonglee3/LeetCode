# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = collections.deque([root])
        res = 0

        while q:
            for _ in range(len(q)):
                curr = q.popleft()

                if curr:
                    q.append(curr.left)
                    q.append(curr.right)
            
            if q: res += 1
        
        return res