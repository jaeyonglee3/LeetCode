class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # if two words are anagrams, they'll be the SAME word when their letters are put alphabetically
        # nat, tan -> ant
        # we'll use a hashmap where the key is the word sorted alphabetically
        # all values are arrays containing strings from arr that are the key when sorted alphabetically

        strs_map = {}

        for word in strs:
            word_sorted = "".join(sorted(word))

            if word_sorted in strs_map:
                strs_map[word_sorted].append(word)
            else:
                strs_map[word_sorted] = [word]
        
        # return an array containing all arrays in the map
        return [val for val in strs_map.values()]