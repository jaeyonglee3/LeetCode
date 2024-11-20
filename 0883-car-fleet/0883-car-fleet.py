class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
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
        
        # cars = [list(car) for car in zip(position, speed)] # our stack
        cars = list(zip(position, speed))
        # cars.sort(key=lambda car: car[0])
        res = curr_time = 0

        # while cars:
        #     for car in reversed(cars):
        #         car[0] += car[1]
        #         speeds[car[0]] = min(speeds[car[0]], car[1])
        #         car[1] = speeds[car[0]]
            
        #     if (cars[-1][0] == target):
        #         res += 1
        #         while cars[-1][0] == target:
        #             cars.pop()

        for dist, speed in sorted(cars, reverse=True):
            destination_time = (target - dist)/speed
            if curr_time < destination_time:
                res += 1
                curr_time = destination_time
        
        return res
