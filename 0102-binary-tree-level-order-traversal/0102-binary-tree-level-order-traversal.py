# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = collections.deque()
        q.append(root)

        while q:
            q_len = len(q)
            curr_level = []
            
            for _ in range(q_len):
                curr_node = q.popleft()

                if curr_node:
                    curr_level.append(curr_node.val)                    
                    q.append(curr_node.left)
                    q.append(curr_node.right)
            
            if curr_level:
                res.append(curr_level)
        
        return res
