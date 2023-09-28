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

        while q:  # continue iterating until queue is empty
            q_len = len(q)  # we'll iterate through each value at each level
            level = []
            for i in range(q_len):
                node = q.popleft()
                if node:  # could be None, so ensure they are not before adding to level list
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            
            if level:
                res.append(level)
        
        return res