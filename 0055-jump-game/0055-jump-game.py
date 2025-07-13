class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # greedy solution
        # work backwards - the goal started at len(nums) - 1
        # move the goal post back by 1 a bunch of times
        # at the end, assert that its at index 0
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                # move the goal post
                goal = i
        
        return goal == 0