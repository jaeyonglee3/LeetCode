class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # You're maintaining a window where the number of zeroes (i.e., flips needed) 
        # is ≤ k. The moment it exceeds k, you move l forward until the condition is satisfied again. 
        # This strategy avoids redundant work and checks only what's necessary, which is the hallmark 
        # of an optimal sliding window solution.
        l, r = 0, 0
        num_flipped = 0
        res = 0

        while r < len(nums):
            if nums[r] == 0:
                num_flipped += 1
            
            while num_flipped > k:
                if nums[l] == 0:
                    num_flipped -= 1
                l += 1
            
            res = max(res, r - l + 1)
            r += 1
        
        return res