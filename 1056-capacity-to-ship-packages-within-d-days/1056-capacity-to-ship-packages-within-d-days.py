class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # want to find: smallest weight capacity x of the ship s.t. everything
        # can be delivered within the number of days

        # assumptions + clarifications
        # - the ship makes 1 trip per day and each trip, its weight
        # cannot exceed the capacity we set.
        # - "loading in order" means from left to right in weights array

        # weights = [1,2,3,4,5,6,7,8,9,10]
        # days = 5
        # output = 15

        # 1. for a suggested x value, how do we determine its feasibility?
        # helper fn that takes in x. it'll iterate over the packages and use counters
        # to determine how many days it will take to ship everything.
        def isFeasible(x) -> bool:
            days_taken = 1
            curr_load = 0

            for weight in weights:
                if curr_load + weight <= x:
                    curr_load += weight
                else:
                    days_taken += 1  # 'sending' the ship off
                    curr_load = weight
            
            return days_taken <= days


        # 2. how do we suggest the right candidates for x?
        # binary search approach -> define a search range of potential values for x
        # and find the smallest, feasible one
        l, r = max(weights), sum(weights)
        res = 0

        while r >= l:
            mid = (l + r) // 2

            if isFeasible(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return res
