# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        # first, convert the tree to an undirected graph represented by an adjacency
        # list - this makes it easier to handle
        graph = collections.defaultdict(set)  # maps values to a set of nodes
        
        def dfs(node):
            if not node:
                return
            
            if node.left:
                graph[node.val].add(node.left.val)
                graph[node.left.val].add(node.val)  # add the reverse edge

            if node.right:
                graph[node.val].add(node.right.val)
                graph[node.right.val].add(node.val)  # add the reverse edge
            
            dfs(node.left)
            dfs(node.right)
        
        # construct the graph with dfs
        dfs(root)
        print(graph)

        # begin a BFS to "infect" the graph
        q = collections.deque()
        q.append(start)
        infected, minutes = set([start]), 0

        while q:
            for _ in range(len(q)):
                curr = q.popleft()

                for n in graph[curr]:
                    if n in infected:
                        continue

                    infected.add(n)
                    q.append(n)

            if q:
                minutes += 1

        return minutes