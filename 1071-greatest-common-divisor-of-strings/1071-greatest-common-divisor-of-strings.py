class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        x = ""
        gcd = math.gcd(len(str1), len(str2))
        
        for i in range(gcd):
            if str1[i] == str2[i]:
                x += str1[i]
            else:
                return ""
        
        # Check if remainder of larger string is composed of x
        remainder_str1 = str1[gcd : ]
        remainder_str2 = str2[gcd : ]
        if (remainder_str1.count(x) * len(x) != len(remainder_str1) or 
            remainder_str2.count(x) * len(x) != len(remainder_str2)):
            return ""
        else:
            return x