# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque()
        q.append(root)
        res = []

        while q:  # continue until queue is empty
            q_len = len(q)
            curr_level = []

            for _ in range(q_len):
                d = q.popleft()

                if d:
                    q.append(d.left)
                    q.append(d.right)
                    curr_level.append(d.val)
            
            if curr_level:
                res.append(curr_level)
        
        return res
           