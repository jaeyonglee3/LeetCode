class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # Naive solution, list.sort takes O(nlogn)
        clean = list(set(nums))
        if len(clean) < 3:
            return max(nums)

        clean.sort()
        return clean[-3]