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

        # extract binary search into a helper
        def bin_search(find_starting: bool) -> None:
            # if find_starting is true, find the starting index
            # otherwise, find the ending index
            # return: nothing, modify the result array directly
            l, r = 0, len(nums) - 1

            while r >= l:
                mid = (r + l) // 2

                if nums[mid] == target:
                    if find_starting and (mid - 1 < 0 or nums[mid - 1] != target):
                        res[0] = mid
                        break
                    
                    if not find_starting and (mid + 1 == len(nums) or nums[mid + 1] != target):
                        res[1] = mid
                        break
                    
                    r = mid - 1 if find_starting else r
                    l = mid + 1 if not find_starting else l
                
                elif nums[mid] > target:
                    r = mid - 1
                
                else:
                    # num[mid] < target
                    l = mid + 1
        
        bin_search(find_starting=True)
        bin_search(find_starting=False)

        return res