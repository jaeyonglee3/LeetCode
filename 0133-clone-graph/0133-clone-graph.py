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
        visited = {}
        visited[node] = Node(node.val)
        
        q = collections.deque()
        q.append(node)

        while q:
            removed = q.popleft()

            for neighbour in removed.neighbors:
                if neighbour not in visited:
                    copy = Node(neighbour.val)
                    visited[neighbour] = copy
                    q.append(neighbour)
                
                visited[removed].neighbors.append(visited[neighbour])
        
        return visited[node]

            
