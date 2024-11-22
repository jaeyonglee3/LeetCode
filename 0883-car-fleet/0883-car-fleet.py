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

        cars = list(zip(position, speed))
        stack = []
        for dist, speed in sorted(cars, reverse=True):
            stack.append((target - dist)/speed)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)

        # OLD FAILED SOL'N + NOTES
        # sort the cars based on their position from target and their speeds too
        # [0, 3, 5, 8, 10] - positions
        # [1, 3, 1, 4, 2] - speeds
        # {0: 1, 3: 3, 5: 1, 8: 4, 10: 2} - slowest speeds
        # while there are remaining cars
            # increment +1 hour of travel time
            # [1, 6, 6, 12, 12] - positions
            # pop off all that are at target, increment result +1
            # [2, 7, 7] - positions
            # [3, 8, 8] - positions
            # [4, 9, 9] - positions
            # ...
            # [7, 12, 12] - positions
            # pop off all that are at target, increment result +1
            # only one car remains, increment result +1
        
        # while cars:
        #     for car in reversed(cars):
        #         car[0] += car[1]
        #         speeds[car[0]] = min(speeds[car[0]], car[1])
        #         car[1] = speeds[car[0]]
            
        #     if (cars[-1][0] == target):
        #         res += 1
        #         while cars[-1][0] == target:
        #             cars.pop()
        # Got stuck here lol

