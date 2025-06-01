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
        # with DFS
        if not node:
            return None
        
        visited = {}
        def dfs(node):
            if node in visited:
                return visited[node]
            
            visited[node] = Node(node.val)

            for n in node.neighbors:
                visited[node].neighbors.append(dfs(n))
            
            return visited[node]
        
        return dfs(node)