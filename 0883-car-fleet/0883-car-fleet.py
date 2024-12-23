class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Hold all fleets in a stack (nested array), each element is a fleet
        # Iterate array in reverse. Calculate arrival time of each car (target-position)/speed
        # If a car that is behind a car arrives sooner or at the same time, 
        # the two must overlap and form a fleet at some point
        # pop off the one travelling at a faster speed
        # (fleets travel at the speed of the slowest car)

        fleets = []
        cars = list(zip(position, speed))

        for pos, speed in sorted(cars, reverse=True):
            fleets.append((target-pos)/speed)

            # Check if car just added arrives sooner or 
            # at same time than the car ahead of it
            # but only check if >= 2 fleets currently
            if len(fleets) >= 2 and fleets[-1] <= fleets[-2]:
                fleets.pop()
        
        return len(fleets)



        