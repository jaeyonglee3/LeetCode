class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search approach
        def feasible(speed: int) -> bool:
            hrs = 0
            
            for pile in piles:
                if pile < speed:
                    hrs += 1
                else:
                    hrs += math.ceil(pile/speed)
                
                if hrs > h:
                    return False
            
            return True
        
        # define a search boundary
        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
        