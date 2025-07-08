class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Greedy approach
        # each num in nums represents the max jump length from that index
        
        max_reach = 0
        for i in range(len(nums)):
            if i > max_reach:
                # If you ever reach an index that’s beyond your current maximum reach, then you're stuck
                return False
            max_reach = max(max_reach, i + nums[i])
        return True

