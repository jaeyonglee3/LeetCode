class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Input: nums = [1,2,3,4]
        # Output: [24,12,8,6]
        # pre: [1, 1, 2, 6] -> pre[i] equals the product of all the elements to the left of i
        # post: [24, 12, 4, 1] -> post[i] equals the product of all the elements to the right of i
        # THEN, output[i] = pre[i] * post[i]

        # How output was calculated [(2, 3, 4), (1, 3, 4), (1, 2, 4), (1, 2, 3)]
        # it would be nice to know the products up to certain points in the input array
        # so we can do our math quickly

        # compute the pre array
        pre = [1]
        curr = 1
        for i in range(len(nums) - 1):
            # i goes from 0 to the 2nd last index in nums
            curr *= nums[i]
            pre.append(curr)
        
        post = [1]
        curr = 1
        for i in range(len(nums) - 1, 0, -1):
            curr *= nums[i]
            post.append(curr)
        post.reverse()

        res = []
        for i in range(len(nums)):
            res.append(pre[i] * post[i])
        
        return res