class Solution:
    def maxDepth(self, s: str) -> int:
        counter = 0
        highest = 0

        for c in s:
            if c == '(':
                counter += 1
            elif c == ")":
                counter -= 1
            
            if counter > highest:
                highest = counter
        
        return highest