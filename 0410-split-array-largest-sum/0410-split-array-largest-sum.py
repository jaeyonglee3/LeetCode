class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def feasible(num: int) -> bool:
            total = 0
            count = 1

            for x in nums:
                total += x
                if total > num:
                    count += 1
                    total = x
                    if count > k:
                        return False
            
            return True

        # define search boundary for bin search
        left, right = max(nums), sum(nums)

        while left < right:
            mid = (left + right) // 2

            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        
        return left