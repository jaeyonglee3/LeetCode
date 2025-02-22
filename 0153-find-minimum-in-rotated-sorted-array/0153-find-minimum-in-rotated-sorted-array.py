class Solution:
    def findMin(self, nums: List[int]) -> int:
        # O(log n) time + input is sorted = binary search
        res = nums[0]

        if nums[-1] > nums[0]:
            return res
        
        l, r = 0, len(nums) - 1

        while r >= l:
            mid = (r + l) // 2

            if nums[mid] >= nums[0]:
                # Then, min element is in right half
                l = mid + 1
            else:
                r = mid - 1
                res = nums[mid]
        
        return res