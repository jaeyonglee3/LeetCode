class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        # Fixed sliding window approach
        s_num = str(num)
        left = 0
        res = 0

        while left + k <= len(s_num):
            sstring = s_num[left: left + k]
            if int(sstring) != 0 and num % int(sstring) == 0:
                res += 1
            
            left += 1
        
        return res

