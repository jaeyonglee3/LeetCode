# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque([root])
        res = []
        is_left_to_right = True

        while q:
            curr_lvl = collections.deque()

            for _ in range(len(q)):
                curr = q.popleft()
                
                if curr:
                    q.append(curr.left)
                    q.append(curr.right)

                    if is_left_to_right:
                        curr_lvl.append(curr.val)
                    else:
                        curr_lvl.appendleft(curr.val)
            
            is_left_to_right = not is_left_to_right
            if curr_lvl:
                res.append(list(curr_lvl))
        
        return res
