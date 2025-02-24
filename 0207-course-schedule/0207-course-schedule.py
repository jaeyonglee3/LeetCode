class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # step 1: build adjacency list representation of directed graph with
        # vertices 0 -> numCourses - 1 and edges: prerequisites
        graph = collections.defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)
        
        # step 2: detect a cycle - if a cycle is detected, it is
        # not possible to take all of the courses
        def dfs_is_cycle_detected(node, visited):
            if node in visited:
                return False
            if graph[node] == []:
                # The node has no neighbours
                # it is a standalone node and therefore cannot have any cycles
                return True
            
            visited.add(node)
            for n in graph[node]:
                if not dfs_is_cycle_detected(n, visited):
                    return False
            
            visited.remove(node)
            graph[node] = []
            return True
        
        for course in range(numCourses):
            if not dfs_is_cycle_detected(course, set()):
                return False
        
        return True