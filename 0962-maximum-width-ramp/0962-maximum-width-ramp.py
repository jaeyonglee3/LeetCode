class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        # for each number n in nums
        # find the furthest next number m such that m >= n
        # and return the greatest distance among all n, m pairs

        # consider what indices are actually "worth" starting a ramp from
        # if If you have an index $i$ and an index $k$ (where $k > i$) and nums[k] 
        # is greater than nums[i], would you ever need to start a ramp at 
        # $k$ to get the maximum width?

        # so, we only care about a decreasing sequence of ramp starting candidates
        # first, gather all possible ramp starting candidates
        candidates = []  # (index, value) pairs
        res = 0

        for i, n in enumerate(nums):
            if candidates and candidates[-1][1] < n:
                continue
            
            candidates.append((i, n))

        # now, iterate thru nums backwards
        for j in range(len(nums) - 1, -1, -1):
            while candidates and nums[j] >= candidates[-1][1]:
                i, val = candidates.pop()
                res = max(res, j - i)
            
            if candidates == []:
                break
        
        return res