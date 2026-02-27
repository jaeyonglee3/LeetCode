class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)

            if (x == y):
                continue
            else:
                # stone x destroyed
                heapq.heappush(stones, -1 * (abs(y) - abs(x)))
        
        if len(stones) == 1:
            return heapq.heappop(stones) * -1
        
        return 0
