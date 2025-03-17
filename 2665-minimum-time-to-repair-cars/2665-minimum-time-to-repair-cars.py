class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        # ranks are the mechanic's ranks. minutes = rank * n^2, where n = num of cars
        # or rearranged, num of cars = sqrt(mins / rank) rounded down to nearest whole num
        # This means that mechanics with lower ranks (smaller r) are faster at repairing 
        # cars than those with higher ranks for the same number of cars.
        # we have a fixed number of cars to fix.
        # want to find: the minimum time needed to repair all the cars.

        # Assumptions: a single mechanic can work on one car at a time, Each mechanic 
        # can repair as many cars as needed, limited only by the total number of cars

        # ranks = [4,2,3,1], cars = 10
        # 10 minutes
        # [1, 2, 1, 3]

        def isFeasible(x) -> bool:
            # each mechanic can fix math.floor(math.sqrt(x / rank)) cars
            num_cars = 0
            
            for rank in ranks:
                num_cars += int(math.sqrt(x / rank))
            
            return num_cars >= cars
        
        # define a search range of x values to try
        l, r = min(ranks), int(max(ranks) * math.pow(cars, 2))
        res = 0

        while r >= l:
            mid = (l + r) // 2

            if isFeasible(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return res

