class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # return (len(set(nums)) != len(nums))

        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            
            hashset.add(n)
        
        return False