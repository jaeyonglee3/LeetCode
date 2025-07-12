class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # time: O(n), space: O(1)
        
        # edge case
        # if the total amount of gas is less than the total of the costs, its impossible
        if sum(gas) < sum(cost):
            return -1
        
        # now, its guaranteed to be possible, since edge case wasn't true
        tank = 0
        starting_i = 0

        for i in range(len(gas)):
            tank += gas[i] - cost[i]

            if tank < 0:
                # then, i is not a valid starting position bc we run out of gas
                # reset the tank back to zero
                # make the starting index be the next index after this one
                tank = 0
                starting_i = i + 1
        
        return starting_i
