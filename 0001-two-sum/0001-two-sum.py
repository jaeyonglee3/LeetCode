class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # maps the number to its index in nums
        seen = {}

        for i, n in enumerate(nums):
            difference = target - n

            if difference in seen:
                return [i, seen[difference]]
            
            seen[n] = i
