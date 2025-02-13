# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # iteratively with BFS
        # we will do a level-order traversal and count the number of levels
        res = 0
        q = collections.deque()
        q.append(root)

        while q:
            len_q = len(q)

            for _ in range(len_q):
                curr_node = q.popleft()

                if curr_node:
                    q.append(curr_node.left)
                    q.append(curr_node.right)
            
            res += 1

        return res - 1