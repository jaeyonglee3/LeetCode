class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # isFeasible(x) helper: can we take nums and split it into k (or fewer) subarrays
        # s.t. the largest sum of those subarrays is <= x? why "or fewer?" if we can split
        # into fewer than k, we know we could easily continue splitting to get to k, and then
        # the largest sum of those subarrays would be even smaller!
        def isFeasible(x) -> bool:
            total = 0
            num_subarrays = 1
            
            for num in nums:
                if total + num <= x:
                    total += num
                else:
                    total = num
                    num_subarrays += 1
            
            return num_subarrays <= k

        # the smallest that the largest sum of any subarray could be
        # is the max(nums) element, since it needs to be part of some subarray
        # the largest that the largest sum of any subarray could be
        # is the sum(nums). technically since we know we need to split nums into k subarrays,
        # there could be a smaller upper bound, but sum(nums) is a definite upper bound.

        # define a search range:
        l, r = max(nums), sum(nums)
        res = r

        while r >= l:
            mid = (l + r) // 2

            if isFeasible(mid):
                # we know that the largest sum of any subarray was <= mid AND we were able to make <= k subarrays.
                # Lets try to make it <= an EVEN smaller value (since we're trying to minimize it) while still
                # making <= k subarrays.
                res = mid
                r = mid - 1
            else:
                # we weren't able to make <= k subarrays such that the largest sum of those subarrays
                # was <= mid. So lets give ourselves more room.
                l = mid + 1
        
        return res
        
        # time: O(n * log(s)) where s = sum(nums) and n is length of nums array
        # space: O(1)