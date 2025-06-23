class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        curr_prefix = strs[0]

        for i in range(1, len(strs)):
            curr_str = strs[i]
            updated = False
            
            for j in range(len(curr_str)):
                if j > len(curr_prefix) - 1:
                    break

                if curr_prefix and curr_str[j] != curr_prefix[j]:
                    updated = True
                    curr_prefix = curr_str[ : j]
                    break
            
            if len(curr_str) < len(curr_prefix) and not updated:
                curr_prefix = curr_str
        
        return curr_prefix

