class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # use a hashmap where the keys are the words sorted alphabetically
        # and the values are all the anagrams of that word.
        anagrams = {}

        for word in strs:
            sorted_word = ''.join(sorted(word))

            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]
            
        # need to return a nested list of all the anagrams grouped together
        return list(anagrams.values())