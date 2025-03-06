class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # monotonically decreasing stack problem!
        res = [0] * len(temperatures)
        stack = []  # contains (index, temp) pairs

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                removed_i = stack.pop()[0]
                res[removed_i] = i - removed_i
            
            stack.append((i, temp))
        
        return res

