class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = max_so_far = 0

        for r, num in enumerate(nums):
            if not num:
                l = r + 1
            else:
                max_so_far = max(max_so_far, r - l + 1)
        
        return max_so_far