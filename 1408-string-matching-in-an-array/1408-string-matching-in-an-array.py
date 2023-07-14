class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        # substrings = set()

        # for word1 in words:
        #     for word2 in words:
        #         if word1 != word2 and word1 in word2:
        #             substrings.add(word1)
        
        # return list(substrings)

        arr = ' '.join(words)
        substrings = [i for i in words if arr.count(i) >= 2]

        return substrings