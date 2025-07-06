class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # backtracking solution
        res = []

        def dfs(curr_str, num_open, num_close):
            # this helper will run the BT algorithm and populate the result
            # left branch: always add another open parentheses
            # righgt branch: always add another closing parentheses
            # left branch should only occur if num_open < n
            # right branch should only occur if num_open > num_close

            # base case: there are exactly n pairs of open and close parentheses
            if num_open == num_close == n:
                res.append(''.join(curr_str))
                return
            
            curr_str.append('(')
            if num_open < n:
                dfs(curr_str, num_open + 1, num_close)
            
            curr_str.pop()

            if num_open > num_close:
                curr_str.append(')')
                dfs(curr_str, num_open, num_close + 1)
                curr_str.pop()
            
        dfs(['('], 1, 0)
        return res