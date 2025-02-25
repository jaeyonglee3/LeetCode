class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1  # this pointer tells us where to put the unique value that we run into

        # right pointer looks for unique elements by checking if nums[r] != nums[r - 1]
        # (this works because the input array is sorted)
        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                # a new unique element is found so set the value at l ptr to val at r ptr
                # and increment left ptr by one since we've put a unique value there
                nums[l] = nums[r]
                l += 1
        
        # at the end, the left ptr stops one index to the right of the last unqiue element
        return l