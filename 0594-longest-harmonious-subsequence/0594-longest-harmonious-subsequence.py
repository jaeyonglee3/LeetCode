class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # if the num - 1 or the num + 1 exists in nums
        # then, num can be a part of a harmonious subsequence
        res = 0
        count = collections.defaultdict(int)

        for n in nums:
            count[n] += 1
        
        for n in count:
            if n - 1 in count:
                res = max(res, count[n] + count[n - 1])
            
            if n + 1 in count:
                res = max(res, count[n] + count[n + 1])
        
        return res