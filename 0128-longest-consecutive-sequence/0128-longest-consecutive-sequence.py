class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []: return 0
        
        # if n - 1 is not in nums, n is the start of some consecutive sequence
        res = -math.inf
        nums_set = set(nums)

        for n in nums_set:
            if n - 1 not in nums_set:
                curr_len = 1
                curr_seq_val = n

                while curr_seq_val + 1 in nums_set:
                    curr_len += 1
                    curr_seq_val += 1
                
                res = max(res, curr_len)
        
        return res
