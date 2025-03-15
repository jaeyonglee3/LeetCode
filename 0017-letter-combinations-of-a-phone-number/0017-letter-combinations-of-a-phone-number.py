class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        
        res = []
        mappings = {"2" : "abc", "3" : "def", "4" : "ghi", "5" : "jkl", 
                    "6" : "mno", "7" : "pqrs", "8" : "tuv", "9" : "wxyz"}

        def dfs(curr_string, i):
            if i == len(digits):
                res.append("".join(curr_string))
                return
            
            for c in mappings[digits[i]]:
                curr_string.append(c)
                dfs(curr_string, i + 1)
                curr_string.pop()
        
        dfs([], 0)
        return res