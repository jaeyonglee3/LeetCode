class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        res = 0

        for word in words:
            curr_prefix = word[ : len(pref)]
            if curr_prefix == pref:
                res += 1
        
        return res