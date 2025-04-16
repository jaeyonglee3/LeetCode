"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        # maps OG nodes to their clone, helps avoid making multiple clones
        visited = {}

        def dfs(node):
            if node in visited:
                return visited[node]
            
            node_copy = Node(node.val)
            visited[node] = node_copy
            
            for n in node.neighbors:
                n_copy = dfs(n)
                node_copy.neighbors.append(n_copy)
            
            return node_copy
        
        return dfs(node)