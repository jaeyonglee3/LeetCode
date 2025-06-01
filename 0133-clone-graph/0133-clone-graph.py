from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        visited = {}
        def dfs_clone(node):
            if node in visited:
                return visited[node]
            
            visited[node] = Node(node.val)
            for n in node.neighbors:
                n_clone = dfs_clone(n)
                visited[node].neighbors.append(n_clone)
            
            return visited[node]
        
        return dfs_clone(node)