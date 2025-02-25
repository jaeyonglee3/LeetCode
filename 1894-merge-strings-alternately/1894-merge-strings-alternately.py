class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        ptr1, ptr2 = 0, 0

        while ptr1 < len(word1) and ptr2 < len(word2):
            res.append(word1[ptr1])
            res.append(word2[ptr2])

            ptr1 += 1
            ptr2 += 1
        
        if ptr1 != len(word1):
            res.append(word1[ptr1 : ])
        elif ptr2 != len(word2):
            res.append(word2[ptr2 : ])
        
        return "".join(res)