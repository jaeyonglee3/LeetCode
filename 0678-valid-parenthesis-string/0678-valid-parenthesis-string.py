class Solution:
    def checkValidString(self, s: str) -> bool:
        opens = []
        stars = []

        for i, c in enumerate(s):
            if c == '(':
                opens.append(i)
            elif c == '*':
                stars.append(i)
            else:
                # we have a closing parentheses
                if not opens and not stars:
                    return False
                
                if opens:
                    opens.pop()
                elif stars:
                    stars.pop()
        
        while opens and stars:
            # if the star comes before the open, return false
            if stars.pop() < opens.pop():
                return False
        
        return len(opens) == 0
            
 