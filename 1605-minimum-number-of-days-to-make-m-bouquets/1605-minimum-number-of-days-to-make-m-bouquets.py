class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        NUM_FLOWERS = len(bloomDay)
        
        def is_feasible(days: int) -> bool:
            bouquets = 0
            flowers = 0

            for bloom_day in bloomDay:
                if bloom_day <= days:
                    flowers += 1
                else:
                    flowers = 0
                
                if flowers == k:
                    bouquets += 1
                    flowers = 0
            
            return bouquets >= m
        
        if NUM_FLOWERS < m * k:
            # we do not have enough flowers
            return -1

        # define a search window
        # its between min/max bloom days because the earliest possible day
        # to make bouquets is when the fastest flower blooms, 
        # and the latest is when the slowest one does.
        l, r = min(bloomDay), max(bloomDay)
        res = -1

        while l <= r:
            mid = (r + l) // 2

            if is_feasible(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return res