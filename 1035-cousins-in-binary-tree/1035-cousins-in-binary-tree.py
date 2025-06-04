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
            node, depth, parent = q.popleft()

            if node.val == x:
                px, dx = parent, depth
            elif node.val == y:
                py, dy = parent, depth

            if node.left:
                q.append((node.left, depth + 1, node))
            if node.right:
                q.append((node.right, depth + 1, node))

        return dx == dy and px != py