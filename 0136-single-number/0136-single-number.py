class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for x in nums:
            duplicate = False
            target = x
            temp_list = nums.copy()
            temp_list.remove(x)

            if target in temp_list:
                duplicate = True

            if duplicate == False:
                return target
        