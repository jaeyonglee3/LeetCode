class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        # nums has at least 3 elements
        p = None
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                if i - 1 == 0:
                    return False
                p = i - 1
                break
            elif nums[i] == nums[i - 1]:
                return False

        if p == None:
            return False
        
        q = None
        for j in range(p + 1, len(nums)):
            if nums[j] > nums[j - 1]:
                if j - 1 == p:
                    return False
                
                q = j - 1
                break
            elif nums[j] == nums[j - 1]:
                return False

        if q == None or q >= len(nums) - 1:
            return False

        for k in range(q + 1, len(nums)):
            if nums[k] <= nums[k - 1]:
                return False
        
        return True