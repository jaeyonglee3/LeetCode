class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # for every point, calculate its distance from the origin
        # store every point in a min-heap that is heapified based on distance from origin
        min_heap = []
        res = []

        for x, y in points:
            dist = math.sqrt((x ** 2) + (y ** 2))
            # heap is heapified using dist since its the first element
            min_heap.append([dist, x, y])
        
        heapq.heapify(min_heap)

        for _ in range(k):
            _, curr_x, curr_y = heapq.heappop(min_heap)
            res.append([curr_x, curr_y])
        
        return res