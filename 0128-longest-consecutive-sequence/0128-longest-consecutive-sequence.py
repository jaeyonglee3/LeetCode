class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # key insight: say n in a number from nums
        # if n-1 is not in nums, then n is the start of
        # a consecutive sequence with length > 0

        num_set = set(nums)
        res = 0

        for n in num_set:
            if n - 1 not in num_set:
                # n is the start of a consecutive sequence
                curr_len = 1
                curr = n
                while curr + 1 in num_set:
                    curr_len += 1
                    curr += 1
                res = max(res, curr_len)
        
        return res