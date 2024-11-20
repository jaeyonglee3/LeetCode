class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # P - return an array ans where ans[i] represents the number of days before a warmer temp than temp on i-th day
        # C - 
        # L -
        # I - use stack. push until you reach temp that is higher than starting temp. Pop until you reach starting temp. Count num pops. add count to answers arr
        # M -
        # T -

        # Naive solution with for loop and nested while loop, TLE
        # answer = []
        # for i, temp in enumerate(temperatures):
        #     if i != len(temperatures) - 1:
        #         day_count = 1
        #         next_temp = i + 1
            
        #         while temperatures[next_temp] <= temp and next_temp < len(temperatures) - 1:
        #             next_temp += 1
        #             day_count += 1
                
        #         if temperatures[next_temp] > temp:
        #             answer.append(day_count)
        #         else:
        #             answer.append(0)

        #     else:
        #         answer.append(0)
    
        # return answer

        # TLE
        # answer = []
        # t_stack = []
        # for i, temp in enumerate(temperatures):
        #     if (i == len(temperatures) - 1):
        #         answer.append(0)
        #     else:
        #         t_stack.append(temp)
        #         next_temp = i + 1

        #         # push until youve pushed smth greater
        #         while next_temp < len(temperatures) and temperatures[next_temp] <= temp:
        #             t_stack.append(temperatures[next_temp])
        #             next_temp += 1
                
        #         if next_temp > len(temperatures) - 1:
        #             answer.append(0)
        #         else:
        #             # pop until youre at temp again
        #             while t_stack[-1] != temp:
        #                 t_stack.pop()
                    
        #             answer.append(next_temp - i) # Calculate num_popped directly
                    
        # return answer
        
        res = [0] * len(temperatures)
        t_stack = [] # Pair: (temp, index)

        for i, temp in enumerate(temperatures):
            while t_stack and temp > t_stack[-1][0]:
                removed = t_stack.pop()
                res[removed[1]] = i - removed[1]
            
            t_stack.append((temp, i))
        
        return res