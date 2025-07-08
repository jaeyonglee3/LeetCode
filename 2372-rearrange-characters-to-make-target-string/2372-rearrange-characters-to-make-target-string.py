class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        s_freq = {}
        t_freq = {}

        for c in target:
            t_freq[c] = t_freq.get(c, 0) + 1

        for c in s:
            if c in target:
                s_freq[c] = s_freq.get(c, 0) + 1

        counts = []
        for c in t_freq:
            if c not in s_freq:
                return 0

            counts.append(s_freq[c] // t_freq[c])
        
        return min(counts)
        