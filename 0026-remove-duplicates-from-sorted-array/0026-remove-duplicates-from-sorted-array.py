class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        i = 0

        while i < len(nums):
            if nums[i] in seen:
                j = i + 1
                while j < len(nums) and nums[j] in seen:
                    j += 1

                if j == len(nums):
                    # No more unique elements can be found in nums
                    return len(seen)
                
                nums[i] = nums[j]
                seen.add(nums[j])
            else:
                seen.add(nums[i])

            i += 1