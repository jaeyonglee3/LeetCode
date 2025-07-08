class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Greedy approach
        # each num in nums represents the max jump length from that index
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        
        return goal == 0
