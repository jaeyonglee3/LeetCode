class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        negatives = [-n for n in nums]
        heapq.heapify(negatives)

        for _ in range(k):
            res = heapq.heappop(negatives)
        
        return -1 * res