class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        # want to find: the smallest divisor x such that dividing all
        # numbers by it and summing them all is <= the threshold

        # assumptions:
        # - there always exists such a divisor
        # - we'll always round up (take the math.ceil of divisions)
        # - nums.length <= threshold <= 106

        # example run:
        # [1,2,5,9], threshold = 6
        # using 5: we get 1 + 1 + 1 + 2

        # validating a potential x
        # helper fn: iterate over all the numbers, compute the divisions, and take the sum.
        # if the sum <= the threshold, return true
        def isFeasible(x) -> bool:
            total = 0

            for num in nums:
                total += math.ceil(num / x)
            
            return total <= threshold

        # which x values do we try and how do we end up with the smallest one?
        # binary search approach with an appropriate search range to efficiently find smallest x
        # define a search range: l = min(nums), r = max(nums)
        l, r = 1, max(nums)
        res = 0

        while r >= l:
            mid = (r + l) // 2

            if isFeasible(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return res