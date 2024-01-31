class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        curr_sum = 0

        for n in nums:
            curr_sum += n
            res.append(curr_sum)
        
        return res