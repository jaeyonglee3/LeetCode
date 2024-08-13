class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # well-formed parentheses have the same number of open + close parentheses
        # also cannot have closing come before opening parentheses
        # You can only add a closing parenthesis if num closing < num opening 

        # This could be more of a backtracking problem...
        res = []
        
        def backtrack(open_n, closed_n, path):
            if open_n == closed_n == n:
                res.append(path)
                return
            

            if open_n < n:
                backtrack(open_n + 1, closed_n, path + "(")
             

            if closed_n < open_n:
                backtrack(open_n, closed_n + 1, path + ")")
                
        backtrack(0, 0, "")
        return res

