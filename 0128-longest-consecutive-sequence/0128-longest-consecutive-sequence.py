class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # given n, if n - 1 is not a member of nums, then n
        # is the start of some sequence of length > 0

        nums_set = set(nums)
        res = 0

        for n in nums_set:
            if n - 1 not in nums_set:
                # n is the start of some sequence of length > 0
                seq_len = 1
                curr_val = n

                while curr_val + 1 in nums_set:
                    seq_len += 1
                    curr_val += 1
                
                res = max(res, seq_len)
            
        return res
