class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # the question guarantees nums to have at least 1
        # element that occurs more than half the time in the array

        result, count = nums[0], 0

        for n in nums:
            if count != 0:
                if n == result:
                    count += 1
                else:
                    count -= 1
            else:
                count = 1
                result = n
        
        return result