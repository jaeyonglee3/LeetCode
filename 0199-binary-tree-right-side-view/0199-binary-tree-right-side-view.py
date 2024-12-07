# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Apply level order traversal
        # At each level, add node at end of the array to the final result array

        res = []
        q = collections.deque()
        q.append(root)

        while q:
            q_len = len(q)
            curr_level = []

            for _ in range(q_len):
                d = q.popleft()

                if d:
                    q.append(d.left)
                    q.append(d.right)
                    curr_level.append(d.val)
            
            if curr_level:
                res.append(curr_level.pop())
        
        return res