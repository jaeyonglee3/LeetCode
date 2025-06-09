class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # use a hashmap where the keys are a tuple of 26 integers,
        # representing the count of each letter in the alphabet, used in the word.
        # the values are all the words that have the same letter count tuple as the key.
        anagrams = {}

        for word in strs:
            count = [0] * 26

            for char in word:
                count[ord(char) - ord('a')] += 1
            
            count_tup = tuple(count)
            if count_tup in anagrams:
                anagrams[count_tup].append(word)
            else:
                anagrams[count_tup] = [word]
            
        return list(anagrams.values())