class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}

        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in hmap:
                hmap[sorted_word].append(word)
            else:
                hmap[sorted_word] = [word]
        
        return list(hmap.values())
        