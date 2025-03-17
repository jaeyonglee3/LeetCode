class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        # m bouqets with k flowers in each
        # flowers must be adjacent in the bloomDay array
        # want to find: the min num of days we need to make m bouqets

        # [1,10,3,10,2]
        # need 3 bouqets with 1 flower in each of them
        # 3 days
        def isFeasible(num_days) -> bool:
            num_flowers, num_bouquets = 0, 0
            
            for day in bloomDay:
                if day <= num_days:
                    num_flowers += 1
                else:
                    num_flowers = 0
                
                if num_flowers == k:
                    num_bouquets += 1
                    num_flowers = 0
            
            return num_bouquets >= m
        
        l, r = min(bloomDay), max(bloomDay)
        res = -1
        while r >= l:
            mid = (l + r) // 2

            if isFeasible(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return res
