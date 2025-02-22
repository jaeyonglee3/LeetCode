class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_set = set(nums)
        
        for n in num_set:
            if nums.count(n) > len(nums) // 2:
                return n