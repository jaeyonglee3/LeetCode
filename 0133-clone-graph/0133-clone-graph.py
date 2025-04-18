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
        
        # maps OG node to the clone that's been created
        visited = {}

        def dfs(node) -> Node:
            if node in visited:
                return visited[node]
            
            visited[node] = Node(node.val)
            for neighbor in node.neighbors:
                neighbor_copy = dfs(neighbor)
                visited[node].neighbors.append(neighbor_copy)
            
            return visited[node]
        
        return dfs(node)