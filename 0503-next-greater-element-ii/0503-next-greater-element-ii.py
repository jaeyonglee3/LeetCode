class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []  # monotonically decreasing storing (index, value)
        res = [-1] * n

        for i in range(n * 2):
            i %= n
            curr_val = nums[i]

            while stack and stack[-1][1] < curr_val:
                idx, _ = stack.pop()
                res[idx] = curr_val

            stack.append((i, curr_val))
        
        return res