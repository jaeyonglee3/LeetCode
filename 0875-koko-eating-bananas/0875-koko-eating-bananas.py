class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # want to find the smallest k such that we can 
        # finish all bananas under h hours
        # the smallest possible k? - 1
        # the largest possible k? - max(piles)

        res = 0

        def is_valid(k) -> bool:
            time = 0

            for pile in piles:
                if pile < k:
                    time += 1
                    continue
                
                time += math.ceil(pile / k)

            return time <= h

        l, r = 1, max(piles)
        while r >= l:
            candidate = (r + l) // 2

            if is_valid(candidate):
                # this is "good enough"
                # but can we do better by eating slower?
                res = candidate
                r = candidate - 1
            else:
                # otherwise, we need to eat faster
                l = candidate + 1
        
        return res