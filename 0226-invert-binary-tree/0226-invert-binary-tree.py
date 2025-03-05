# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = collections.deque([root])

        while q:
            for _ in range(len(q)):
                curr_node = q.popleft()

                if curr_node:
                    curr_node.left, curr_node.right = curr_node.right, curr_node.left
                    q.append(curr_node.left)
                    q.append(curr_node.right)
        
        return root