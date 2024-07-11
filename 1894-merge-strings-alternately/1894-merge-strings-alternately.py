class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        smaller_len = min(len(word1), len(word2))

        for i in range(smaller_len):
            res += word1[i] + word2[i]
        
        if len(word1) - len(word2) < 0:
            res += word2[len(word1): ]
        elif len(word1) - len(word2) > 0:
            res += word1[len(word2): ]
        
        return res