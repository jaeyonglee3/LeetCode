class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        # If we place all the balls with at least a gap of x 
        # between any two consecutive balls, x will be the minimum magnetic force.
        # we'll try to place all the balls with at least gaps of x, incrementing x on each
        # success until we cannot place all the balls anymore.
        position.sort()

        def isFeasible(x) -> bool:
            curr_dist = 0
            balls_used = 1
            
            for i in range(1, len(position)):
                if balls_used == m: return True

                curr_dist += position[i] - position[i - 1]
                if curr_dist >= x:
                    balls_used += 1
                    curr_dist = 0
            
            return balls_used == m
        
        # r = the maximum gap possible in the positions array
        l, r =  1, position[-1] - position[0]
        res = 1
        while r >= l:
            mid = (l + r) // 2

            if isFeasible(mid):
                # If we can place all the balls with at least a gap of x between them, then trying 
                # smaller gaps is unnecessary, as it will always be possible to place them w/ a smaller gap.
                res = mid
                l = mid + 1
            else:
                # If we cannot place all the balls with at least a gap of x between them, then trying gaps larger 
                # than x is futile, as it would also be impossible to place the balls with a larger gap.
                r = mid - 1
        
        return res  