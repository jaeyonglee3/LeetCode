class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # looking for the minimal k value satisfying nums[k] >= target
        left, right = 0, len(nums)

        while left < right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        
        return left