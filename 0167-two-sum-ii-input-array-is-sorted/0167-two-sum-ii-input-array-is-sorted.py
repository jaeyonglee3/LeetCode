class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # paraphrase
        # given a sorted array called numbers, 
        # return a list [a + 1, b + 1] where numbers[a] + numbers[b] == target
        # every input has exactly one solution (we're guanrateed to have a solution)
        
        # dry runs
        # [2,7,11,15]
        # 2 + 7 is 9 so return [1, 2]
        
        # approach
        # have two pointers l, r at the ends of numbers. let sum = nums[l] + num[r]
            # if sum > target: r -= 1
            # if sum < target: l += 1
            # if sum is target: return [l + 1, r + 1]
        
        # implement
        l, r = 0, len(numbers) - 1

        while r > l:
            curr_sum = numbers[l] + numbers[r]

            if curr_sum == target:
                return [l + 1, r + 1]
            elif curr_sum > target:
                r -= 1
            else:
                l += 1