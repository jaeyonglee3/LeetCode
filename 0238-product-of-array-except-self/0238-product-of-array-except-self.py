class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # we'll construct a post and prefix array. at index i, postfix contains
        # the product of all the numbers to the right of i in nums. prefix contains
        # the product of all the numbers to the left of i in nums.
        # then the result at i is the product of prefix[i] and postfix[i]
        
        pre = []
        curr_pre = 1
        for n in nums:
            pre.append(curr_pre)
            curr_pre = curr_pre * n
        
        post = [-1] * len(nums)
        curr_post = 1
        for i in range(len(nums) - 1, -1, -1):
            post[i] = curr_post
            curr_post *= nums[i]
        
        res = []
        for i in range(len(nums)):
            res.append(pre[i] * post[i])
        
        return res
