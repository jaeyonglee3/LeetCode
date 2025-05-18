# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = collections.deque([root])

        while q:
            curr_lvl = []
            
            for _ in range(len(q)):
                curr_node = q.popleft()

                if curr_node:
                    curr_lvl.append(curr_node.val)
                    q.append(curr_node.left)
                    q.append(curr_node.right)
            
            if curr_lvl: res.append(curr_lvl)
        
        return res