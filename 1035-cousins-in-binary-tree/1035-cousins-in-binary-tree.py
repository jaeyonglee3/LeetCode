# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        # Track parent and depth
        px, dx = None, None
        py, dy = None, None

        q = deque([(root, 0, None)])  # node, depth, parent

        while q and (px is None or py is None):
            curr, depth, parent = q.popleft()

            if curr.val == x:
                px, dx = parent, depth
            if curr.val == y:
                py, dy = parent, depth
            
            if curr.left:
                q.append((curr.left, depth + 1, curr))
            if curr.right:
                q.append((curr.right, depth + 1, curr))
        
        return px != py and dx == dy
