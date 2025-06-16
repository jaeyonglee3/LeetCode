class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        # so we need triplets of numbers a, b, and c.
        # lets iterate over nums, fix an a, and find b and c
        # such that b + c = -a, meaning a + b + c = 0
        for i_a, a in enumerate(nums):
            if i_a > 0 and a == nums[i_a - 1]:
                continue

            target = -a
            l, r = i_a + 1, len(nums) - 1

            while r > l:
                curr = nums[l] + nums[r]
                
                if curr == target:
                    res.append([a, nums[r], nums[l]])
                    # We only skip over duplicates of nums[l] and nums[r] after we’ve used them in a result, to avoid repeating the same triplet. 
                    # But if there’s no match, we’re free to explore all options — including duplicates — because they might eventually 
                    # contribute to a valid triplet with a different combination.
                    while l < len(nums) - 1 and nums[l] == nums[l + 1]:
                        l += 1
                    while r > 0 and nums[r] == nums[r - 1]:
                        r -= 1
                    r -= 1
                    l += 1
                elif curr > target:
                    r -= 1
                else:
                    l += 1
        
        return res