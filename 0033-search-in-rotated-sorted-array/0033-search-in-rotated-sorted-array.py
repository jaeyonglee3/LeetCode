class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # O(log n) complexity + sorted input -> binary search
        # we will be halving the search window size each time
        # b/c the array is sorted and rotated, there are two sorted portions, left and right
        # we can leverage binary search to determine which portion the target may lie in

        l, r = 0, len(nums) - 1
        while r >= l:
            mid = (r + l) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[0]:
                # we are in the left sorted portion
                if target >= nums[l] and target < nums[mid]:
                    r = mid -1
                else:
                    l = mid + 1
            else:
                # we are in the right sorted portion
                if nums[mid] < target and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1