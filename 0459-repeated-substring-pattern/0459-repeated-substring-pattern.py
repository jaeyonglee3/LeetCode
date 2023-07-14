class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        factors = [x for x in range(1, len(s) + 1) if len(s) % x == 0]

        for num in factors:
            sstring = s[:num]
            partial_remainder = s[num:len(sstring) + num]
            
            
            l = [s[(x - num):x] for x in range(num, len(s) + 1, num)]
            
            if all([word == sstring for word in l]) and l != [] and len(l) != 1:
                return True
        
        return False