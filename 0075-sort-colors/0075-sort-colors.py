class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Input: nums = [2,0,2,1,1,0]
        # [0, 0, 2, 1, 1, 2], two_ptr = 4, i = 1
        # [0, 0, 2, 1, 1, 2]
        # [0, 0, 1, 1, 2, 2]

        # [1, 0, 2, 1, 1, 0], two_ptr = 4, i = 1
        # [0, 0, 2, 1, 1, 2]
        # [0, 0, 1, 1, 2, 2]

        # [2, 2, 0, 0]
        # [0, 2, 0, 2]
        zero_ptr, two_ptr = 0, len(nums) - 1
        i = 0

        while i < len(nums):
            num = nums[i]

            if num == 2 and i < two_ptr:
                nums[i], nums[two_ptr] = nums[two_ptr], nums[i]
                two_ptr -= 1
            
            elif num == 0:
                nums[i], nums[zero_ptr] = nums[zero_ptr], nums[i]
                zero_ptr += 1
                i += 1
            
            else:
                i += 1
