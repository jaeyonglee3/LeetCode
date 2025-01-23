class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # We need to find the smallest k such that koko can eat all bananas
        # What is the search window for k?
        # k is an element of [1, max(piles)]

        # define helper isFeasible, returns bool given proposed k val
        def is_doable(k):
            time_total = 0
            
            for pile in piles:
                if k > pile:
                    time_total += 1
                else:
                    time_total += math.ceil(pile / k)
            
            return time_total <= h
        
        # Now, do a binary search on the window for k
        l, r = 1, max(piles)
        res = 0

        while r >= l:
            curr_k = (l + r) // 2
            
            if is_doable(curr_k):
                r = curr_k - 1
                res = curr_k
            else:
                l = curr_k + 1
        
        return res