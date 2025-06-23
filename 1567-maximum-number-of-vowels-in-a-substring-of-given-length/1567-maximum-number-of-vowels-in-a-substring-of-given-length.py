class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # fixed sliding window
        l, r = 0, k - 1
        vowels = set('aeiou')
        num_vowels = len([s for s in s[0 : k] if s in vowels])
        res = 0

        while r < len(s):
            res = max(res, num_vowels)
            
            if s[l] in vowels:
                num_vowels -= 1
            
            l += 1
            r += 1

            if r < len(s) and s[r] in vowels:
                num_vowels += 1
        
        return res
