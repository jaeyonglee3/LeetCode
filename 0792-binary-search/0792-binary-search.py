class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        mid = (l + r) // 2

        while r - l > 1:
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                l = mid
            else:
                r = mid
            
            mid = (l + r) // 2
        
        if nums[l] == target:
            return l
        elif nums[r] == target:
            return r

        if nums[mid] == target:
            return mid
        
        return -1