class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # try to identify an upper & lower bound on k
        # and with those, try and find the minimum, valid k value
        # valid meaning with that speed, koko can eat all bananas within h hours
        res = 0

        def is_feasible(k):
            # returns True if koko can eat all bananas within h hours
            # eating at a speed of k. Returns False otherwise.
            hrs_required = 0

            for pile in piles:
                if pile < k:
                    hrs_required += 1
                else:
                    hrs_required += math.ceil(pile / k)
            
            return hrs_required <= h
        
        # the fastest she can go is eating is the entire pile in the hour!
        l, r = 1, max(piles)

        while r >= l:
            mid = (l + r) // 2
            if is_feasible(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return res