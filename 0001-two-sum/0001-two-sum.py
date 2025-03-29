class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # O(n) where n = len(nums)

        seen = {}  # maps values to index in array

        for i, n in enumerate(nums):
            diff = target - n

            if diff in seen:
                return [i, seen[diff]]
            
            seen[n] = i