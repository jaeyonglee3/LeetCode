class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # at a high level, we want to know all the anagrams of p.
        # then, we'll fix a window of length size(p) and move that window over s.
        # each time the window contains a substring of s which is an anagram of p, result += 1
        # return the result after window slides over entirety of s.

        # optimal O(len(s)) solution

        # edge case: if p is longer than s, s cannot contain anagrams of p
        if len(p) > len(s): return []

        # construct 2 hashmaps. one has count of each char in p
        # s_count will always have the count of each char in the current window
        p_count = {}
        s_count = {}
        for i in range(len(p)):
            p_count[p[i]] = p_count.get(p[i], 0) + 1
            s_count[s[i]] = s_count.get(s[i], 0) + 1
        
        # now, start the fixed size sliding window
        l, r = 0, len(p) - 1
        res = []
        
        while r < len(s):
            if s_count == p_count:
                # the hasmaps match, meaning the current substring of s is an anagram of p
                res.append(l)
            
            # when you shift the window, no need to recalculate s_count from scratch
            # just remove the old s[l], and add the new s[r] chars respectively from the count
            s_count[s[l]] -= 1
            if s_count[s[l]] == 0:
                del s_count[s[l]]
            
            l += 1
            r += 1
            
            if r < len(s):
                s_count[s[r]] = s_count.get(s[r], 0) + 1
        
        return res
        
