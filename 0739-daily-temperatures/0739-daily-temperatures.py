class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # monotonically decreasing stack problem!
        # keep on adding to the stack until what you're about to add
        # is GREATER than whats at the top of the stack!

        stack = [] # (index, temperature)
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                removed = stack.pop()
                res[removed[0]] = i - removed[0]
            
            stack.append((i, temp))
        
        return res