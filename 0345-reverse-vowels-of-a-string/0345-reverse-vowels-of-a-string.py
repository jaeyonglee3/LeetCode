class Solution:
    def reverseVowels(self, s: str) -> str:
        # Naive solution, quite slow
        # vowels = {'a', 'e', 'i', 'o', 'u'}
        # vowels_in_s = [c for c in s if c.lower() in vowels]
        # new_s = ""

        # for c in s:
        #     new_s += vowels_in_s.pop() if c.lower() in vowels else c
        
        # return new_s

        # ----------------------------------------------
        # Optimized for better runtime with two pointers
        # If left and right are vowels, swap them.
        s = list(s)
        l, r = 0, len(s) - 1
        vowels = set('AEIOUaeiou')

        while l < r:
            while l<r and s[l] not in vowels:
                l += 1
            while l<r and s[r] not in vowels:
                r -= 1
            
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        
        return ''.join(s)
            
