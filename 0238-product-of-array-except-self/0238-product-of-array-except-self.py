class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # if we could use division, we could take product of nums 
        # and divide it by the values of each element
        
        # compute two arrays first, prefix and postfix
        res = [1] * len(nums)
        prefix = 1

        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res
        