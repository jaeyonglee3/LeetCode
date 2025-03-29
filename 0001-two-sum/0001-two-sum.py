class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # O(n) runtime, where n = len(nums)
        # O(n) space, for the seen hashmap

        seen = {}  # maps values to index in array

        for i, n in enumerate(nums):
            diff = target - n

            if diff in seen:
                return [i, seen[diff]]
            
            seen[n] = i