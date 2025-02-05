class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # monotonically decreasing stack problem!
        res = [0] * len(temperatures)
        stack = []
        
        # Iterate over all the temperatures
        for i, temp in enumerate(temperatures):
            # First, check if what we are about to add
            # is greater than whats at the top of the stack
            while stack and temp > stack[-1][1]:
                index_to_update = stack.pop()[0]
                res[index_to_update] = i - index_to_update
            
            stack.append((i, temp))
        
        return res