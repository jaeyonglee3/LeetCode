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
                curr = q.popleft()

                if curr:
                    curr_lvl.append(curr.val)
                    q.append(curr.left)
                    q.append(curr.right)
            
            if curr_lvl: res.append(curr_lvl)
        
        return res