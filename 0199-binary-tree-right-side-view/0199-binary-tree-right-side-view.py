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
            rightmost = None

            for _ in range(len(q)):
                curr = q.popleft()

                if curr:
                    rightmost = curr.val
                    q.append(curr.left)
                    q.append(curr.right)
            
            if rightmost != None:
                res.append(rightmost)
        
        return res