class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def is_feasible(capacity: int) -> bool:
            num_days = 1
            total_weight = 0

            for weight in weights:
                if num_days > days:
                    return False

                if total_weight + weight <= capacity:
                    total_weight += weight
                else:
                    num_days += 1
                    total_weight = weight
            
            return num_days <= days
        
        # define search window
        # min would be max(weights) bc ship should be able to ship >= 1 package
        # max would be sum(weights) bc then we could ship ALL the packages in 1 day
        res = 0
        l, r = max(weights), sum(weights)

        while l <= r:
            mid = (l + r) // 2

            if is_feasible(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return res

