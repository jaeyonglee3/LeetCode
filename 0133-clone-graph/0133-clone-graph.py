from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # DFS approach
        if not node:
            return None
        
        visited = {}
        def dfs(curr_node):
            if curr_node in visited:
                return visited[curr_node]
            
            clone = Node(curr_node.val)
            visited[curr_node] = clone

            for n in curr_node.neighbors:
                clone.neighbors.append(dfs(n))
            
            return clone
        
        return dfs(node)
