# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.right), self.maxDepth(root.left))

        # Iterative sol'n using BFS and Queue
        # if root == None:
        #     return 0

        # level = 0
        # q = deque([root])

        # while q:
        #     for i in range(len(q)):
        #         node = q.popleft()
        #         if node.left != None:
        #             q.append(node.left)
        #         if node.right != None:
        #             q.append(node.right)
            
        #     level += 1
        
        # return level