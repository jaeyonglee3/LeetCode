class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Attempt 1 (correct), unnecessary to start l and r at index of first zero
        # first_zero = nums.index(0) if 0 in nums else -1
        # if first_zero == -1:
        #     return

        # l, r = first_zero, first_zero

        # while r + 1 < len(nums):
        #     r += 1
        #     if nums[r] != 0:
        #         nums[l], nums[r] = nums[r], nums[l]
        #         l += 1
        
        l = 0
        for r in range(len(nums)):
            if nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1