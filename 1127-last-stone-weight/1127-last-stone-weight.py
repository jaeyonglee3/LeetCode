class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # To use python heapq for a max heap
        # make all the values negative
        stones = [-weight for weight in stones]
        heapq.heapify(stones) # this is a O(n) operation

        # Simulate the game as long as there are at least 2
        # stone weight remaining in the max heap
        while len(stones) >= 2:
            # stone y is guaranteed to have weight >= x
            # but we made everything negative so we're guaranteed to have x >= y
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)

            if x != y:
                heapq.heappush(stones, -abs(y - x))
            
            # if stones are equal weights, do nothing!
        
        return abs(stones[0]) if len(stones) > 0 else 0