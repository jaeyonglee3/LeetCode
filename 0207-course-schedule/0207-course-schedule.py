class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # This is a cycle detection problem
        # If a cycle is detected in the graph with edges formed by prerequisites, return false
        # A graph contains a cycle iff DFS yields a back edge
        # A back edge is defined as an edge that points to an ancestor of the current node in a DFS traversal.
        
        # We'll represent the graph with an adjacency list
        graph = collections.defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)
        
        visited = set()
        def dfs(c, path):
            if c in path:
                return False
            if c in visited:
                return True
            
            path.add(c)
            for course in graph[c]:
                if not dfs(course, path):
                    return False
            
            path.remove(c)
            visited.add(c)
            return True
        
        for course in range(numCourses):
            is_possible = dfs(course, set())
            if not is_possible:
                return False
        
        return True