class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # step 1: represent the data in a directed graph using adjacency list
        graph = collections.defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)
        
        # step 2: build a valid course ordering list, or return [] if impossible
        # this is a topological sort
        res = []
        visited = set()

        def dfs(node, path):
            if node in path:
                return False
            if node in visited:
                return True
            
            path.add(node)
            for n in graph[node]:
                if not dfs(n, path):
                    return False
            
            path.remove(node)
            visited.add(node)
            res.append(node)
            return True

        for course in range(numCourses):
            if not dfs(course, set()):
                return []
        
        return res