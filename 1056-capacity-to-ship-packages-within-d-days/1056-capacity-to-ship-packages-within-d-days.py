class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def isPossible(capacity) -> bool:
            curr_load = 0
            days_taken = 1

            for weight in weights:
                if curr_load + weight > capacity: # Then, ship load is at capacity!
                    days_taken += 1
                    curr_load = weight # Start a new load with the current weight
                else:
                    curr_load += weight # Add the weight to the current load
            
            return days_taken <= days
        
        l, r = max(weights), sum(weights)
        res = sum(weights)

        while r >= l:
            mid = (l + r) // 2

            if isPossible(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return res