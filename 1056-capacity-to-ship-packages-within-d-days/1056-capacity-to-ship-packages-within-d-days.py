class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def isPossible(capacity) -> bool:
            curr_load = 0
            curr_package = 0
            days_taken = 0

            print("CAPACITY: ", capacity)
            while curr_package < len(weights):
                while curr_package < len(weights) and curr_load + weights[curr_package] <= capacity:
                    # print(curr_load)
                    # add the weight of the current package to current load
                    print(weights[curr_package])
                    curr_load += weights[curr_package]
                    curr_package += 1
                    # print(curr_package)
                
                # print("")
                curr_load = 0
                days_taken += 1
            
            # print("days taken: ", days_taken)
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