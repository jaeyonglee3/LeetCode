class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # classis sliding window approach
        l, r = 0, 0
        total = 0
        res = math.inf

        while r < len(nums):
            total += nums[r]

            # then, we have a valid subarray formed by nums[l : r + 1]
            while total >= target:
                res = min(r - l + 1, res)  # res becomes the smaller between curr subarray len and past res
                # move the left pointer to attempt to make window smaller
                total -= nums[l]
                l += 1
        
            r += 1
        
        return res if res != math.inf else 0