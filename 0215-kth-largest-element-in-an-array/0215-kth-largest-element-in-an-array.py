class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # create a max heap with all the elements in the array
        # use heapq.heappop until you pop the kth time, and thats the result to return
        max_heap = []

        for n in nums:
            max_heap.append(n * -1)
        
        heapq.heapify(max_heap)

        res = 0
        for _ in range(k):
            res = heapq.heappop(max_heap)
        
        return res * -1