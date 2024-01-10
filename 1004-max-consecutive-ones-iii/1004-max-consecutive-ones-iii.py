class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # Incorrect solution
        # l, r = 0, 0
        # num_flipped = 0
        # max_len = 0

        # while r < len(nums):
        #     if nums[r] == 0 and num_flipped != k:
        #         num_flipped += 1
        #         r += 1
        #     elif nums[r] == 0 and num_flipped == k:
        #         l += 1
        #         r = l
        #         num_flipped = 0
        #     else:
        #         r += 1        
            
        #     max_len = max(r - l, max_len)
        
        # return max_len

        l = max_so_far = 0

        for r, num in enumerate(nums):
            k -= 1 if num == 0 else 0

            if k < 0:
                k += 1 if nums[l] == 0 else 0
                l += 1
            else:
                max_so_far = max(r - l + 1, max_so_far)

        return max_so_far