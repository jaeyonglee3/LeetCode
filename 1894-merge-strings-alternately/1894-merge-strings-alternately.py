class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        ptr1, ptr2 = 0, 0
        len1, len2 = len(word1), len(word2)

        while ptr1 < len1 and ptr2 < len2:
            res.append(word1[ptr1])
            res.append(word2[ptr2])
            ptr1 += 1
            ptr2 += 1
        
        res.append(word1[ptr1:])  # Append the remaining part of word1 (if any)
        res.append(word2[ptr2:])  # Append the remaining part of word2 (if any)

        return "".join(res)
