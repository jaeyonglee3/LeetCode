import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.scores = nums

        if not nums:
            return

        # keep the k largest elements out of all elements
        # then, the smallest of those k largest will naturally be the kth largest
        heapq.heapify(self.scores)
        for _ in range(len(self.scores) - k):
            # discard and leave behind only the k largest elements
            heapq.heappop(self.scores)

    def add(self, val: int) -> int:
        if len(self.scores) == self.k:
            heapq.heappushpop(self.scores, val)
        else:
            heapq.heappush(self.scores, val)
        
        return self.scores[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)