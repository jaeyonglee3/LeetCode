class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Build the adjacency list representation of the prerequisite graph
        graph = collections.defaultdict(list)
        for crs, pre in prerequisites:
            graph[crs].append(pre)
        
        # Path stores the set of nodes currently in the recursion stack
        result = []
        path, processed = set(), set()
        
        def dfs(c):
            if c in path:
                return False  # Cycle detected
            if c in processed:
                if c not in result:  # Avoid duplicates
                    result.append(c)
                return True
            
            path.add(c)
            for course in graph[c]:
                if not dfs(course):
                    return False
            
            path.remove(c)
            processed.add(c)  # Mark as processed
            result.append(c)  # Add to result in reverse topological order
            return True
        
        # DFS on every course, looking for cycles
        for course in range(numCourses):
            if course not in result:  # Only process unvisited courses
                if not dfs(course):
                    return []  # Cycle detected, return empty list
        
        return result  # Reverse the result to get the correct order
