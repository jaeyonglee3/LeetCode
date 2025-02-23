class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Start w/ empty result and an random word from the list
        # we can use any word since the prefix must be common
        # among all of the words anyway
        res = ""
        arbitrary_word = strs[0]

        # iterate over every character of our arbitrary word from our list
        for i, c in enumerate(arbitrary_word):
            # compare that character to the char from every
            # other word at the same index
            for word in strs:
                if i == len(word) or word[i] != c:
                    # then, we've found the prefix is no longer common
                    # since it can't get any longer, return what we have
                    return res
            
            # add to the result since loop finished and we can conclude
            # the character is common in that positon with every other word
            res += c

        return res