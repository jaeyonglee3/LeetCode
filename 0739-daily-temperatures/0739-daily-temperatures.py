class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # monotonically increasing stack application
        answer = [0] * len(temperatures)
        stack = []  # stores temp, index pairs

        for cur_i, cur_temp in enumerate(temperatures):
            # before you add the tuple, check if the cur_temp is greater
            # than the temp at the top of the stack because then, we've found a warmer temp
            # and we need to update the answer array
            while stack and cur_temp > stack[-1][0]:
                removed_i = stack.pop()[1]
                answer[removed_i] = cur_i - removed_i
            
            stack.append((cur_temp, cur_i))
        
        return answer