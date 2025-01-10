class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(str1, str2):
            # returns true if str1 is both a prefix and a suffix
            # of str2, and false otherwise
            pre = str2[ : len(str1)]
            suff = str2[-len(str1) : ]
            print(suff)
            return pre == str1 and suff == str1
        
        # return an int denoting the number of index pairs (i, j)
        # s.t. i < j and isPrefixAndSuffix(words[i], words[j]) is true.
        res = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if isPrefixAndSuffix(words[i], words[j]):
                    res += 1

        return res