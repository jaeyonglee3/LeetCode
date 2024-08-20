class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # key: if some number - 1 is not in the list, that number is the start of a consec seq
        greatest_seq = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                curr_num = num + 1
                curr_seq = 1
                while curr_num in num_set:
                    curr_seq += 1
                    curr_num += 1
                greatest_seq = max(curr_seq, greatest_seq)
        
        return greatest_seq
