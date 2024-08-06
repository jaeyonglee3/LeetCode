class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
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

            
