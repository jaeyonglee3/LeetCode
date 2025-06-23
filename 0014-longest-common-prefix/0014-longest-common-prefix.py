class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        curr_prefix = strs[0]

        for i in range(1, len(strs)):
            curr_str = strs[i]
            
            j = 0
            while j < min(len(curr_prefix), len(curr_str)):
                if curr_prefix[j] != curr_str[j]:
                    break
                j += 1
            
            curr_prefix = curr_prefix[ : j]
        
        return curr_prefix

