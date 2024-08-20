class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # if two words are anagrams, they'll be the SAME word when their letters are put alphabetically
        # nat, tan -> ant
        # Use a hashmap where key = alphabetically organized word. Values are arrays of words from strs

        words = {}

        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in words:
                words[sorted_word].append(word)
            else:
                words[sorted_word] = [word]
        
        # To return, must compile a list of all the values from words
        result = list(words.values())
        return result        