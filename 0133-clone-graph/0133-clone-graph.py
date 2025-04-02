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
        if not node: return None

        visited = {}  # maps original nodes to their new copy

        def dfs(node):
            if node in visited:
                return visited[node]
            
            copy = Node(node.val)
            visited[node] = copy

            for n in node.neighbors:
                n_copy = dfs(n)
                copy.neighbors.append(n_copy)
            
            return copy
        
        return dfs(node)