class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # at a high level, we want to know all the anagrams of p.
        # then, we'll fix a window of length size(p) and move that window over s.
        # each time the window contains a substring of s which is an anagram of p, result += 1
        # return the result after window slides over entirety of s.

        # brute force - slide a fixed size window over s and run sort(), then compare to sorted(p)
        res = []
        p = sorted(p)
        l, r = 0, len(p) - 1

        while r < len(s):
            curr_str = s[l : r + 1]

            if sorted(curr_str) == p:
                res.append(l)
            
            l += 1
            r += 1
        
        return res