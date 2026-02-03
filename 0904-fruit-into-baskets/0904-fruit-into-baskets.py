class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # two infinite baskets which can hold only 1 type
        # start at any tree, pick exactly 1 fruit, put into a basket
        # stop once you reach a tree that cannot fit in the baskets

        # sliding window approach
        # we want to know where the best tree to start at would be

        # 2, 3, 2, 2, 1, 1
        # 2, 2, 2, 3, 3, 3

        # want to know length of longest window that has at most 2 unique elements
        unique_nums = {}
        l = 0
        res = 0

        for r in range(len(fruits)):
            curr_fruit = fruits[r]
            unique_nums[curr_fruit] = unique_nums.get(curr_fruit, 0) + 1

            while len(unique_nums) > 2:
                # we need to tighten the window such that it goes
                # back to having at most 2 unique integers by advancing left ptr
                unique_nums[fruits[l]] -= 1
                if unique_nums[fruits[l]] == 0:
                    del unique_nums[fruits[l]]
                
                l += 1
            
            res = max(res, r - l + 1)
        
        return res


