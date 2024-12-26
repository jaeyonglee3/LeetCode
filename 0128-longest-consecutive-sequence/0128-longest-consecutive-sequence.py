class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if num - 1 is not in the array, then num is the start of some consecutive sequence
        longest_seq = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                next_num = num + 1
                curr_seq = 1

                while next_num in num_set:
                    curr_seq += 1
                    next_num += 1
                
                longest_seq = max(longest_seq, curr_seq)
        
        return longest_seq
