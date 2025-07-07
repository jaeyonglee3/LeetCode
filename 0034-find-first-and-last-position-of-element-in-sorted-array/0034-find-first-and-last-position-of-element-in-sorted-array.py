class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # paraphrase
        # we're given a sorted array nums
        # find the starting and ending positions of a specific target

        # approach
        # run a binary search
        # we have two targets to find, the starting and ending positions of a specific number

        # nums = [5,7,7,7,7,10,11]

        # find the starting index first
        res = [-1, -1]
        l, r = 0, len(nums) - 1

        while r >= l:
            mid = (l + r) // 2

            if nums[mid] == target:
                if mid - 1 < 0 or nums[mid - 1] != target:
                    # mid is the starting index
                    res[0] = mid
                    break
                else:
                    r = mid - 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        # find the ending index next
        l, r = 0, len(nums) - 1

        while r >= l:
            mid = (l + r) // 2

            if nums[mid] == target:
                if mid + 1 == len(nums) or nums[mid + 1] != target:
                    # mid is the ending index
                    res[1] = mid
                    break
                else:
                    l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return res