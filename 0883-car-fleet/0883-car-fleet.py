class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # we can calculate the arrival time of each car: arrival_time = (target - position) / speed
        # cars cannot pass one another, so we know that if car A initially started behind car B
        # and car A arrival_time <= car B arrival time, we know that they've formed a fleet

        # arrival_times[i] is the arrival time of the i-th car
        arrival_times = [(target - position[i]) / speed[i] for i in range(len(position))]
        arrival_and_pos = [(arrival_times[i], position[i]) for i in range(len(position))]
        arrival_and_pos.sort(key=lambda pair : pair[1])

        # now we'll go through each arrival_time, start_position pair in the order
        # of the ones with start_position closer to the target first.
        fleets = []
        while arrival_and_pos:
            curr_arrival_time = arrival_and_pos.pop()[0]
            if not fleets or curr_arrival_time > fleets[-1]:
                # no overlap occurred: the car that started behind ended up at the target LATER
                # so add it as a fleet
                fleets.append(curr_arrival_time)

        return len(fleets)