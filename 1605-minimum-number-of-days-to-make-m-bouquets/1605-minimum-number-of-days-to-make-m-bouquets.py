class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        # paraphrase
        # m == num of bouquets needed
        # k == num of adjacent flowers in each bouquet
        # the flower at index i will bloom on the bloomDay[i]-th day
        # WANT TO KNOW - min number of days required to make all m bouquets

        # dry run
        # Input: bloomDay = [1,10,3,10,2], m = 3, k = 1
        # possible range for min days: [1, 10]
        # 1 day: [x, _, _, _, _], we can make 1 bouquet
        # 2 day: [x, _, _, _, x], we can make 2 bouquets
        # 3 day: [x, _, x, _, x], we can make 3 bouquets
        # output -> 3

        # edge case: if len(bloomDay) < m * k, return -1
        # we physically do not have enough flowers, no matter how many days pass

        # Input: bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3
        # possible range for min days: [7, 12]
        # 7 day: [x, x, x, x, _, x, x]
        # 12 day: [x, x, x, x, x, x, x]
        # output -> 12

        # intuition
        # we want to minimize the number of days
        # can we limit the possible answer to a specific range
        # for example, assuming we have enough actual flowers,
        # after max(bloomDay), EVERY flower will have bloomed, meaning it would be possible to make the bouquets
        # so the min number of days is somewhere between [min(bloomDay), max(bloomDay)]
        # to find the actual min number, we can try binary search
            # this works because we have a fixed size and sorted search space
            # if x days makes MORE bouquets than needed, SHRINK the search space to only look at days LESS than x
            # if x days makes LESS bouquets than needed, SHRINK the search space to only look at days GREATER than x
        def num_bouquets(days):
            num_adjacent_bloomed = 0
            res = 0

            for bloom_day in bloomDay:
                if days >= bloom_day:
                    num_adjacent_bloomed += 1
                else:
                    num_adjacent_bloomed = 0
                
                if num_adjacent_bloomed == k:
                    res += 1
                    num_adjacent_bloomed = 0
            
            return res
       
        if len(bloomDay) < m * k: 
            return -1
        
        l, r = min(bloomDay), max(bloomDay)
        res = None

        while r >= l:
            mid = (r + l) // 2

            if num_bouquets(mid) >= m:
                res = mid
                r = mid - 1
            else:
                # num_bouquets(mid) < m
                l = mid + 1
        
        return res

