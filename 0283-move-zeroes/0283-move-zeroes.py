class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0

        for r in range(len(nums)):
            if nums[r] != 0:
                # perform a swap whenever nums[r] is non-zero
                nums[l], nums[r] = nums[r], nums[l]
                # after swap, nums[l] if guaranteed to be non-zero
                # so only then, increment l ptr
                l += 1
