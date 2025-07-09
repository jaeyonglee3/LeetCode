class Solution:
    def jump(self, nums: List[int]) -> int:
        # greedy approach, similar to BFS
        res = 0
        l, r = 0, 0  # tells us the window of the current BFS level

        while r < len(nums) - 1:
            # farthest tells us how far we can jump using vals from the current window
            farthest = 0

            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            
            l = r + 1
            r = farthest
            res += 1
        
        return res
            
