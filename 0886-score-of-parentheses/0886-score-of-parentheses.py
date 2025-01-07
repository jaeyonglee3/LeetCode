class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        score = 0

        for c in s:
            if c == "(":
                stack.append(score)

                # Reset score to 0, because the upcoming 
                # parentheses will define a new sub-score.
                score = 0
            else:
                # This handles both the base case ()
                # and recursive doubling for nested structures
                score = stack.pop() + max(1, score*2)
        
        return score
        
