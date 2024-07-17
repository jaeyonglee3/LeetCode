# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = collections.deque([root])

        while q:
            right_most = None
            q_len = len(q)

            for i in range(q_len):
                curr = q.popleft()
                if curr:
                    right_most = curr
                    q.append(curr.left)  # these 2 could be null, but that'd be verified next while loop iteration
                    q.append(curr.right)
            
            if right_most:  # verify that rightmost is not null
                res.append(right_most.val)
        
        return res


