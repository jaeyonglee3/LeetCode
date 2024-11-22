class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Key Idea: sort cars by position and iterate in reversed order
        # At each car, calculate time at which destination is reached
        # Compare with lead_car_time. If lead_car_time is smaller, that means they'll form a fleet 
        # because dest_time is greater than lead_car_time
        # res += 1 and curr_time = calculated des time

        # cars = list(zip(position, speed))
        # res = lead_car_time = 0 # lead_car_time is time taken by leading car of curr fleet
        # # in reverse bc cars closer to target have potential to form fleets w cars behind them
        # for dist, speed in sorted(cars, reverse=True): 
        #     destination_hour = (target - dist)/speed
        #     if lead_car_time < destination_hour:
        #         res += 1
        #         lead_car_time = destination_hour
        
        # return res

        # NEETCODE - stack solution
        cars = list(zip(position, speed))
        stack = []
        for dist, speed in sorted(cars, reverse=True):
            stack.append((target - dist)/speed)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                # always popping cars in the fleet with faster speeds 
                # so that only the slowest cars remain
                # and stack eventually only contains 1 car from each fleet.
                stack.pop() 
        
        return len(stack)

