class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_freq = collections.defaultdict(int)
        t_freq = collections.defaultdict(int)

        for c in s:
            s_freq[c] += 1
        
        for c in t:
            t_freq[c] += 1
        
        all_chars = set(s + t)
        res = 0
        for c in all_chars:
            # If s has more of a character than t, the difference represents the excess in s that must be changed.
            # If t has more of a character than s, the difference represents the excess in t that must be changed.
            res += abs(s_freq[c] - t_freq[c])

        # The total res counts every change twice—once from s to t and once from t to s. 
        # Since each change affects both strings at the same time, we divide by 2 to 
        # get the actual number of steps needed.
        return res // 2