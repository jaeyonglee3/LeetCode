class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {2 : "abc", 3 : "def", 4 : 'ghi', 5 : "jkl", 6 : "mno", 7 : "pqrs", 8 : "tuv", 9 : "wxyz"}
        res = []

        def dfs(i, curr_combo):
            # Base case
            if i > len(digits) - 1:
                if curr_combo != "": res.append(curr_combo[:]) 
                return

            curr_letters = letters[int(digits[i])]
            for char in curr_letters:
                curr_combo += char
                dfs(i + 1, curr_combo)
                curr_combo = curr_combo[:-1]
        
        dfs(0, "")
        return res
