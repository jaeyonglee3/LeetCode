class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        res = 0

        for l in range(len(nums)):
            even_nums, odd_nums = set(), set()
            
            for r in range(l, len(nums)):
                if nums[r] % 2 == 0:
                    # even
                    even_nums.add(nums[r])
                else:
                    odd_nums.add(nums[r])
                
                if len(even_nums) == len(odd_nums):
                    res = max(res, r - l + 1)
        
        return res