class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # The key insight here is that if there is a cycle in the prerequisite graph, it is 
        # impossible to finish all courses, because a cycle means there is a circular 
        # dependency. Thus, the problem reduces to detecting cycles in a directed graph.
        
        # Step 1: build adjacency list representation of directed graph with
        # vertices: {0 -> numCourses - 1} and edges: {prerequisites}
        graph = collections.defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)
        
        # Step 2: detect a cycle - if a cycle is detected, it is
        # not possible to take all of the courses
        visited = set()
        def dfs_is_cycle_detected(node, path):
            if node in path:
                # Then the node is already in the current recursion path, meaning
                # a cycle exists!
                return False
            if node in visited or graph[node] == []:
                # Either the node has already been process and no cycle was detected
                # or the node has no neighbours, meaning no cycle possible
                return True
            
            path.add(node)
            for n in graph[node]:
                if not dfs_is_cycle_detected(n, path):
                    return False
            
            path.remove(node)  # Backtracking step, required in e.g. like: [[1, 7], [7, 0], [1, 0]]
            visited.add(node)
            return True
        
        for course in range(numCourses):
            if not dfs_is_cycle_detected(course, set()):
                return False
        
        return True

        # time: O(V + E) b/c each node and each edge is visited once
        # space: O(V + E) b/c visited and path sets are O(V) and adjacency list is O(E)