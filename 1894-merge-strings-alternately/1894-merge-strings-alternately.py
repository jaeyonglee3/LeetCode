class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        smaller_len = min(len(word1), len(word2))

        for i in range(smaller_len):
            res += word1[i] + word2[i]
        
        return res + word1[smaller_len : ] if len(word1) != smaller_len else res + word2[smaller_len : ]