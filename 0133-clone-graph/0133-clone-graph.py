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
        
        # hashmap mapping original nodes to their clones
        visited = {}
        visited[node] = Node(node.val)
        
        # queue only contains OG nodes to be processed
        q = collections.deque([node])

        while q:
            curr = q.popleft()

            for n in curr.neighbors:
                if n not in visited:
                    n_copy = Node(n.val)
                    visited[n] = n_copy
                    q.append(n)
                
                visited[curr].neighbors.append(visited[n])
        
        return visited[node]