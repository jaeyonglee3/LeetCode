class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # min heap with k largest integers
        self.k = k
        self.min_heap = nums
        heapq.heapify(self.min_heap)
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)

        # edge case, heap may have been initialized with less than or 
        # equal to k elements
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        
        # 0th index will always store the minimum value
        return self.min_heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)