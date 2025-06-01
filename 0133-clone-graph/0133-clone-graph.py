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
        # with BFS
        if not node:
            return None
        
        q = collections.deque([node])
        visited = {}
        visited[node] = Node(node.val)

        while q:
            curr = q.popleft()
            
            for n in curr.neighbors:
                if n not in visited:
                    visited[n] = Node(n.val)
                    q.append(n)
                
                visited[curr].neighbors.append(visited[n])
        
        return visited[node]
