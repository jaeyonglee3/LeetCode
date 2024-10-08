class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # First, O(n^2) solution
        # for i, num1 in enumerate(nums):
        #     for j, num2 in enumerate(nums):
        #         if num1 + num2 == target and i != j:
        #             return [i, j]

        # O(n) solution
        seen = {}

        for i, num in enumerate(nums):
            if target - num in seen:
                return [i, seen[target - num]]
            else:
                seen[num] = i
