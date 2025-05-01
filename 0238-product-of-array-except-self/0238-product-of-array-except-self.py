class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        pre, post = [], [-1] * len(nums)
        curr_pre, curr_post = 1, 1

        for n in nums:
            pre.append(curr_pre)
            curr_pre *= n
        
        for i in range(len(nums) - 1, -1, -1):
            post[i] = curr_post
            curr_post *= nums[i]
        
        return [pre[i] * post[i] for i in range(len(nums))]
