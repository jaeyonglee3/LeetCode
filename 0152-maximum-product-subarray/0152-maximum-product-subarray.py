import math
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return 0

        max_product = -math.inf
        min_product = math.inf
        result = -math.inf

        for num in nums:
            if num < 0:
                # Swap when encountering a negative number
                max_product, min_product = min_product, max_product

            max_product = max(num, max_product * num)
            min_product = min(num, min_product * num)

            result = max(result, max_product)

        return result
