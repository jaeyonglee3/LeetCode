class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # need a stack that is montonically decreasing

        res = len(temperatures) * [0]
        t_stack = [] # (index, temp)

        # iterate over the temperatures array
        for i, temp in enumerate(temperatures):
            # check if the current temperature is greater
            # than the temp sitting at the top of the stack.
            # if true, we can update the answer in the results arr
            # for the temp for which we've just found a bigger one
            while t_stack and temp > t_stack[-1][1]:
                res[t_stack[-1][0]] = i - t_stack[-1][0]
                t_stack.pop()
            
            t_stack.append((i, temp))
        
        return res