class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # at a high level, we want to know all the anagrams of p.
        # then, we'll fix a window of length size(p) and move that window over s.
        # each time the window contains a substring of s which is an anagram of p, result += 1
        # return the result after window slides over entirety of s.

        # optimal O(len(s)) solution
        p_count = {}
        for c in p:
            p_count[c] = p_count.get(c, 0) + 1
        
        s_count = {}
        for c in s[0 : len(p)]:
            s_count[c] = s_count.get(c, 0) + 1
        
        l, r = 0, len(p) - 1
        res = []
        
        while r < len(s):
            if s_count == p_count:
                res.append(l)
            
            s_count[s[l]] -= 1
            if s_count[s[l]] == 0:
                del s_count[s[l]]
            
            l += 1
            r += 1
            
            if r < len(s):
                s_count[s[r]] = s_count.get(s[r], 0) + 1
        
        return res
        
