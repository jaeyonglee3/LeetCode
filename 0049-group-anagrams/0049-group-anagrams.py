class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}
        res = []

        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in hmap:
                hmap[sorted_word].append(word)
            else:
                hmap[sorted_word] = [word]
        
        for key in hmap:
            res.append(hmap[key])
        
        return res


        