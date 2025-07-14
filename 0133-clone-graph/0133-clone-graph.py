from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # BFS approach
        if not node:
            return None
        
        clone = Node(node.val)
        visited = {node : clone}
        q = collections.deque()  # the queue will only contain the clones
        q.append(node)

        while q:
            curr = q.popleft()

            for n in curr.neighbors:
                if n not in visited:
                    clone = Node(n.val)
                    visited[n] = clone
                    q.append(n)
                
                visited[curr].neighbors.append(visited[n])
        
        return visited[node]