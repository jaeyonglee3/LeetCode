class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Say we have car A and car B
        
        # If car A starts behind car B but will arrive at target FASTER than
        # or at the SAME TIME as car B, it must have caught up to it at some point
        # meaning they formed a fleet (cars cannot pass each other)

        # We can calculate each car's time that it would take to reach target with
        # time = (target - position) / speed

        # if we sort by the cars arriving first (shortest time to target)
        # and examine them in that order, we can compare each arriving car's
        # starting positions to determine if they ever formed a fleet

        # position = [10,8,0,5,3], speed = [2,4,1,1,3]
        # target = 12

        # arrival times stores (time, start_pos) tuples
        # arrival_times = [(1, 10), (1, 8), (12, 0), (7, 5), (3, 3)]
        # arrival_times = [(1, 10), (1, 8), (7, 5), (3, 3), (12, 0)]
        # fleets = 3

        pos_and_spd = list(zip(position, speed))
        arrival_times = [((target - pos) / spd, pos) for pos, spd in pos_and_spd]
        arrival_times.sort(key=lambda pair : pair[1], reverse=True)  # sort by position in reverse

        fleets = []  # monotonically increasing
        for time, pos in arrival_times:
            if not fleets or fleets[-1] < time:
                fleets.append(time)
        
        return len(fleets)