class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        s_freq = {}
        t_freq = {}

        # create two frequency maps, one each for s and target
        for c in target:
            t_freq[c] = t_freq.get(c, 0) + 1

        for c in s:
            if c in target:
                s_freq[c] = s_freq.get(c, 0) + 1

        res = 0
        for c in t_freq:
            if c not in s_freq:
                return 0

            # this floor division tells us how many of the target we can create
            # using the number of that char that was found in s
            res = min(res, s_freq[c] // t_freq[c])
        
        # this min value is the result because the limiting factor is the 
        # character we have the *least* of relative to what's needed in target
        return res
        