class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # isFeasible helper fn returns True if all bananas can be eaten
        # within h hours based on speed k
        def isFeasible(k) -> bool:
            total_hours = 0
            for pile in piles:
                if pile < k:
                    total_hours += 1
                else:
                    total_hours += math.ceil(pile/k)

            return total_hours <= h
        
        res = max_k = max(piles)
        l, r = 1, max_k - 1

        while r >= l:
            mid = (l + r) // 2

            if isFeasible(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return res