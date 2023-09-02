class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def feasible(capacity: int) -> bool: 
            days_needed = 1
            weight_so_far = 0

            for box in weights:
                if weight_so_far + box <= capacity:
                    weight_so_far += box
                else:
                    days_needed += 1
                    weight_so_far = box

            return days_needed <= days
        
        # initialize boundary (of capacity) for binary search
        # capacity is at least the heaviest weight (we can't just skip the heaviest box)
        # capacity is at most the sum of all the weights (ship all in 1 day)
        left, right = max(weights), sum(weights)  

        while left < right:
            mid = (left + right) // 2

            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        
        return left