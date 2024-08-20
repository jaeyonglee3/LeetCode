class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # key: if some number - 1 is not in the list, that number is the start of a consec seq
        # greatest_seq = 0
        # num_set = set(nums)

        # for num in nums:
        #     if num - 1 not in num_set:
        #         curr_num = num + 1
        #         curr_seq = 1
        #         while curr_num in num_set:
        #             curr_seq += 1
        #             curr_num += 1
        #         greatest_seq = max(curr_seq, greatest_seq)
        
        # return greatest_seq

        curr_greatest_len = 0
        arr_as_set = set(nums)
        
        for num in arr_as_set:
            if num - 1 not in arr_as_set:
                curr_seq_num = num
                seq_len = 1
                while curr_seq_num + 1 in arr_as_set:
                    curr_seq_num += 1
                    seq_len += 1
                
                curr_greatest_len = max(curr_greatest_len, seq_len)
        
        return curr_greatest_len
