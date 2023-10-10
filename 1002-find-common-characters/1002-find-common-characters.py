class Solution:
    # def commonChars(self, words: List[str]) -> List[str]:
    #     first_word = words[0]
    #     shared = []

    #     for idx, c in enumerate(first_word):
    #         if all({c in words[i][idx:] for i in range(1, len(words))}):
    #             shared.append(c)
        
    #     return shared

    def commonChars(self, words: List[str]) -> List[str]:
        if len(words) < 2:
            return words
        res = []
        word1 = set(words[0])
        
        for char in word1:
            frequency = min([word.count(char) for word in words])
            res += [char] * frequency
        
        return res


