# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = None

    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None: return None
        
        deepest_nodes = self.findDeepestNodes(root)
        if len(deepest_nodes) == 1:
            return deepest_nodes[0]
        
        # need to return the LCA of all deepest nodes
        self.postOrder(root, len(deepest_nodes), deepest_nodes)
        return self.res
    
    def postOrder(self, node, target, deepest_nodes):
        if node is None:
            return 0
        
        # left
        left = self.postOrder(node.left, target, deepest_nodes)
        
        # right
        right = self.postOrder(node.right, target, deepest_nodes)
        
        if left + right == target and self.res == None:
            self.res = node
        
        if node in deepest_nodes:
            return left + right + 1
        return left + right

    def findDeepestNodes(self, root):
        # do a level order traversal
        q = collections.deque([root])
        res = []

        while q:
            q_len = len(q)
            curr_level = []

            for _ in range(q_len):
                curr = q.popleft()

                if curr:
                    curr_level.append(curr)
                    q.append(curr.left)
                    q.append(curr.right)
            
            if curr_level: res.append(curr_level)
        
        return res[-1]