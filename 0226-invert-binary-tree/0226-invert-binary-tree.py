# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None

        q = collections.deque([root])
        while q:
            for _ in range(len(q)):
                curr = q.popleft()

                if curr and (curr.left or curr.right):
                    curr.left, curr.right = curr.right, curr.left
                    q.append(curr.left)
                    q.append(curr.right)

        return root
