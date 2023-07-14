class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        k = 1

        for i in range(1, len(nums)):
            if nums[i] not in nums[:j]:
                # swap nums[i] with nums[j]
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
                k += 1
            else:
                pass

        return k

            