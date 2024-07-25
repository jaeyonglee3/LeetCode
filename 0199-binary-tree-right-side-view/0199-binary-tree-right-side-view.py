# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque([root])
        res = []

        while q:
            len_q = len(q)
            right_most = None

            for i in range(len_q):
                curr = q.popleft()

                if curr:
                    right_most = curr
                    q.append(curr.left)
                    q.append(curr.right)
            
            if right_most:
                res.append(right_most.val)
        
        return res



