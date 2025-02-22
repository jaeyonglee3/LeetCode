class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if num - 1 is not in the array, then num is the start of some consecutive sequence
        
        nums_set = set(nums)
        res = 0

        for num in nums_set:
            if num - 1 not in nums_set:
                # num is the start of some consecutive sequence
                curr, seq = num, 1
                while curr + 1 in nums_set:
                    seq += 1
                    curr += 1
                
                res = max(seq, res)
        
        return res