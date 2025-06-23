class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = []

        for i, i_char in enumerate(strs[0]):
            for j in range(1, len(strs)):
                curr_str = strs[j]

                if i > len(curr_str) - 1 or curr_str[i] != i_char:
                    return ''.join(res)
            
            res.append(i_char)
        
        return ''.join(res)