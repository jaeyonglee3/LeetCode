from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        q = collections.deque([node])
        visited = {}
        
        # You add the starting node to visited so that: 
        # Its clone is ready before processing neighbors. 
        # You avoid extra logic to handle the "first node" case separately.
        visited[node] = Node(node.val)
        
        while q:
            curr = q.popleft()

            for n in curr.neighbors:
                if n not in visited:
                    visited[n] = Node(n.val)
                    q.append(n)
                
                visited[curr].neighbors.append(visited[n])
        
        return visited[node]