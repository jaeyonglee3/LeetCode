class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == t: return True

        curr = 0

        for c in t:
            if curr == len(s):
                return True

            if c == s[curr]:
                curr += 1
        
        return curr == len(s)

        # Approach with two pointers, not typical two pointer technique
        # s_pointer = 0 
        # t_pointer = 0

        # while s_pointer < len(s) and t_pointer < len(t):
        #     if s[s_pointer] == t[t_pointer]:
        #         s_pointer += 1
        #     t_pointer += 1
        
        # return s_pointer == len(s)