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

        # [0, 3, 5, 8, 10] - positions
        # [1, 3, 1, 4, 2] - speeds
        # [(10, 2), (8, 4), (5, 1), (3, 3), (0, 1)]
        # dest = 1, curr_time = 0, res += 1, curr_time = 1
        # dest = 1, curr_time = 1, res += 0, curr_time = 1
        # dest = 7, curr_time = 1, res += 1, curr_time = 7
        # dest = 3, curr_time = 7, res += 0, curr_time = 7
        # dest = 12, curr_time = 7, res += 1, curr_time = 12
        # return res = 3
        for dist, speed in sorted(cars, reverse=True):
            destination_hour = (target - dist)/speed
            if curr_time < destination_hour:
                res += 1
                curr_time = destination_hour
        
        return res
