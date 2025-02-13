# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = collections.deque()
        q.append(root)

        while q:
            q_len = len(q)
            right_most = None

            for _ in range(q_len):
                curr_node = q.popleft()

                if curr_node:
                    right_most = curr_node
                    q.append(right_most.left)
                    q.append(right_most.right)
            
            if right_most:
                res.append(right_most.val)

        return res