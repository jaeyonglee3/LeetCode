class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # represent as a directed graph with an adjacency 
        # list and run a cycle detection DFS algorithm
        graph = collections.defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)
        
        # visited keeps track of every node we've verified is NOT part of a cycle
        # it allows us to avoid processing the same node multiple times
        visited = set()
        
        def dfs(course, path):
            # course is the current course we are visiting
            # path is the current path we are on
            if course in path:
                return False
            if course in visited:
                return True
            
            # add the current course to the current path
            path.add(course)

            # visit each of the current courses neighbors and call DFS
            for n in graph[course]:
                if not dfs(n, path):
                    return False
            
            # backtracking step
            path.remove(course)
            visited.add(course)

            return True
        
        for course in range(numCourses):
            if not dfs(course, set()):
                return False
        
        return True
