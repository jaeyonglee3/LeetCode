class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""

        min_len = min(len(word1), len(word2))

        for i in range(0, min_len):
            res += word1[i] + word2[i]
        
        return res + word1[min_len : ] if len(word1) != min_len else res + word2[min_len : ]
        