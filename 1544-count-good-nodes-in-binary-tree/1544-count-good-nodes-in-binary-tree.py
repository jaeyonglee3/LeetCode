# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        q = deque()

        # Track the maximum value (max_val) seen along the path from the root to the current node.
        q.append((root, -math.inf))
        
        while q:
            node, max_val = q.popleft()

            if node.val >= max_val:
                res += 1
            
            # when you append a left or right subtree to the queue, you always have the node
            # itself as reference, so you can easily check the max value seen along the path
            # from the root to current node.
            if node.left:    
                q.append((node.left, max(max_val, node.val)))
            
            if node.right:
                q.append((node.right, max(max_val, node.val)))
                
        return res

        # time: O(n), we visit each node exactly once, , we perform O(1) 
        # operations (checking the value, updating max_val, and adding children to the queue).
        
        # space: O(n)
        # Queue holds at most one level at a time, which is O(N/2) = O(N) 
        # in the worst case (for a full binary tree).
