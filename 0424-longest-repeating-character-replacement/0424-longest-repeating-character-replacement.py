class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # paraphrase and notes
        # use var length sliding window appraoch
        # for any substring our window creates, the number of character replacements we need to do
        # is equal to the total number of non-most-frequent characters in the substring
        # we can calculate this by taking size of substring MINUS frequency of most-frequent character

        # maintain a count dictionary containing the count of each char in the substring
        # also maintain a separate variable that tracks the most frequent character so we can access it quick

        # if the substring requires more than k replacements, 
        # move up the left pointer until we need <= k replacements

        # dry rums (examples)
        # Input: s = "ABAB", k = 2
        # res = 4
        # count = {A : 2, B : 2}
        # most freq = A
        # substring = A,B,A,B

        # Input: s = "AABABBA", k = 1
        # res = 4
        # count = {A : 2, B : 3}
        # most freq = B
        # substring = BABBA

        res = 1
        l = 0
        count = {s[l] : 1}
        most_freq = s[l]

        for r in range(1, len(s)):
            count[s[r]] = count.get(s[r], 0) + 1

            if count[s[r]] > count[most_freq]:
                # we have a new most frequent character
                most_freq = s[r]
            
            num_char_replacements = (r - l + 1) - count[most_freq]

            if num_char_replacements > k:
                # increment the left ptr once and continue with the loop
                # we dont increment until num_char_replacements is <= k all at once
                # because the loop needs to go back to the top incase we have a new most_freq char
                count[s[l]] -= 1
                # so by doing this, we effectively shift the window up by exactly 1
                # without changing the windows size/length
                l += 1
            else:
                # only update the result if we have a valid subarray
                res = max(res, r - l + 1)
        
        return res