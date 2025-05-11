class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # while forming combinations: 
        # of closing parentheses can never exceed the number of opening.
        # number of open parentheses can never exceed n.
        res = []

        def dfs(curr, num_open, num_close):
            if num_open == num_close == n:
                res.append("".join(curr[:]))
                return
            
            if num_open < n:
                curr.append("(")
                dfs(curr, num_open + 1, num_close)
                curr.pop()
            
            if num_close < num_open:
                curr.append(")")
                dfs(curr, num_open, num_close + 1)
                curr.pop()

        dfs(["("], 1, 0)
        return res