class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        # try to make s1 into s2
        # an even index can only swap with an even index
        # an odd index can only swap with an odd index

        # To be able to make the two strings equal, 
        # the characters at even and odd positions 
        # in the strings should be the same.

        s1_evens, s1_odds = [], []
        for i, c in enumerate(s1):
            if i % 2 == 0:
                s1_evens.append(c)
            else:
                s1_odds.append(c)
        
        s2_evens, s2_odds = [], []
        for i, c in enumerate(s2):
            if i % 2 == 0:
                s2_evens.append(c)
            else:
                s2_odds.append(c)
        
        s1_evens.sort()
        s2_evens.sort()
        s1_odds.sort()
        s2_odds.sort()

        return s1_evens == s2_evens and s1_odds == s2_odds