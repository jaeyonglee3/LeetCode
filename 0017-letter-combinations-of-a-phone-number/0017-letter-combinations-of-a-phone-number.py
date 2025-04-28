class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        
        res = []
        mappings = {"2" : "abc", "3" : "def", "4" : "ghi", "5" : "jkl", 
                    "6" : "mno", "7" : "pqrs", "8" : "tuv", "9" : "wxyz"}
        
        def dfs(i, curr):
            if i > len(digits) - 1:
                res.append("".join(curr))
                return
            
            for c in mappings[digits[i]]:
                curr.append(c)
                dfs(i + 1, curr)
                curr.pop()
        
        dfs(0, [])
        return res