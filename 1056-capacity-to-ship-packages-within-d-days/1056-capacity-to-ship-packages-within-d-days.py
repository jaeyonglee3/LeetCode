class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def is_feasible(capacity: int) -> bool:
            num_days = 1
            total_weight = 0

            for weight in weights:
                if num_days > days or weight > capacity:
                    return False

                if total_weight + weight <= capacity:
                    total_weight += weight
                else:
                    num_days += 1
                    total_weight = weight
            
            return num_days <= days
        
        # define our search window for possible capacities
        # min could be len(weights) * min(weights), could be feasible if all packages
        # have the same weight as smallest weight
        # max could be num packages * max(weights)
        res = 0
        l, r = 1, max(weights) * len(weights)

        while l <= r:
            mid = (l + r) // 2

            if is_feasible(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return res

