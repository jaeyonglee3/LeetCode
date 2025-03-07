class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), key=lambda pair: -pair[0])  # Sort by position (descending)
        fleets = 0
        last_arrival_time = 0  # Tracks the slowest car leading a fleet

        for pos, spd in cars:
            arrival_time = (target - pos) / spd  # Time to reach the target
            
            # If this car arrives later, it forms a new fleet
            if arrival_time > last_arrival_time:
                fleets += 1
                last_arrival_time = arrival_time  # Update slowest fleet leader
        
        return fleets