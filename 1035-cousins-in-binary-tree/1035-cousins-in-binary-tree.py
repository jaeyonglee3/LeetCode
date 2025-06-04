# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        # BFS is more appropriate for level/depth related problems
        px, dx = None, None
        py, dy = None, None

        q = collections.deque()
        q.append((root, 0))

        while q and (px == None or py == None):
            curr, curr_depth = q.popleft()

            if curr:
                q.append((curr.left, curr_depth + 1))
                q.append((curr.right, curr_depth + 1))

                if curr.left:
                    if curr.left.val == x:
                        px, dx = curr.val, curr_depth
                    elif curr.left.val == y:
                        py, dy = curr.val, curr_depth
                
                if curr.right:
                    if curr.right.val == x:
                        px, dx = curr.val, curr_depth
                    elif curr.right.val == y:
                        py, dy = curr.val, curr_depth
        
        return dx == dy and px != py