class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Attempt 1: TLE
        # def isAnagram(s1: str, s2: str):
        #     return sorted(s1) == sorted(s2)
        
        # res = []
        # # while strs is not empty
        # # take the word at index 0 and find all its anagrams
        # # take that list and add it to res, removing all words involved
        # # keep going until strs is empty

        # while strs:
        #     curr = strs[0] 
        #     temp = []

        #     for word in strs:
        #         if isAnagram(curr, word):
        #             temp.append(word)
            
        #     for chosen in temp:
        #         strs.remove(chosen)
            
        #     res.append(temp)
        
        # return res

        # Attempt 2: Use Hashmap, sorted words to words
        anagrams = {}

        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]
        
        return [words for words in anagrams.values()]

        