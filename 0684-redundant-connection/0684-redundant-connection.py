class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        # array to keep track of parents
        par = [i for i in range(N + 1)]  # ith node will map to its parent (1 - n)
        rank = [1] * (N + 1)  # rank is size

        def find(n):
            if n != par[n]:
                # This'll change the parent of each node to be the root node
                par[n] = find(par[n])  # go "up the chain" recursively
            
            return par[n]
        
        def union(n1, n2):
            # This is not a full implementation of union
            # but it gets the job done for what we need right now
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False

            if rank[p1] > rank[p2]:
                # then we want p2 to be a child of p1
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            
            return True  # if n1 and n2 were not already connected
        
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
        