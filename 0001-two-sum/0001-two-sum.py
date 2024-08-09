class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # First, the O(n^2) solution
        # for i, num1 in enumerate(nums):
        #     for j, num2 in enumerate(nums):
        #         if num1 + num2 == target and i != j:
        #             return [i, j]

        # Now, the O(n) with hashmap
        hmap = {}

        for i, num in enumerate(nums):
            if target - num in hmap:
                return [hmap[target - num], i]
            
            hmap[num] = i