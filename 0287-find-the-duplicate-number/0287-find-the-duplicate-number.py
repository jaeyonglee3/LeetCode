class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tortoise, hare = 0, 0

        # Phase 1
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]

            if tortoise == hare:
                break

        # Phase 2
        tortoise2 = 0
        while True:
            tortoise = nums[tortoise]
            tortoise2 = nums[tortoise2]
            if tortoise == tortoise2:
                return tortoise
