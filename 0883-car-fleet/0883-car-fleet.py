class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = []
        # [(pos, speed), (pos, speed)]
        cars = list(zip(position, speed))

        # go through the cars in reverse based on position
        # so that we see the cars closer to target first
        for pos, speed in sorted(cars, reverse=True):
            arrival_time = (target - pos) / speed
            fleets.append(arrival_time)

            # if car just added arrives sooner or at the same time
            # as a car already in fleets (which is ahead of it)
            # they must form a fleet at some point
            # so just remove what you just added
            while len(fleets) >= 2 and fleets[-2] >= fleets[-1]:
                fleets.pop()
        
        return len(fleets)