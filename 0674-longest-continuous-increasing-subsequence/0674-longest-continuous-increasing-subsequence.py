class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        count, max_count = 1, 1

        for i in range(len(nums) - 1):
            if nums[i + 1] > nums[i]:
                count += 1
                if count > max_count:
                    max_count = count
            else:
                count = 1
        
        return max_count
