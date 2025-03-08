class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        # well formed parentheses have an equal number of openings and closings
        def backtrack(curr, num_open, num_close):
            if num_open == num_close == n:
                res.append("".join(curr))
                return
            
            # left branch, add opening bracket
            if num_open < n:
                curr.append("(")
                backtrack(curr, num_open + 1, num_close)
                curr.pop()

            # right branch, add closing bracket
            if num_close < num_open:
                curr.append(")")
                backtrack(curr, num_open, num_close + 1)
                curr.pop()
        
        backtrack(["("], 1, 0)
        return res

