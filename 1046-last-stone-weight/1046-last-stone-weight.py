class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # we need to be able to efficiently get the two heaviest stones
        # use a max-heap to fetch the heaviest stone in O(1) time
        
        # Step 1: heapify stones using heapq.heapify
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            # "game loop"
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)  # x <= y

            if x != y:
                new_stone = abs(y) - abs(x)
                heapq.heappush(stones, -new_stone)
        
        if len(stones) > 0:
            return abs(stones[0])
        
        return 0
