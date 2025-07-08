class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # paraphrase
        # given an array nums, return a list of lists, containing all groups of 3
        # numbers from the array that sum to 0
        # no duplicates in groups of 3, and same element can't be used more than once in a group

        # dry runs (examples)
        # nums = [-1,0,1,2,-1,-4]
        # sort_nums = [-4, 2, 2, 2, 2, 5, 5, 5]
        # result = [[-1, 0, -1], [-1, -1, 2]]
        # nums[i] = -1
        # nums[j] = -1
        # nums[k] = 2

        # approach
        # fix the nums[i] number first
        # then, search the rest of the array for two numbers that add up to the negation of nums[i]
        # we can do this using two pointers, 
        # moving them depending on if the sum at the moment if too large or too little
        # add the list of [nums[i], nums[j], nums[k]] to the result

        # implement
        nums.sort()  # O(n log n) operation
        res = []

        for i, num_i in enumerate(nums):
            if i > 0 and nums[i - 1] == num_i:
                continue
                
            target = -num_i
            l, r = i + 1, len(nums) - 1

            while r > l:
                curr_sum = nums[l] + nums[r]

                if curr_sum == target:
                    res.append([num_i, nums[l], nums[r]])
                    r -= 1
                    l += 1
                    while r > 0 and nums[r] == nums[r + 1]:
                        r-= 1
                    while l < len(nums) and nums[l] == nums[l - 1]:
                        l += 1
                elif curr_sum > target:
                    r -= 1
                else:
                    l += 1
        
        return res