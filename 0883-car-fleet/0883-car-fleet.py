class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []  # [(arrival time)]
        cars = list(zip(position, speed))  # [(pos, speed)]
        cars.sort(key=lambda pair : -pair[0])

        # visit the pairs closest to target first
        for pos, speed in cars:
            arrival_time = (target - pos) / speed
            stack.append(arrival_time)

            # smaller arrival time => arriving before the one w/ greater arrival time.
            # if what we just added to the stack (stack[-1]) arrives 
            # before what was already in the stack (stack[-2]), since cars is
            # sorted by closest to dest first, these two cars MUST intersect
            # at some point. so just pop from the stack as long as this is true,
            # and the car we keep in there represents the fleet since its the slowest.
            while len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        # at the end, each "fleet" formed is represented by one "car"
        # that we've kept in the stack, so len(stack) represents total num fleets.
        return len(stack)