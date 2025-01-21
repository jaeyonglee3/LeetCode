class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # This is a cycle detection problem
        # If a cycle is detected in the graph with edges formed by prerequisites, return false
        # A graph contains a cycle iff DFS yields a back edge
        # A back edge is defined as an edge that points to an ancestor of the current node in a DFS traversal.
        
        # First, build the adjacency list representation of the prerequisite graph
        graph = collections.defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)
        
        # Visited stores all the courses 
        def dfs(c, path):
            if c in path:
                return False
            if graph[c] == []:
                return True
            
            path.add(c)
            for course in graph[c]:
                # If the DFS returns false, we can return false early
                if not dfs(course, path):
                    return False
            
            path.remove(c)
            # Optimization: we will mark a course as processed (cycle-free) 
            # by setting its adjacency list to empty and checking this as a base case.
            # This ensures no unnecessary reprocessing of nodes, reducing redundant DFS calls.
            graph[c] = []
            return True
        
        # DFS on every course, looking for cycles
        for course in range(numCourses):
            path = set()
            is_possible = dfs(course, path)
            if not is_possible:
                return False
        
        return True