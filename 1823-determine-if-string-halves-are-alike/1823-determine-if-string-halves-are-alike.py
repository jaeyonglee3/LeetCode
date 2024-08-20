class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        midpoint = len(s) // 2
        vowels = {'a', 'e', 'i', 'o', 'u'}
        a, b = s[ : midpoint], s[midpoint : ]
        a_vowels, b_vowels = 0, 0

        for i in range(len(a)):
            if a[i].lower() in vowels:
                a_vowels += 1
            if b[i].lower() in vowels:
                b_vowels += 1
        
        return a_vowels == b_vowels