class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Using two hashmaps
        # one mapping chars in S to chars in T
        # the other mapping chars in T to chars in S
        
        mapST, mapTS = {}, {}

        for c1, c2 in zip(s, t):
            if ((c1 in mapST and mapST[c1] != c2) or (c2 in mapTS and mapTS[c2] != c1)):
                return False
            else:
                mapST[c1] = c2
                mapTS[c2] = c1
        
        return True

