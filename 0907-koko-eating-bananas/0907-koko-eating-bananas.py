class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # search window for k: 1 to max(piles)
        # find the slowest values for k such that all can be eaten within h hours

        def isFeasible(k):
            total_hrs = 0
            for pile in piles:
                if k >= pile:
                    total_hrs += 1
                else:
                    total_hrs += math.ceil(pile/k)
            
            return total_hrs <= h
        
        l, r = 1, max(piles)
        res = 0

        while r >= l:
            mid = (l + r) // 2
            print(mid)

            if isFeasible(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return res