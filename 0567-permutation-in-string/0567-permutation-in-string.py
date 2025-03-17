class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        n = len(s1)
        m = len(s2)
        s1_map = Counter(s1)
        s2_map = Counter()

        for i in range(m):
            s2_map[s2[i]] += 1
            
            if i >= n:
                char_to_rmv = s2[i - n]
                if s2_map[char_to_rmv] > 1:
                    s2_map[char_to_rmv] -= 1                    
                else:
                    del s2_map[char_to_rmv]

            if s1_map == s2_map:
                return True 

        return False