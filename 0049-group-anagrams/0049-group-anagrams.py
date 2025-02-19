class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_map = collections.defaultdict(list)

        for word in strs:
            sorted_word = "".join(sorted(word))
            strs_map[sorted_word].append(word)
        
        return list(strs_map.values())