class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # given any number n from nums, how can we identify if it
        # is the start of some sequence?

        # well, if n - 1 is not in nums, then n is the start of
        # some consecutive sequence of length > 0

        if nums == []:
            return 0

        nums_set = set(nums)
        res = 1

        for n in nums_set:
            seq_len = 1

            if n - 1 not in nums_set:
                while n + seq_len in nums_set:
                    seq_len += 1
                
                res = max(res, seq_len)
        
        return res