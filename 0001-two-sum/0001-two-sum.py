class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # maps values : index

        for i, val in enumerate(nums):
            diff = target - val

            if diff in seen:
                return [i, seen[diff]]
            else:
                seen[val] = i
