class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # want to find the maximum length window over the fruits array
        # that contains at most 2 unique integers
        l = 0
        res = 0
        unique_nums = {}

        for r in range(len(fruits)):
            unique_nums[fruits[r]] = unique_nums.get(fruits[r], 0) + 1

            while len(unique_nums) > 2:
                # we need to tighten the window such that it goes
                # back to having at most 2 unique integers by advancing left ptr
                l += 1
                
                fruit_removed = fruits[l - 1]
                unique_nums[fruit_removed] -= 1

                if unique_nums[fruit_removed] == 0:
                    del unique_nums[fruit_removed]

            res = max(res, r - l + 1)
        
        return res