class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # for any index i, we know that the result at i should be
        # the product of...
            # the product of all the numbers that come before index i in nums
            # with
            # the product of all the numbers that come after index i in nums
        
        # so, construct two arrays prefix and postfix
        # prefix at index i equals the product of all the numbers that come before index i in nums
        # postfix at index i equals the product of all the numbers that come after index i in nums
        n = len(nums)
        
        prefix = []
        curr_product = 1
        for num in nums:
            prefix.append(curr_product)
            curr_product *= num
        
        postfix = [-1] * n
        curr_idx = n - 1
        curr_product = 1
        for i in range(n - 1, -1, -1):
            postfix[curr_idx] = curr_product
            curr_product *= nums[i]
            curr_idx -= 1
        
        result = []
        for i in range(n):
            result.append(prefix[i] * postfix[i])
        
        return result