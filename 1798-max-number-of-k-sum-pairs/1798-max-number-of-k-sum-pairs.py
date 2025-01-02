class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        res = 0

        for num in nums:
            if seen[k - num] > 0:
                seen[k - num] -= 1
                res += 1
            else:
                seen[num] += 1
        
        return res