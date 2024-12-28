class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel_letters = "aeiou"
        l, r = 0, k - 1

        substring = s[l : r + 1]
        res = 0
        for c in substring:
            if c in vowel_letters:
                res += 1

        num_vowels = res
        while r < len(s) - 1:
            # decrement num vowels if left char was a vowel
            if s[l] in vowel_letters:
                num_vowels -= 1
            
            l += 1
            # increment if the new char at right is a vowel
            r += 1
            if s[r] in vowel_letters:
                num_vowels += 1
            
            res = max(res, num_vowels)
        
        return res