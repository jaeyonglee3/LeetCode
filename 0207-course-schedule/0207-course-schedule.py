class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Cycle detection problem - if cycle detected, courses cannot all be finished
        # Represent with adjacency list
        courses = defaultdict(list)
        for a, b in prerequisites:
            courses[a].append(b)
        
        # Define a DFS helper that returns a bool based on whether
        # all courses can be taken
        visited = set()  # prevents redundant DFS calls → avoids reprocessing nodes that have already been checked for cycles.
        def dfs(node, path) -> bool:
            if node in path:
                return False  # Cycle detected
            if node in visited:
                return True
            
            path.add(node)
            for n in courses[node]:
                valid = dfs(n, path)
                if not valid:
                    return False
            
            path.remove(node)
            visited.add(node)
            return True
        
        for node in range(numCourses):
            valid = dfs(node, set())
            if not valid:
                return False
        
        return True