class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        # try to make s1 into s2
        # an even index can only swap with an even index
        # an odd index can only swap with an odd index

        # To be able to make the two strings equal, 
        # the characters at even and odd positions 
        # in the strings should be the same.

        # We can merge the two parity groups into one frequency array.
        # indices [0...25] are used for characters at even positions
        # indices [26...51] are used for characters at odd positions

        freq = [0] * 52

        for i, (a, b) in enumerate(zip(s1, s2)):
            offset_multiplier = 0 if i % 2 == 0 else 1
            offset = offset_multiplier * 26
            
            freq[ord(a) - 97 + offset] += 1
            freq[ord(b) - 97 + offset] -= 1
        
        return all(c == 0 for c in freq)