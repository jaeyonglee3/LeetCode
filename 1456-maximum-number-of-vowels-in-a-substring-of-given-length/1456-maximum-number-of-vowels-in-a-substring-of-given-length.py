class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # Fixed sliding window approach
        vowels = 'aeiou'
        left = 0
        right = left + k
        max_vowels = 0

        while right <= len(s):
            sstring = s[left: right]
            # num_vowels = len([c for c in sstring if c in 'aeiou']) # This leads to TLE
            num_vowels = sum(sstring.count(vowel) for vowel in vowels)
            max_vowels = max(num_vowels, max_vowels)
            left += 1
            right += 1
        
        return max_vowels 