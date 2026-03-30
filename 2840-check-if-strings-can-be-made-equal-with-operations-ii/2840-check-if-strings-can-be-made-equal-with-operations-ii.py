class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        # try to make s1 into s2
        # an even index can only swap with an even index
        # an odd index can only swap with an odd index

        # To be able to make the two strings equal, 
        # the characters at even and odd positions 
        # in the strings should be the same.

        odds, evens = {}, {}
        for i, c in enumerate(s1):
            if i % 2 == 0:
                evens[c] = evens.get(c, 0) + 1
            else:
                odds[c] = odds.get(c, 0) + 1
        
        for i, c in enumerate(s2):
            if i % 2 == 0:
                if c not in evens: return False
            else:
                if c not in odds: return False
        
        return True