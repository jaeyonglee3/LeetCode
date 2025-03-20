# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # BFS solution
        q = collections.deque()

        # queue contains a tuple of node, lower bound, and upper bound
        q.append((root, -math.inf, math.inf))

        while q:
            curr, lower, upper = q.popleft()

            if curr.val <= lower or curr.val >= upper:
                return False
            
            if curr.left:
                q.append((curr.left, lower, curr.val))
            
            if curr.right:
                q.append((curr.right, curr.val, upper))
        
        return True